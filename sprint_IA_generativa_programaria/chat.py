from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import asyncio
import openai
from langchain_openai.chat_models import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

search_path = Path(__file__).parent / 'recomendador_de_livros_com_IA.py'

client = MultiServerMCPClient(
    {
        'search_book_oficina': {
            'command': 'python',
            'args': [str(search_path)],
            'transport': 'stdio'
        },
        "apify": {
            "transport": "sse",
            "url": "https://mcp.apify.com/sse?actors=runtime/goodreads-book-scraper",
            "headers": {
                "Authorization": f"Bearer {os.getenv('APIFY_API_KEY')}",
            }
        }
    }
)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

async def chat():
    llm = ChatOpenAI(name ='o4-mini', top_p = 0.5, api_key=openai.api_key)
    tools = await client.get_tools()
    agent = create_react_agent(
        model=llm, 
        tools=tools, 
        checkpointer=InMemorySaver(), #memoria do agente
        prompt = "Você é um agente que ajuda usuários a encontrar livros com base em suas solicitações. " \
        "Você pode usar tools para buscar informações sobre livros. Lembre-se de traduzir o gênero do livro para o inglês antes de fazer a busca na tool." \
        "Considere livros curtos os livros que tem no máximo 130 páginas." \
        "Considere livros longos os livros que tem mais de 400 páginas." \
        "Na hora de responder escolha os 10 melhores livros baseados nas avaliações dos usuários."  \
        "Para encontrar informações de um livro específico, passe o nome em inglês, do jeito que o usuário escreveu e com codificação UTF-8 para a tool de buscar por nome." \
        "Se o usuário pesquisar livros com algum termo específico, use a ferramenta do goodreads-book-scraper do apify e passe o search term em inglês." 
    )
    
    print('Qual seu pedido?')
    
  
    while True:
        user_input = input('>> ')
        
        if user_input.lower() == '/q':
            print('Saindo...')
            break
        
        config ={ 
            "configurable": {
                "thread_id":"1"
            }
        }
        
        response = await agent.ainvoke(
            {
                "messages": [{'role': 'user', 'content': user_input}]
            }, 
            config = config
        ),
        
        print('Resposta do agente: \n')
        print(response['menssages'][-1].content)
        
        # async for chunk in agent.astream(
        #                 {"messages": user_input},
        #                 stream_mode=["messages", "custom"],
        #                 config=config,
        #             ):
        #     print(chunk) # o astream serve para ver o que cada chamada retorna
           
    
if __name__ == '__main__':
    print('geice')