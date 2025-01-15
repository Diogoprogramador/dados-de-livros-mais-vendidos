
# Análise dos Livros Mais Vendidos do New York Times - 2024

Este repositório contém um script Python que extrai dados sobre os livros mais vendidos de 2024 listados no New York Times, publicados na Wikipédia. O script coleta informações sobre os títulos dos livros e seus respectivos autores, e gera gráficos de barras mostrando a distribuição percentual de livros por autor e títulos mais vendidos.

## Funcionalidades

- Extrai dados diretamente da Wikipédia sobre os livros mais vendidos do New York Times em 2024.
- Cria dois gráficos:
  - Distribuição percentual de livros mais vendidos por autor.
  - Distribuição percentual de títulos mais vendidos.

## Requisitos

Para executar este script, você precisa ter as seguintes bibliotecas Python instaladas:

- `requests`
- `beautifulsoup4`
- `pandas`
- `matplotlib`
- `seaborn`

Você pode instalar as dependências necessárias executando o seguinte comando:

```bash
pip install requests beautifulsoup4 pandas matplotlib seaborn
Como Usar
Clone este repositório para o seu computador:

bash
Copiar código
git clone https://github.com/seu-usuario/ny_times_best_sellers_2024.git
Navegue até o diretório do repositório:

bash
Copiar código
cd ny_times_best_sellers_2024
Execute o script Python:

bash
Copiar código
python ny_times_best_sellers_2024.py
O script irá extrair os dados diretamente da página da Wikipédia sobre os livros mais vendidos de 2024 e gerar dois gráficos:

Um gráfico de barras mostrando a porcentagem de livros mais vendidos por autor.
Um gráfico de barras mostrando a porcentagem de vezes que cada livro foi número 1 na lista.
Exemplo de Saída
Após a execução do script, você verá os seguintes gráficos:

Porcentagem de Livros Mais Vendidos por Autor: Mostra a distribuição percentual de livros mais vendidos de 2024 por autor.
Porcentagem de Livros Mais Vendidos: Mostra a distribuição percentual de títulos de livros mais vendidos, com a frequência de cada um sendo número 1.
