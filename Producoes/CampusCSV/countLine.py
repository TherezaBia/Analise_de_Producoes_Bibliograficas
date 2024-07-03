import pandas as pd
import os

# Diretório contendo os arquivos CSV
directory = 'C:/Users/there/OneDrive/Documentos/Producoes/Artigos por Campus'

# Dicionário para armazenar o número de linhas de cada arquivo
file_line_counts = {}

# Leitura de todos os arquivos CSV no diretório e contagem de linhas
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        try:
            df = pd.read_csv(file_path)
            line_count = len(df)
            file_line_counts[filename] = line_count
        except Exception as e:
            print(f"Erro ao ler o arquivo {filename}: {e}")

# Exibir a contagem de linhas para cada arquivo
for file, count in file_line_counts.items():
    print(f'{file}: {count} linhas')

# Armazenar os dados em um novo arquivo CSV
output_df = pd.DataFrame(list(file_line_counts.items()), columns=['Arquivo', 'Numero_de_Linhas'])
output_file_path = 'C:/Users/there/OneDrive/Documentos/Producoes/contagem_linhas.csv'
output_df.to_csv(output_file_path, index=False)

print(f'Dados armazenados em {output_file_path}')
