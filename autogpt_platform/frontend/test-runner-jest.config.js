const { getJestConfig } = require("@storybook/test-runner");

// a configuração padrão do jest vem de @storybook/test-runner
const testRunnerConfig = getJestConfig();

/**
 * @type {import('@jest/types').Config.InitialOptions}
 */
module.exports = {
    ...testRunnerConfig,

    /**
     * adicionar seu próprio substitui abaixo, certifique-se
     * de levar as propriedades de testrunnerconfig no seu
     * 
     * @see https://jestjs.io/docs/configuration
     */
    testPathIgnorePatterns: [
        "/node_modules/",
        "/supabase/"
    ]
};