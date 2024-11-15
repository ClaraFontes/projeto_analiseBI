import pandas as pd

final_df = pd.read_csv('./data-bases/final-data.csv')
#print(final_df.head())

# Embaralhando as linhas da base de dados tratada
df_shuffled = final_df.sample(frac=1).reset_index(drop=True)
print(df_shuffled.head())

# Salvar a nova base de dados em um arquivo CSV
output_file_path = './data-bases/shuffled-data.csv'
df_shuffled.to_csv(output_file_path, index=False)

# Definindo arquivo a ser reduzido
df_flights = pd.read_csv('./data-bases/reduced-flights-data2.csv')

# Reduzindo em 20% (Foram feitas várias reduções até chegar ao valor satisfatório de linhas: 8.212)
reduced_data = df_flights.sample(frac=0.8, random_state=42)

# Salvando em novo arquivo csv
reduced_file_path = './data-bases/reduced-flights-data-final.csv'
reduced_data.to_csv(reduced_file_path, index=False)

reduced_file_path