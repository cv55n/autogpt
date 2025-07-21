# autogpt classic

foi um projeto experimental para demonstrar a operação autônoma do gpt-4. ele foi projetado para fazer o gpt-4 operar de forma independente e encadear tarefas para atingir objetivos mais complexos.

## status do projeto

**esse projeto não possui suporte e as dependências não serão atualizadas. foi um experimento que concluiu sua fase inicial de pesquisa. se você deseja utilizar o autogpt, deve usar a [plataforma autogpt](https://github.com/cv55n/autogpt/tree/master/autogpt_platform).**

para aqueles interessados em agentes de ia autônomos, recomendamos explorar alternativas mais ativamente mantidas ou consultar esta base de código apenas para fins educacionais.

## overview

o autogpt classic foi uma das primeiras implementações de agentes de ia autônomos - sistemas de ia que podem, de forma independente:

- dividir objetivos complexos em tarefas menores
- executar essas tarefas usando ferramentas e apis disponíveis
- aprender com os resultados e ajuste sua abordagem
- encadear várias ações para atingir um objetivo

## features

- 🔄 encadeamento autônomo de tarefas
- 🛠 capacidades de integração de ferramentas e api
- 💾 gerenciamento de memória para retenção de contexto
- 🔍 navegação na web e coleta de informações
- 📝 operações de arquivo e criação de conteúdo
- 🔄 auto-sugestão e divisão de tarefas

## estrutura

o projeto está organizado em vários componentes principais:

- `/benchmark` - ferramentas de teste de desempenho
- `/forge` - estrutura central de agente autônomo
- `/frontend` - componentes da interface de usuário
- `/original_autogpt` - implementação original
