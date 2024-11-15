import pandas as pd
from ydata_profiling import ProfileReport

df_flights = pd.read_csv('./data-bases/flights.csv')
print(df_flights.head())

flights_profile = ProfileReport(df_flights)
flights_profile.to_file('pandas-flights.html')

# Removendo colunas com mais de 80% de dados faltantes
df_cleaned = df_flights.drop(columns=['AIR_SYSTEM_DELAY', 'SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY', 'CANCELLATION_REASON'])
#print(df_cleaned.head)

# Removendo colunas irrelevantes para a análise
df_cleaned_final = df_cleaned.drop(columns=['YEAR', 'FLIGHT_NUMBER', 'TAIL_NUMBER', 'TAXI_OUT', 'TAXI_IN', 'WHEELS_OFF', 'WHEELS_ON', 'DIVERTED', 'CANCELLED'])
print(df_cleaned_final.head)

# Removendo linhas com valores nulos
df_cleaned_final.dropna(inplace=True)

output_file_path = './data-bases/final_dataframe.csv'

# Salvar a nova base de dados em um arquivo CSV
df_cleaned_final.to_csv(output_file_path, index=False)


