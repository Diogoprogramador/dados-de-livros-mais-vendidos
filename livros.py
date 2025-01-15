import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para extrair dados da tabela da Wikipédia
def extrair_dados_da_tabela(url):
    # Fazer a requisição HTTP
    response = requests.get(url)

    # Fazer o parsing do HTML com BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar a tabela que contém os dados (geralmente com a classe 'wikitable')
    tabela = soup.find('table', {'class': 'wikitable'})

    # Extrair as linhas da tabela
    linhas = tabela.find_all('tr')

    # Listas para armazenar os dados
    livros = []
    autores = []

    # Loop para extrair dados de cada linha (começando do índice 1, pois a primeira linha são os cabeçalhos)
    for linha in linhas[1:]:
        colunas = linha.find_all('td')  # As células da tabela
        if len(colunas) > 0:  # Se a linha contiver colunas
            try:
                # Extrair título do livro (primeira coluna)
                titulo_livro = colunas[0].get_text(strip=True)

                # Extrair nome do autor (segunda coluna)
                nome_autor = colunas[1].get_text(strip=True)

                # Adicionar os dados às listas
                livros.append(titulo_livro)
                autores.append(nome_autor)
            except IndexError:
                continue  # Caso algum livro ou autor esteja ausente, continuar para o próximo

    return livros, autores

# Função para calcular as porcentagens
def calcular_porcentagens(df, coluna):
    total = len(df)  # Total de livros/entradas
    porcentagens = df[coluna].value_counts(normalize=True) * 100
    return porcentagens

# Função para gerar gráficos
def gerar_grafico_porcentagem(df, coluna, title, xlabel, ylabel):
    # Calcular as porcentagens
    porcentagens = calcular_porcentagens(df, coluna)

    # Configuração do gráfico
    plt.figure(figsize=(14, 7))
    ax = sns.barplot(x=porcentagens.index, y=porcentagens.values, palette="Set2")
    plt.xticks(rotation=90)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Adicionar porcentagens acima das barras
    for p in ax.patches:
        percentage = p.get_height()
        # Formatar a porcentagem com 0 ou 1 casa decimal
        ax.annotate(f'{percentage:.0f}%',  # Aqui definimos para 0 casas decimais
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center',
                    fontsize=12, color='black',
                    xytext=(0, 9), textcoords='offset points')

    plt.tight_layout()
    plt.show()

# URL da página da Wikipédia
url = "https://en.wikipedia.org/wiki/List_of_The_New_York_Times_number-one_books_of_2024"

# Extraindo os dados da tabela
livros, autores = extrair_dados_da_tabela(url)

# Criar um DataFrame com os dados extraídos
df = pd.DataFrame({
    'Livro': livros,
    'Autor': autores
})

# Exibir os primeiros dados extraídos
print(df.head())

# GERANDO GRÁFICOS

# Gráfico de porcentagens por autor
gerar_grafico_porcentagem(df, 'Autor', 'Porcentagem de Livros Mais Vendidos por Autor em 2024', 'Autor', 'Porcentagem de Livros')

# Gráfico de porcentagens por título de livro
gerar_grafico_porcentagem(df, 'Livro', 'Porcentagem de Livros Mais Vendidos em 2024', 'Livro', 'Porcentagem de Vezes em que foi Nº1')
