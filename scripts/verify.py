import os
import re
import urllib.parse
import urllib.request
import json
import time
import pathlib
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# ==========================================
# CONFIGURAÇÕES
# ==========================================
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Definição dos caminhos base do projeto
RAIZ_PROJETO = os.path.abspath('.')
DOCS_DIR = os.path.abspath('./src/content/docs')
ASSETS_DIR = os.path.abspath('./src/assets')

# Estrutura centralizada para armazenar os logs da execução global
relatorio = {
    'renomeados': [],
    'imagens': [],
    'links_fix': [],
    'links_quebrados': [],
    'traducoes': [],
    'deletados': [],
    'erros': []
}

# Mapeamento auxiliar de códigos para nomes extensos (usado pelo Gemini)
IDIOMAS_MAP = {
    'en': 'English',
    'es': 'Spanish (Castilian)',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'ja': 'Japanese',
    'zh': 'Chinese (Simplified)'
}

def enviar_discord():
    """Avalia o log acumulado e envia o relatório formatado para o Discord."""
    if not DISCORD_WEBHOOK_URL or DISCORD_WEBHOOK_URL == 'SEU_WEBHOOK_AQUI':
        print("\n⚠️ Webhook do Discord não configurado. Pulando etapa de notificação.")
        return

    total_eventos = sum(len(lista) for lista in relatorio.values())
    
    if total_eventos == 0:
        print("\n✨ Nenhuma alteração feita e nenhum erro encontrado. O Discord não será notificado.")
        return

    print("\n📨 Preparando envio do relatório para o Discord...")

    def formatar_lista(lista, limite=10):
        if not lista: return ""
        linhas = [f"  • {item}" for item in lista[:limite]]
        if len(lista) > limite:
            linhas.append(f"  • *(... e mais {len(lista) - limite} ocorrências)*")
        return "\n".join(linhas)

    mensagem = "🚨 **Relatório de Automação da Wiki** 🚨\n\n"

    if relatorio['renomeados']:
        mensagem += f"🔄 **Arquivos Renomeados (Pt-Br): {len(relatorio['renomeados'])}**\n"
        mensagem += f"{formatar_lista(relatorio['renomeados'])}\n\n"

    if relatorio['links_fix']:
        mensagem += f"🔗 **Links Absolutos Ajustados (Pt-Br): {len(relatorio['links_fix'])}**\n"
        mensagem += f"{formatar_lista(relatorio['links_fix'])}\n\n"

    if relatorio['imagens']:
        mensagem += f"🖼️ **Imagens Corrigidas: {len(relatorio['imagens'])}**\n"
        mensagem += f"{formatar_lista(relatorio['imagens'])}\n\n"

    if relatorio['traducoes']:
        mensagem += f"🌐 **Artigos Traduzidos/Atualizados: {len(relatorio['traducoes'])}**\n"
        mensagem += f"{formatar_lista(relatorio['traducoes'])}\n\n"

    if relatorio['deletados']:
        mensagem += f"🗑️ **Arquivos Órfãos Removidos: {len(relatorio['deletados'])}**\n"
        mensagem += f"{formatar_lista(relatorio['deletados'])}\n\n"

    if relatorio['links_quebrados']:
        mensagem += f"⚠️ **Links Internos Não Resolvidos: {len(relatorio['links_quebrados'])}**\n"
        mensagem += f"{formatar_lista(relatorio['links_quebrados'])}\n\n"

    if relatorio['erros']:
        mensagem += f"❌ **Erros de Execução: {len(relatorio['erros'])}**\n"
        mensagem += f"{formatar_lista(relatorio['erros'])}\n\n"

    payload = {'content': mensagem}
    dados = json.dumps(payload).encode('utf-8')
    
    req = urllib.request.Request(
        DISCORD_WEBHOOK_URL, 
        data=dados, 
        headers={'Content-Type': 'application/json', 'User-Agent': 'Python/ScriptMonitor'}
    )

    try:
        urllib.request.urlopen(req)
        print("✅ Relatório enviado com sucesso para o Discord!")
    except Exception as e:
        print(f"❌ Falha ao enviar para o Discord: {e}")


def desduplicar_artigos_pt_br():
    """Garante nomes únicos dentro do escopo do pt-br antes da tradução."""
    pt_br_dir = os.path.join(DOCS_DIR, 'pt-br')
    if not os.path.exists(pt_br_dir):
        print("⚠️ Pasta 'pt-br' não encontrada para desduplicação.")
        relatorio['erros'].append("Pasta 'pt-br' não encontrada.")
        return

    arquivos_por_nome = {}
    nomes_ocupados_globalmente = set()
    
    for root, _, files in os.walk(pt_br_dir):
        for file in files:
            if file.endswith(('.md', '.mdx')):
                nome_sem_ext = os.path.splitext(file)[0]
                nomes_ocupados_globalmente.add(nome_sem_ext)
                if file not in arquivos_por_nome:
                    arquivos_por_nome[file] = []
                arquivos_por_nome[file].append(os.path.join(root, file))

    print("🔍 Verificando duplicatas de nomes de artigos em 'pt-br'...")
    
    for file, paths in arquivos_por_nome.items():
        if len(paths) > 1:
            paths_ordenados = sorted(paths, key=os.path.getmtime)
            for i in range(1, len(paths_ordenados)):
                caminho_atual = paths_ordenados[i]
                diretorio_atual = os.path.dirname(caminho_atual)
                nome_orig_sem_ext, ext = os.path.splitext(file)
                
                contador = 1
                while True:
                    proposto_sem_ext = f"{nome_orig_sem_ext}-{contador}"
                    novo_nome = f"{proposto_sem_ext}{ext}"
                    novo_caminho = os.path.join(diretorio_atual, Rails_nome := novo_nome)
                    
                    if proposto_sem_ext not in nomes_ocupados_globalmente and not os.path.exists(novo_caminho):
                        break
                    contador += 1 
                
                try:
                    os.rename(caminho_atual, novo_caminho)
                    log_msg = f"{os.path.basename(caminho_atual)} -> {novo_nome}"
                    print(f" 🔄 Renomeado: {log_msg}")
                    relatorio['renomeados'].append(log_msg)
                    nomes_ocupados_globalmente.add(proposto_sem_ext)
                except Exception as e:
                    erro_msg = f"Erro ao renomear {caminho_atual}: {e}"
                    print(f" ❌ {erro_msg}")
                    relatorio['erros'].append(erro_msg)


def corrigir_formatacao_customizada(content):
    """Corrige problemas comuns de espaçamento em negritos seguidos de dois pontos."""
    # Exemplo: **Host** : -> **Host**:
    return re.sub(r'\*\*([^*]+)\*\*\s+:', r'**\1**:', content)


def mapear_assets():
    index = {}
    if not os.path.exists(ASSETS_DIR):
        return index
    for root, _, files in os.walk(ASSETS_DIR):
        for file in files:
            index[file] = os.path.join(root, file)
    return index

def mapear_artigos():
    index = {}
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(('.md', '.mdx')):
                nome_sem_ext = os.path.splitext(file)[0]
                caminho_abs = os.path.join(root, file)
                if nome_sem_ext not in index:
                    index[nome_sem_ext] = []
                index[nome_sem_ext].append(caminho_abs)
    return index


def obter_idiomas_disponiveis(docs_path):
    """Varre as pastas existentes em src/content/docs para descobrir os idiomas ativos."""
    idiomas = {}
    if not docs_path.exists():
        return idiomas
    for item in docs_path.iterdir():
        if item.is_dir() and item.name != 'pt-br' and len(item.name) <= 5:
            idiomas[item.name] = IDIOMAS_MAP.get(item.name, item.name.upper())
    return idiomas


def traduzir_conteudo(conteudo_md, idioma_destino):
    """
    Traduz documentação Markdown preservando estrutura,
    código, frontmatter e links.
    """

    if not OPENAI_API_KEY:
        print("⚠️ Chave API da OpenAI não configurada.")
        return None

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)

        system_prompt = """
Você é um tradutor técnico especialista em documentação de TI,
Markdown, Astro Starlight e documentação de software.

REGRAS OBRIGATÓRIAS:

1. Preserve integralmente a estrutura Markdown.
2. Preserve integralmente o frontmatter entre ---.
3. Traduza apenas os valores textuais do frontmatter.
4. Nunca altere as chaves YAML.
5. Nunca altere caminhos de imagens.
6. Nunca altere URLs.
7. Preserve blocos de código exatamente como estão.
8. Dentro dos blocos de código:
   - Traduza apenas comentários humanos.
   - Nunca altere comandos, variáveis, funções, APIs, nomes técnicos ou sintaxe.
9. Preserve tabelas Markdown.
10. Preserve anchors, IDs, referências e formatação.
11. Retorne SOMENTE o conteúdo Markdown traduzido.
12. Não use cercas ```markdown.
13. Não adicione explicações.
14. Não resuma conteúdo.
"""

        user_prompt = f"""
Traduza o documento abaixo para {idioma_destino}.

DOCUMENTO:

{conteudo_md}
"""

        response = client.chat.completions.create(
            model=os.getenv('OPENAI_MODEL'),
            #temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        erro_msg = f"Erro na API OpenAI: {e}"
        print(f" ❌ {erro_msg}")
        relatorio['erros'].append(erro_msg)
        return None


def sincronizar_e_traduzir():
    """Gerencia a internacionalização e a correção de links pós-tradução."""
    print("\n🌐 Iniciando sincronização e tradução automática de idiomas...")
    docs_path = pathlib.Path(DOCS_DIR)
    pt_dir = docs_path / "pt-br"

    if not pt_dir.exists():
        return

    target_languages = obter_idiomas_disponiveis(docs_path)
    if not target_languages:
        print("ℹ️ Nenhum outro idioma configurado na pasta docs além de pt-br.")
        return

    # --- PASSO 1: ATUALIZAR E TRADUZIR ---
    for pt_file in pt_dir.rglob("*.md*"):
        if not pt_file.is_file():
            continue

        relative_path = pt_file.relative_to(pt_dir)
        with open(pt_file, "r", encoding="utf-8") as f:
            pt_content = f.read()
            
        pt_mtime = pt_file.stat().st_mtime
        
        for lang_code, lang_name in target_languages.items():
            target_file = docs_path / lang_code / relative_path
            
            if not target_file.exists() or pt_mtime > target_file.stat().st_mtime:
                print(f"🚀 Traduzindo [{lang_code.upper()}]: {relative_path}")
                
                conteudo_traduzido = traduzir_conteudo(pt_content, lang_name)
                
                if conteudo_traduzido:
                    # CORREÇÃO DE LINKS ABSOLUTOS DIRECIONADOS AO IDIOMA CORRETO
                    conteudo_traduzido = re.sub(r'\]\(/pt-br/', f'](/{lang_code}/', conteudo_traduzido)
                    conteudo_traduzido = re.sub(r'href="/pt-br/', f'href="/{lang_code}/', conteudo_traduzido)
                    conteudo_traduzido = re.sub(r'src="/pt-br/', f'src="/{lang_code}/', conteudo_traduzido)

                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    with open(target_file, "w", encoding="utf-8") as f:
                        f.write(conteudo_traduzido)
                        
                    log_msg = f"[{lang_code.upper()}] {relative_path}"
                    relatorio['traducoes'].append(log_msg)
                    time.sleep(2) 

    # --- PASSO 2: LIMPAR DELETADOS ---
    for lang_code in target_languages.keys():
        lang_dir = docs_path / lang_code
        if lang_dir.exists():
            for target_file in lang_dir.rglob("*.md*"):
                if not target_file.is_file():
                    continue
                relative_path = target_file.relative_to(lang_dir)
                corresponding_pt_file = pt_dir / relative_path
                
                if not corresponding_pt_file.exists():
                    log_msg = f"[{lang_code.upper()}] {relative_path}"
                    print(f"🗑️ Removendo arquivo órfão: {log_msg}")
                    relatorio['deletados'].append(log_msg)
                    target_file.unlink()
                    
                    if not any(target_file.parent.iterdir()):
                        target_file.parent.rmdir()


def processar_wiki():
    # 1. Executa a desduplicação de arquivos pt-br
    desduplicar_artigos_pt_br()
    
    asset_index = mapear_assets()
    artigos_index = mapear_artigos()
    
    pattern = re.compile(r'(!?)\[(.*?)\]\((.*?)\)')
    arquivos_corrigidos = 0

    print("\n🔍 Iniciando varredura e correções locais em 'pt-br'...")

    pt_br_dir = os.path.join(DOCS_DIR, 'pt-br')
    if not os.path.exists(pt_br_dir):
        return

    for root, _, files in os.walk(pt_br_dir):
        for file in files:
            if file.endswith(('.md', '.mdx')):
                filepath = os.path.join(root, file)
                file_dir = os.path.dirname(filepath)
                nome_arquivo_atual = os.path.basename(filepath)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # CORREÇÃO DE FORMATAÇÃO (Negrito e Dois Pontos)
                content_ajustado = corrigir_formatacao_customizada(content)
                modificado = (content_ajustado != content)
                content = content_ajustado

                def master_replacer(match):
                    nonlocal modificado
                    
                    is_image = bool(match.group(1))
                    text = match.group(2)
                    raw_path = match.group(3).strip()
                    path = urllib.parse.unquote(raw_path)

                    if path.startswith(('http://', 'https://', '//', 'mailto:')) or (not is_image and path.startswith('#')):
                        return match.group(0)

                    if is_image:
                        system_img_path = path.replace('/', os.sep)
                        nome_imagem = os.path.basename(system_img_path)

                        if nome_imagem in asset_index:
                            caminho_real_absoluto = asset_index[nome_imagem]
                            novo_caminho_relativo = os.path.relpath(caminho_real_absoluto, file_dir).replace('\\', '/')

                            if novo_caminho_relativo != raw_path:
                                modificado = True
                                log_msg = f"[{nome_arquivo_atual}] Imagem ajustada"
                                if log_msg not in relatorio['imagens']:
                                    relatorio['imagens'].append(log_msg)
                                return f"![{text}]({novo_caminho_relativo})"
                        return match.group(0)

                    else:
                        base_path = path
                        anchor = ""
                        if '#' in path:
                            base_path, anchor = path.split('#', 1)
                            anchor = f"#{anchor}"

                        system_link_path = base_path.replace('/', os.sep).rstrip(os.sep)
                        nome_alvo = os.path.basename(system_link_path)
                        nome_alvo_sem_ext = os.path.splitext(nome_alvo)[0]

                        if not nome_alvo_sem_ext or nome_alvo_sem_ext not in artigos_index:
                            log_quebrado = f"[{nome_arquivo_atual}] ➔ {raw_path}"
                            if log_quebrado not in relatorio['links_quebrados']:
                                relatorio['links_quebrados'].append(log_quebrado)
                                print(f" ⚠️ Não encontrado: {log_quebrado}")
                            return match.group(0)

                        rel_to_docs = os.path.relpath(filepath, DOCS_DIR)
                        partes_dir = rel_to_docs.split(os.sep)
                        idioma_atual = partes_dir[0] if len(partes_dir) > 1 else ''

                        caminho_real_absoluto_destino = None
                        target_rel_to_docs = None

                        for caminho_possivel in artigos_index[nome_alvo_sem_ext]:
                            target_rel = os.path.relpath(caminho_possivel, DOCS_DIR)
                            target_partes = target_rel.split(os.sep)
                            
                            if target_partes[0] == idioma_atual:
                                caminho_real_absoluto_destino = caminho_possivel
                                target_rel_to_docs = target_rel
                                break

                        if caminho_real_absoluto_destino and target_rel_to_docs:
                            caminho_web = os.path.splitext(target_rel_to_docs)[0].replace('\\', '/')
                            if caminho_web.endswith('/index'): caminho_web = caminho_web[:-6]
                            elif caminho_web == 'index': caminho_web = ''

                            novo_caminho_absoluto = f"/{caminho_web}{anchor}"
                            
                            if novo_caminho_absoluto != raw_path:
                                modificado = True
                                log_msg = f"[{nome_arquivo_atual}] ➔ {novo_caminho_absoluto}"
                                if log_msg not in relatorio['links_fix']:
                                    relatorio['links_fix'].append(log_msg)
                                return f"[{text}]({novo_caminho_absoluto})"
                        
                        return match.group(0)

                new_content = pattern.sub(master_replacer, content)

                if modificado or new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    arquivos_corrigidos += 1

    print("🚀 Correções locais concluídas.")
    
    # 2. Roda a rotina de tradução automática baseando-se no pt-br consolidado
    sincronizar_e_traduzir()
    
    # 3. Dispara o relatório consolidado para o Discord
    enviar_discord()

if __name__ == '__main__':
    processar_wiki()
