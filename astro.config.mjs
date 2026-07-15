// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightImageZoom from 'starlight-image-zoom';
import path from 'node:path';

function remarkFixPagesCMSImages() {
	return function (tree, file) {
		function walk(node) {
			if (!node) return;

			// Se encontrar uma imagem e o link começar com /src/assets/images/...
			if (node.type === 'image' && node.url && node.url.startsWith('/src/assets/images/')) {
				// Descobre em qual pasta o arquivo .md atual está (ex: pt-br/start)
				const mdFilePath = file.history ? file.history[0] : file.path;

				if (mdFilePath) {
					const mdDir = path.dirname(mdFilePath);
					const projectRoot = process.cwd();

					// Junta o caminho raiz do projeto com o da imagem
					const imgAbs = path.join(projectRoot, node.url);

					// Calcula matematicamente os "../../../" necessários
					let relUrl = path.relative(mdDir, imgAbs).replace(/\\/g, '/');

					// Garante que o caminho relativo tenha a formatação correta
					node.url = relUrl.startsWith('.') ? relUrl : './' + relUrl;
				}
			}
			// Continua varrendo os outros elementos do texto
			if (node.children) node.children.forEach(walk);
		}
		walk(tree);
	};
}

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'Monsta Docs',
			logo: {
				src: './src/assets/logo/monsta-logo.png',
				alt: 'Monsta Logo',
			},
			defaultLocale: 'pt-br',
			locales: {
				en: { label: 'English', lang: 'en' },
				es: { label: 'Español', lang: 'es' },
				'pt-br': { label: 'Português', lang: 'pt-BR' },
			},
			customCss: ['./src/styles/custom.css'],
			favicon: '/favicon.png',
			plugins: [
				starlightImageZoom()
			],
			sidebar: [
				{
					label: 'Início',
					translations: {
						en: 'Home',
						es: 'Inicio'
					},
					link: '/',
				},
				{
					label: 'Primeiros Passos',
					collapsed: true,
					translations: { en: 'Getting Started', es: 'Primeros Pasos' },
					items: [
						{
							label: 'Conceitos Iniciais',
							collapsed: true,
							translations: { en: 'Initial Concepts', es: 'Conceptos Iniciales' },
							items: [{ autogenerate: { directory: 'start/conceitos-iniciais' } }]
						},
						{
							label: 'Assinatura e Licença Trial',
							collapsed: true,
							translations: { en: 'Subscription and Trial License', es: 'Suscripción y Licencia de Prueba' },
							items: [{ autogenerate: { directory: 'start/licenca-assinatura' } }]
						},
						{
							label: 'Instalação',
							collapsed: true,
							translations: { en: 'Installation', es: 'Instalación' },
							items: [{ autogenerate: { directory: 'start/instalacao' } }]
						},
						{
							label: 'Migração de Servidor',
							collapsed: true,
							translations: { en: 'Migration of Server', es: 'Migración de Servidor' },
							items: [{ autogenerate: { directory: 'start/migracao' } }]
						}
					],
				},
				{
					label: 'Manual do Usuário',
					collapsed: true,
					translations: { en: 'User Manual', es: 'Manual de Usuario' },
					items: [
						{
							label: 'Introdução ao Manual',
							translations: {
								en: 'Introduction to the Manual',
								es: 'Introducción al Manual'
							},
							link: '/manual/manual-usuario/', // O Starlight injeta o idioma automaticamente (/pt-br/, /en/, /es/)
						},
						{
							label: 'Barra Superior',
							collapsed: true,
							translations: { en: 'Top Bar', es: 'Barra Superior' },
							items: [{ autogenerate: { directory: 'manual/barra-superior' } }]
						},
						{
							label: 'Dispositivos',
							collapsed: true,
							translations: { en: 'Devices', es: 'Dispositivos' },
							items: [{ autogenerate: { directory: 'manual/dispositivos' } }]
						},
						{
							label: 'Painéis',
							collapsed: true,
							translations: { en: 'Dashboards', es: 'Paneles' },
							items: [{ autogenerate: { directory: 'manual/paineis' } }]
						},
						{
							label: 'Linha do Tempo',
							collapsed: true,
							translations: { en: 'Timeline', es: 'Línea de Tiempo' },
							items: [{ autogenerate: { directory: 'manual/linha-tempo' } }]
						},
						{
							label: 'Grupos de Alertas',
							collapsed: true,
							translations: { en: 'Alert Groups', es: 'Grupos de Alertas' },
							items: [{ autogenerate: { directory: 'manual/grupos-alertas' } }]
						},
						{
							label: 'Configurações',
							collapsed: true,
							translations: { en: 'Settings', es: 'Configuraciones' },
							items: [{ autogenerate: { directory: 'manual/configuracoes' } }]
						}
					],
				},
				{
					label: 'Documentação Técnica',
					collapsed: true,
					translations: { en: 'Technical Documentation', es: 'Documentación Técnica' },
					items: [
						{
							label: 'Datasheet do Monsta',
							translations: {
								en: 'Datasheet of Monsta',
								es: 'Datasheet de Monsta'
							},
							link: '/tech/datasheet/', // O Starlight injeta o idioma automaticamente (/pt-br/, /en/, /es/)
						},
						{
							label: 'Protocolos de Coleta',
							collapsed: true,
							translations: { en: 'Collection Protocols', es: 'Protocolos de Recolección' },
							items: [{ autogenerate: { directory: 'tech/protocolos-coleta' } }]
						},
						{
							label: 'Arquitetura e Comunicação',
							collapsed: true,
							translations: { en: 'Architecture and Communication', es: 'Arquitectura y Comunicación' },
							items: [{ autogenerate: { directory: 'tech/arquitetura-comunicacao' } }]
						},
						{
							label: 'Módulos de Script com Lua',
							collapsed: true,
							translations: { en: 'Script Modules with Lua', es: 'Módulos de Script con Lua' },
							items: [{ autogenerate: { directory: 'tech/modulos-script' } }]
						},
						{
							label: 'Guias Técnicos',
							collapsed: true,
							translations: { en: 'Technical Guides', es: 'Guías Técnicas' },
							items: [{ autogenerate: { directory: 'tech/guias-tecnicos' } }]
						},
						{
							label: 'Tutoriais do Monsta',
							collapsed: true,
							translations: { en: 'Monsta Tutorials', es: 'Tutoriales de Monsta' },
							items: [{ autogenerate: { directory: 'tech/tutoriais-monsta' } }]
						},
						{
							label: 'Changelog',
							collapsed: true,
							translations: { en: 'Changelog', es: 'Changelog' },
							items: [{ autogenerate: { directory: 'tech/changelog' } }]
						}
					],
				},
				{
					label: 'Dúvidas Comuns (FAQ)',
					collapsed: true,
					translations: { en: 'FAQ', es: 'Preguntas Frecuentes (FAQ)' },
					items: [
						{
							label: 'Conceitos Fundamentais',
							collapsed: true,
							translations: { en: 'Fundamental Concepts', es: 'Conceptos Fundamentales' },
							items: [{ autogenerate: { directory: 'faq/conceitos-fundamentais' } }]
						},
						{
							label: 'Contratação e Licenciamento',
							collapsed: true,
							translations: { en: 'Hiring and Licensing', es: 'Contratación y Licenciamiento' },
							items: [{ autogenerate: { directory: 'faq/contratacao-licenciamento' } }]
						},
						{
							label: 'Alertas e Notificações',
							collapsed: true,
							translations: { en: 'Alerts and Notifications', es: 'Alertas y Notificaciones' },
							items: [{ autogenerate: { directory: 'faq/alertas-notificacoes' } }]
						},
						{
							label: 'Problemas de Acesso',
							collapsed: true,
							translations: { en: 'Access Issues', es: 'Problemas de Acceso' },
							items: [{ autogenerate: { directory: 'faq/problemas-acesso' } }]
						},
						{
							label: 'Problemas de Coleta de Dados',
							collapsed: true,
							translations: { en: 'Data Collection Issues', es: 'Problemas de Recolección de Dados' },
							items: [{ autogenerate: { directory: 'faq/problemas-coleta' } }]
						},
						{
							label: 'Problemas de Licença',
							collapsed: true,
							translations: { en: 'License Issues', es: 'Problemas de Licencia' },
							items: [{ autogenerate: { directory: 'faq/problemas-licenca' } }]
						}
					],
				},
				{
					label: 'Guias Extras',
					collapsed: true,
					translations: { en: 'Extra Guides', es: 'Guías Adicionales' },
					items: [
						{
							label: 'Configuração de Equipamentos',
							collapsed: true,
							translations: { en: 'Equipment Configuration', es: 'Configuración de Equipos' },
							items: [{ autogenerate: { directory: 'extra/configuracao-equipamentos' } }]
						},
						{
							label: 'Linux',
							collapsed: true,
							translations: { en: 'Linux', es: 'Linux' },
							items: [{ autogenerate: { directory: 'extra/linux' } }]
						},
						{
							label: 'Windows',
							collapsed: true,
							translations: { en: 'Windows', es: 'Windows' },
							items: [{ autogenerate: { directory: 'extra/windows' } }]
						},
						{
							label: 'Hyper-V',
							collapsed: true,
							translations: { en: 'Hyper-V', es: 'Hyper-V' },
							items: [{ autogenerate: { directory: 'extra/hyper-v' } }]
						},
						{
							label: 'MikroTik',
							collapsed: true,
							translations: { en: 'MikroTik', es: 'MikroTik' },
							items: [{ autogenerate: { directory: 'extra/mikrotik' } }]
						}
					],
				}
			]
		}),
	],
	markdown: {
		remarkPlugins: [remarkFixPagesCMSImages],
	},
});