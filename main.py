import os
import asyncio
from dotenv import load_dotenv
from agent_framework.azure import AzureOpenAIResponsesClient
from azure.identity import AzureCliCredential

load_dotenv()
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")


async def main():
    agent = AzureOpenAIResponsesClient(
        endpoint = AZURE_OPENAI_ENDPOINT,
        api_key = AZURE_OPENAI_API_KEY,
        deployment_name = AZURE_OPENAI_DEPLOYMENT
        
    ).create_agent(
        name="CF_Hackathon_Agent",
        instructions="You are an expert assistant for hackathon projects.",
    )
    print(await agent.run("Give me assistance for a hackathon Civic Agent project."))
    
if __name__ == "__main__":
    asyncio.run(main())