import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async ({ site }) => {
    // Busca todos os artigos da documentação do Starlight
    const docs = await getCollection('docs');

    // Filtra rascunhos (se houver) e ordena por caminho/idioma
    const publishedDocs = docs
        .filter((doc) => !doc.data.draft)
        .sort((a, b) => a.id.localeCompare(b.id));

    let content = `# Monsta Docs\n\n`;
    content += `> Documentação técnica oficial, manuais de usuário, guias de instalação e resolução de problemas do sistema de monitoramento Monsta.\n\n`;

    // Agrupamento simples por idioma com base na pasta raiz (pt-br, en, es)
    const languages: Record<string, typeof publishedDocs> = {
        'pt-br': [],
        en: [],
        es: [],
        outros: [],
    };

    for (const doc of publishedDocs) {
        if (doc.id.startsWith('pt-br/')) languages['pt-br'].push(doc);
        else if (doc.id.startsWith('en/')) languages['en'].push(doc);
        else if (doc.id.startsWith('es/')) languages['es'].push(doc);
        else languages['outros'].push(doc);
    }

    const formatSection = (title: string, items: typeof publishedDocs) => {
        if (items.length === 0) return '';
        let section = `## ${title}\n\n`;
        for (const item of items) {
            // Remove a extensão do arquivo (.md/.mdx) e ajusta barras para formar a URL limpa
            const slug = item.slug || item.id.replace(/\.(md|mdx)$/, '');
            const url = new URL(slug.endsWith('/') ? slug : `${slug}/`, site).href;
            const desc = item.data.description ? `: ${item.data.description}` : '';

            section += `- [${item.data.title}](${url})${desc}\n`;
        }
        return section + '\n';
    };

    content += formatSection('Documentação em Português (PT-BR)', languages['pt-br']);
    content += formatSection('English Documentation (EN)', languages['en']);
    content += formatSection('Documentación en Español (ES)', languages['es']);

    return new Response(content, {
        headers: {
            'Content-Type': 'text/plain; charset=utf-8',
        },
    });
};