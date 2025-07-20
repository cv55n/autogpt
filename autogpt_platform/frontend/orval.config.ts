import { defineConfig } from "orval";

export default defineConfig({
    autogpt_api_client: {
        input: {
            target: `./src/app/api/openapi.json`,

            override: {
                transformer: "./src/app/api/transformers/fix-tags.mjs"
            }
        },

        output: {
            workspace: "./src/app/api",

            target: `./__generated__/endpoints`,
            schemas: "./__generated__/models",

            mode: "tags-split",
            client: "react-query",
            httpClient: "fetch",

            indexFiles: false,

            override: {
                mutator: {
                    path: "./mutators/custom-mutator.ts",
                    name: "customMutator"
                },

                query: {
                    useQuery: true,
                    useMutation: true,

                    // adicionará mais conforme os casos de uso surgirem
                },

                operations: {
                    "agentes da biblioteca getv2list": {
                        query: {
                            useInfinite: true,
                            useInfiniteQueryParam: "page"
                        }
                    }
                }
            }
        },

        hooks: {
            afterAllFilesWrite: "prettier --write"
        }
    }
});