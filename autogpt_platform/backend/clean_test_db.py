#!/usr/bin/env python3

"""
limpa o banco de dados de teste removendo todos os dados e preservando o schema.

uso:
    poetry run python clean_test_db.py [--yes]
opções:
    -- yes    pula o prompt de confirmação
"""

import asyncio
import sys

from prisma import Prisma

async def main():
    db = Prisma()

    await db.connect()

    print("=" * 60)
    print("limpando banco de dados de teste")
    print("=" * 60)
    print()

    # obtém as contagens iniciais
    user_count = await db.user.count()
    agent_count = await db.agentgraph.count()

    print(f"dado atual: {user_count} usuários, {agent_count} gráficos de agente")

    if user_count == 0 and agent_count == 0:
        print("banco de dados já está limpo")

        await db.disconnect()

        return
    
    # checa pela flag --yes
    skip_confirm = "--yes" in sys.argv

    if not skip_confirm:
        response = input("\nvocê deseja limpar todos os dados? (yes/no): ")

        if response.lower() != "yes":
            print("abortado...")

            await db.disconnect()

            return
        
    print("\nlimpando banco de dados...")

    # deleta na ordem reversa ao das dependências
    tables = [
        ("UserNotificationBatch", db.usernotificationbatch),
        ("NotificationEvent", db.notificationevent),
        ("CreditRefundRequest", db.creditrefundrequest),
        ("StoreListingReview", db.storelistingreview),
        ("StoreListingVersion", db.storelistingversion),
        ("StoreListing", db.storelisting),
        ("AgentNodeExecutionInputOutput", db.agentnodeexecutioninputoutput),
        ("AgentNodeExecution", db.agentnodeexecution),
        ("AgentGraphExecution", db.agentgraphexecution),
        ("AgentNodeLink", db.agentnodelink),
        ("LibraryAgent", db.libraryagent),
        ("AgentPreset", db.agentpreset),
        ("IntegrationWebhook", db.integrationwebhook),
        ("AgentNode", db.agentnode),
        ("AgentGraph", db.agentgraph),
        ("AgentBlock", db.agentblock),
        ("APIKey", db.apikey),
        ("CreditTransaction", db.credittransaction),
        ("AnalyticsMetrics", db.analyticsmetrics),
        ("AnalyticsDetails", db.analyticsdetails),
        ("Profile", db.profile),
        ("UserOnboarding", db.useronboarding),
        ("User", db.user)
    ]

    for table_name, table in tables:
        try:
            count = await table.count()

            if count > 0:
                await table.delete_many()

                print(f"[✓] {count} records deletados de {table_name}")
        except Exception as e:
            print(f"[⚠] erro ao limpar {table_name}: {e}")

    # atualiza as visualizações materializadas (elas devem estar vazias agora)
    try:
        await db.execute_raw("SELECT refresh_store_materialized_views();")

        print("\n[✓] visualizações materializadas atualizadas")
    except Exception as e:
        print(f"\n[⚠] não foi possível atualizar as visualizações materializadas: {e}")

    await db.disconnect()

    print("\n" + "=" * 60)
    print("banco de dados limpo com sucesso")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())