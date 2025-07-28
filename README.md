# autogpt: crie, implemente e execute agentes de ia

uma plataforma poderosa que permite criar, implantar e gerenciar agentes de ia contínuos que automatizam fluxos de trabalho complexos.

## opções de hospedagem

- baixar e auto-hospedar
- [entrar na waitlist](https://agpt.co/waitlist) para o beta da hospedagem em nuvem

## como configurar e auto-hospedar

> [!note]
> configurar e hospedar a plataforma autogpt por conta própria é um processo técnico.
> se preferir algo que simplesmente funcione, recomendamos entrar na lista de espera para o beta hospedado na nuvem.

### requisitos de sistema

antes de prosseguir com a instalação, certifique-se de que seu sistema atende aos seguintes requisitos:

#### requisitos de hardware

- cpu: 4+ cores recomendado
- ram: mínimo 8gb; 16gb recomendado
- armazenamento: pelo menos 10gb de espaço livre

#### requisitos de software

- sistemas operacionais:
    - linux (ubuntu 20.04 ou mais recente recomendado)
    - macos (10.15 ou mais recente)
    - windows 10/11 com wsl2
- software necessário (com versões mínimas):
    - docker engine (20.10.0 ou mais recente)
    - docker compose (2.0.0 ou mais recente)
    - git (2.30 ou mais recente)
    - node.js (16.x ou mais recente)
    - npm (8.x ou mais recente)
    - vscode (1.60 ou mais recente) ou qualquer outro editor de código moderno

#### requisitos de rede

- conexão de internet estável
- acesso às portas necessárias (será configurado no docker)
- capacidade de fazer conexões https de saída

### instruções de setup atualizadas

mudamos para um site de documentação totalmente mantido e atualizado regularmente.

👉 [siga o guia de auto-hospedagem oficial aqui](https://docs.agpt.co/platform/getting-started/)

este tutorial pressupõe que você tenha o docker, o vscode, o git e o npm instalados.

##### ⚡ configuração rápida com script de uma linha (recomendado para hospedagem local)

pule as etapas manuais e comece em minutos usando nosso script de configuração automática.

para macos/linux:

```
curl -fsSL https://setup.agpt.co/install.sh -o install.sh && bash install.sh
```

para windows (powershell):

```
powershell -c "iwr https://setup.agpt.co/install.bat -o install.bat; ./install.bat"
```

isso instalará dependências, configurará o docker e iniciará sua instância local — tudo de uma vez.

### 🧱 interface autogpt

o frontend do autogpt é onde os usuários interagem com nossa poderosa plataforma de automação de ia. ele oferece diversas maneiras de interagir e aproveitar nossos agentes de ia. esta é a interface onde você dará vida às suas ideias de automação de ia:

**builder de agente**: para aqueles que desejam personalizar, nossa interface intuitiva e de baixo código permite que você projete e configure seus próprios agentes de ia.

**gerenciamento de workflow**: crie, modifique e otimize seus fluxos de trabalho de automação com facilidade. Você cria seu agente conectando blocos, onde cada bloco executa uma única ação.

**controles de deployment**: gerencie o ciclo de vida dos seus agentes, do teste à produção.

**agentes prontos para uso**: não quer construir? basta selecionar um agente da nossa biblioteca de agentes pré-configurados e colocá-los para trabalhar imediatamente.

**interação de agente**: não importa se você criou seus próprios agentes ou se está usando agentes pré-configurados: execute-os e interaja com eles facilmente por meio de nossa interface amigável.

**monitoramento e análise**: acompanhe o desempenho dos seus agentes e obtenha insights para melhorar continuamente seus processos de automação.

[leia esse guia](https://docs.agpt.co/platform/new_blocks/) para aprender a construir seus próprios blocos personalizados.

### 💽 servidor do autogpt

o servidor autogpt é a força motriz da nossa plataforma. é aqui que seus agentes são executados. uma vez implantados, os agentes podem ser acionados por fontes externas e operar continuamente. ele contém todos os componentes essenciais para o funcionamento perfeito do autogpt.

**código-fonte**: a lógica central que impulsiona nossos agentes e processos de automação.

**infraestrutura**: sistemas robustos que garantem desempenho confiável e escalável.

**mercado**: um mercado abrangente onde você pode encontrar e implementar uma ampla variedade de agentes pré-criados.

### 🐙 agentes de exemplo

aqui estão dois exemplos do que você pode fazer com o autogpt:

1. **crie vídeos virais a partir de tópicos populares**
    - esse agente lê tópicos no reddit.
    - ele identifica tópicos de tendência.
    - e então cria automaticamente um vídeo curto com base no conteúdo.

2. **identifique as melhores citações de vídeos para mídias sociais**
    - esse agente se inscreve no seu canal do youtube.
    - quando você posta um novo vídeo, ele é transcrevido.
    - ele usa ia para identificar as citações mais impactantes para gerar um resumo.
    - depois, ele escreve uma postagem para publicar automaticamente nas suas redes sociais.

esses exemplos mostram apenas uma pequena amostra do que você pode alcançar com o autogpt. você pode criar fluxos de trabalho personalizados para criar agentes para qualquer caso de uso.

### missão e licenciamento

nossa missão é fornecer ferramentas para que você possa se concentrar no que importa:

- **🏗️ construindo** - estabelecer a base para algo incrível.
- **🧪 testando** - ajustar seu agente até a perfeição.
- **🤝 delegando** - deixar a ia trabalhar para você e dar vida às suas ideias.

faça parte disso tudo, o autogpt veio para ficar, na vanguarda da inovação em ia.

📖 [documentação](https://docs.agpt.co/) | 🚀 [contribuindo](https://github.com/cv55n/autogpt/blob/master/CONTRIBUTING.md)

##### licenciamento:

licença mit: a maior parte do repositório autogpt está sob a licença mit.

licença polyform shield: essa licença se aplica à pasta `autogpt_platform`.

para mais informações, veja https://agpt.co/blog/introducing-the-autogpt-platform
