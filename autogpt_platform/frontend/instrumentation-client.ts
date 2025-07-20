import * as Sentry from "@sentry/nextjs";

import { BehaveAs, getBehaveAs, getEnvironmentStr } from "@/lib/utils";

const isProductionCloud = process.env.NODE_ENV === "production" && getBehaveAs() === BehaveAs.CLOUD;

Sentry.init({
    dsn: "https://fe4e4aa4a283391808a5da396da20159@o4505260022104064.ingest.us.sentry.io/4507946746380288",

    environment: getEnvironmentStr(),

    enabled: isProductionCloud,

    // adiciona integrações opcionais para features adicionais
    integrations: [
        Sentry.replayIntegration(),
        Sentry.httpClientIntegration(),
        Sentry.replayCanvasIntegration(),
        Sentry.reportingObserverIntegration(),
        Sentry.browserProfilingIntegration()
    ],

    // define a probabilidade de os traços serem amostrados. ajuste
    // este valor na produção ou use tracesSampler para maior controle
    tracesSampleRate: 1,

    // define `tracepropagationtargets` para controlar para quais urls
    // a propagação de rastreamento deve ser habilitada
    tracePropagationTargets: [
        "localhost",
        "localhost:8006",

        /^https:\/\/dev\-builder\.agpt\.co\/api/,
        /^https:\/\/.*\.agpt\.co\/api/
    ],

    // define a probabilidade de eventos de repetição serem amostrados
    //
    // isso define a taxa de amostragem como 10%
    replaysSessionSampleRate: 0.1,

    // define a probabilidade de eventos de repetição serem amostrados
    // quando ocorre um erro
    replaysOnErrorSampleRate: 1.0,

    // definir esta opção como true imprimirá informações úteis no
    // console enquanto você configura o sentry
    debug: false,

    // defina profilessamplerate como 1.0 para criar um perfil de cada transação
    profilesSampleRate: 1.0,

    _experiments: {
        // habilita o envio de logs para o sentry
        enableLogs: true
    }
});

export const onRouterTransitionStart = Sentry.captureRouterTransitionStart;