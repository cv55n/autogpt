import { withSentryConfig } from "@sentry/nextjs";

/** @type {import('next').NextConfig} */
const nextConfig = {
    images: {
        domains: [
            "images.unsplash.com",
            "ddz4ak4pa3d19.cloudfront.net",
            "upload.wikimedia.org",
            "storage.googleapis.com",

            "ideogram.ai", // para imagens geradas
            "picsum.photos" // para imagens de espaço reservado
        ]
    },

    output: "standalone",

    transpilePackages: ["geist"]
};

const isDevelopmentBuild = process.env.NODE_ENV !== "production";

export default isDevelopmentBuild
    ? nextConfig
    : withSentryConfig(nextConfig, {
        // para todas as opções disponíveis, veja:
        // https://github.com/getsentry/sentry-webpack-plugin#options

        org: "cv55n",
        project: "builder",

        // expor env do vercel no cliente
        env: {
            NEXT_PUBLIC_VERCEL_ENV: process.env.VERCEL_ENV
        },

        // printa somente logs para upload de mapas de origem no ci
        silent: !process.env.CI,

        // para todas as opções disponíveis, veja:
        // https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/

        // carrega um conjunto maior de mapas de origem para obter rastreamentos de pilha mais bonitos (aumenta o tempo de build)
        widenClientFileUpload: true,

        // anota automaticamente os componentes do react para mostrar seus nomes completos em trilhas de navegação e reprodução de sessão
        reactComponentAnnotation: {
            enabled: true
        },

        // encaminha solicitações do navegador para o sentry por meio de uma reescrita do next.js para contornar adblockers
        tunnelRoute: "/store",

        // não há necessidade de ocultar mapas de origem dos pacotes de clientes gerados, pois a origem é pública de qualquer maneira
        hideSourceMaps: false,

        // agita automaticamente as instruções do registrador sentry para reduzir o tamanho do pacote
        disableLogger: true,

        // habilita a instrumentação automática dos monitores vercel cron
        //
        // veja os links abaixo para mais informações:
        //
        // https://docs.sentry.io/product/crons/
        // https://vercel.com/docs/cron-jobs
        automaticVercelMonitors: true,

        async headers() {
            return [
                {
                    source: "/:path*",

                    headers: [
                        {
                            key: "Document-Policy",
                            value: "js-profiling"
                        }
                    ]
                }
            ];
        }
    });