import pandas as pd
from pathlib import Path    
from mcp.server.fastmcp import MCP

mcp = FastMCP('search_book')

biblioteca = Path(__file__).parent / 'GoodReads_100k_books.csv'
def search_book(gender, size, ):
    list_filtered = []
    
    gender_filtered = biblioteca.get(gender)
    
    if gender_filtered:
        for item in gender_filtered:
            if item.size <= size:
                list_filtered.append(item)           
    print(f'''Foram encontrados {len(list_filtered)} livros do gênero {gender} com até {size} páginas''')
    return list_filtered

@mcp.tool() #decoramos a função para que o agente use como uma ferramenta
def search_book_oficina(gender: str, size: int, csv_path = biblioteca) -> pd.DataFrame:
    
    '''inserir uma descrição do que a função faz, os params que recebe e os tipos, o retorno'''
    
    libre = pd.read_csv(biblioteca, encoding= 'utf-8') #usa o pandas para ler o arquivo csv
    
    libre['pages'] = libre['pages'].astype(int) #define os tipos para que não seja diferente das colunas
    libre['raiting'] = libre['raiting'].astype(float)
    
    list_filtered = libre[(
        libre['genre'].str.contains(gender, case= False)) and #vai na coluna gênero e vê se contem o nome
        ((size-20) < libre['pages']) and # filtra 20 paginas a baixo e acima da quantidade escolhida
        ((size+20) < libre['pages'])
    ]
    
    if len(libre) > 100:
        for_stars = libre[libre['rating'] > 4]
        if len(for_stars) > 0:
            list_filtered = for_stars
        
    list_filtered = list_filtered.sort_values(by='rating', ascending=False)
    result = list_filtered[['title', 'author', 'pages', 'genre', 'rating', 'desc']].head(10).to_dict(orient='records')
                        
    print(f'''Foram encontrados {len(list_filtered)} livros do gênero {gender} com até {size} páginas''')
    
    return list_filtered

@mcp.tool()
def search_of_name(title: str):
    libre = pd.read_csv(biblioteca, encoding='utf-8')
    
    book = libre[libre['name'].str.contains(title, case=False,)]
    
    return book

if __name__ == '__main__':
    # saida = search_book_oficina('romance', 100)
    # print(saida)
    mcp.run(transport='stdio') #stdio indica que a execução é local