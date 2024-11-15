# 📝 Projeto: Solução de BI
Um projeto feito para a disciplina de Tópicos Especiais em Banco de Dados.

Neste projeto, foi desenvolvida uma solução de Business Intelligence (BI) para análise de dados de atraso de voos ✈️, com base em uma base de dados rica em informações sobre distâncias de voo, atrasos, chegadas antecipadas, etc. A solução implementada permitiu identificar padrões e correlações entre as variáveis de voo, fornecendo insights estratégicos para a análise de desempenho e eficiência das operações aéreas.

Base de dados: <https://www.kaggle.com/datasets/usdot/flight-delays?ref=hackernoon.com>

## ⚙️ Passo-a-passo (abordagem ETL)
1. Foram definidos os gráficos e relatórios que seriam gerados a partir das bases de dados;
2. Mediante as variáveis presentes na base, foi definida a estrutura do modelo dimensional (Tabela de fato e tabelas de dimensão);
3. Análise exploratória dos dados utilizando o Pandas;
4. Tratamento dos dados, como remoção de valores nulos algumas colunas com muitos dados faltantes ou irrelevantes;
5. Criação das tabelas de dimensão e fato no data warehouse (MySQL Workbench);
6. Carga do data warehouse extraindo dados das bases “airlines_data”, “aiports_data” e “flights_data”;
7. Geração e análise de gráficos e relatórios no Power BI.

## 💡 Insight interessante 
<div align="center">
  <img src="https://github.com/user-attachments/assets/6c413a1d-1912-4ad0-b77e-b88f9c9f6f18" width="550">
  <p>
    A companhia aérea Hawaiian Airlines Inc. (HA), fez 112 voos (gráfico cartão) e não houve correlação entre a distância e os minutos atrasados na chegada (gráfico de dispersão). Dentre os voos feitos, 2 estavam entre 4001-5000 milhas de distância (gráfico de contagem de voos por distância) e os mesmos tiveram a média mais alta de atraso (gráfico de média de atrasos em minutos). Inferimos que, nesse caso, os voos com maior distância foram os que mais atrasaram e que os de menor distância, atrasaram bem pouco.
  </p>
</div>

## 💻 Tecnologias utilizadas
``VS Code`` | ``Python`` | ``Mysql Workbench`` | ``SQL Server`` | ``Power BI ``

⚠️ Para saber mais detalhes do projeto e ver mais alguns insights obtidos, acesse o arquivo "PASSOS".

