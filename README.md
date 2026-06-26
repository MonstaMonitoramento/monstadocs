# Monsta Docs

[![Built with Starlight](https://astro.badg.es/v2/built-with-starlight/tiny.svg)](https://starlight.astro.build)

Bem-vindo ao Monsta Docs, a wiki oficial da plataforma de monitoramento Monsta. Este repositório contém todos os artigos, tutoriais e documentações de referência para ajudar você a extrair o máximo do Monsta.

## 🚀 Estrutura do Conteúdo

O conteúdo da documentação está localizado em `src/content/docs/` e é organizado por idioma. A estrutura de diretórios para o conteúdo em português (`pt-br`) é a seguinte, servindo de modelo para os outros idiomas:

```
src/content/docs/
├── en/
│   └── ... (mesma estrutura do pt-br)
├── es/
│   └── ... (mesma estrutura do pt-br)
└── pt-br/
    ├── extra/
    │   ├── configuracao-equipamentos/
    │   ├── hyper-v/
    │   ├── linux/
    │   ├── mikrotik/
    │   ├── windows/
    │   └── wmi-configuracao/
    ├── faq/
    │   ├── alertas-notificacoes/
    │   ├── conceitos-fundamentais/
    │   ├── contratacao-licenciamento/
    │   ├── problemas-acesso/
    │   ├── problemas-coleta/
    │   └── problemas-licenca/
    ├── manual/
    │   ├── barra-superior/
    │   ├── configuracoes/
    │   ├── dispositivos/
    │   ├── grupos-alertas/
    │   ├── linha-tempo/
    │   ├── paineis/
    │   └── manual-usuario.md
    ├── start/
    │   ├── conceitos-iniciais/
    │   ├── instalacao/
    │   ├── licenca-assinatura/
    │   └── migracao/
    ├── tech/
    │   ├── arquitetura-comunicacao/
    │   ├── guias-tecnicos/
    │   ├── modulos-script/
    │   ├── protocolos-coleta/
    │   ├── tutoriais-monsta/
    │   └── datasheet.md
    └── index.md
```

O Starlight busca por arquivos `.md` ou `.mdx` no diretório `src/content/docs/`. Cada arquivo é exposto como uma rota com base no nome do arquivo.

Imagens podem ser adicionadas em `src/assets/` e incorporadas no Markdown com um link relativo.

Ativos estáticos, como favicons, podem ser colocados no diretório `public/`.

## 🧞 Comandos

Todos os comandos são executados a partir da raiz do projeto, em um terminal:

| Command                   | Ação                                                               |
| :------------------------ | :----------------------------------------------------------------- |
| `npm install`             | Instala as dependências                                            |
| `npm run dev`             | Inicia o servidor de desenvolvimento em `localhost:4321`           |
| `npm run build`           | Compila o site para produção no diretório `./dist/`                |
| `npm run preview`         | Pré-visualiza a compilação localmente, antes de implantar           |
| `npm run astro ...`       | Executa comandos da CLI do Astro, como `astro add` e `astro check` |
| `npm run astro -- --help` | Obtém ajuda sobre o uso da CLI do Astro                            |
