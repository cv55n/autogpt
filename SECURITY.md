# política de segurança

## reportando problemas de segurança

levamos a segurança do nosso projeto a sério. se você acredita ter encontrado uma vulnerabilidade de segurança, informe-nos em particular. **não relate vulnerabilidades de segurança por meio de problemas públicos, discussões ou solicitações de pull no github.**

> **nota importante**: qualquer código dentro da pasta `classic/` é considerado legado, sem suporte e fora do escopo de relatórios de segurança. não abordaremos vulnerabilidades de segurança neste código obsoleto.

em vez disso, por favor reporte via:

- [github security advisory](https://github.com/cv55n/autogpt/security/advisories/new)

### processo de report

1. **envio de report**: utiliza um dos canais acima para enviar seu relatório
2. **tempo de resposta**: nossa equipe acusará o recebimento do seu relatório em até 14 dias úteis.
3. **colaboração**: colaboraremos com você para entender e validar o problema
4. **resolução**: trabalharemos em uma correção e coordenaremos o processo de lançamento

### política de divulgação

- por favor, forneça relatórios detalhados com etapas reproduzíveis
- inclua o hash da versão/commit onde você descobriu a vulnerabilidade
- permita-nos uma janela de correção de segurança de 90 dias antes de qualquer divulgação pública
- após o lançamento do patch, aguarde 30 dias para que os usuários atualizem antes da divulgação pública (para um total máximo de 120 dias entre o momento da atualização e o momento da correção)
- compartilhe quaisquer possíveis mitigações ou soluções alternativas, se conhecidas

## versões suportadas

somente as seguintes versões são elegíveis para atualizações de segurança:

| versão | suportado |
|--------|-----------|
| último lançamento no branch master | ✅ |
| commits de desenvolvimento (pre-master) | ✅ |
| pasta clássica (deprecated) | ❌ |
| todas as outras versões | ❌ |

## melhores práticas de segurança

ao utilizar esse projeto:

1. use sempre a versão estável mais recente
2. revise os avisos de segurança antes de atualizar
3. siga nossa documentação e diretrizes de segurança
4. mantenha suas dependências atualizadas
5. não use código da pasta `classic/` pois ele está obsoleto e não é suportado

## avisos de segurança anteriores

para obter uma lista de avisos de segurança anteriores, visite nossa [página de avisos de segurança](https://github.com/cv55n/autogpt/security/advisories) e a [página de divulgações da huntr](https://huntr.com/repos/cv55n/autogpt).

---

última atualização: julho de 2025
