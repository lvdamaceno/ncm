import pandas as pd
from pathlib import Path
from functions import add_zeros, save_treated_df

# Criar um data frame com a tabela em tsv, não soube como tratar as vírgulas dentro das colunas do csv
df = pd.read_csv('sheet_files/NCM_original.tsv', sep='\t', dtype={
    'Codigo': str,
    'Descricao': str,
    'Categoria': str,
    'Data Início': str,
    'Data Fim': str
})

# Transforma as descricões em Upper Case
df['Descricao'] = df['Descricao'].str.upper()
# Transforma as categorias em Upper Case
df['Categoria'] = df['Categoria'].str.upper()

# Transforma a coluna de códigos para que todos tenham um total de 8 dígitos, preenchendo os vazios com 0
# Exemplo, '01' vira '01000000
df_with_zeros = add_zeros(df, 'Codigo')

# Cria níveis de hierarquia N1 até N7
df_with_zeros['Grau'] = df_with_zeros['Codigo'].map(
    lambda n: 'N1' if len(n) - len(n.rstrip('0')) == 6 else
    'N2' if len(n) - len(n.rstrip('0')) == 5 else
    'N3' if len(n) - len(n.rstrip('0')) == 4 else
    'N4' if len(n) - len(n.rstrip('0')) == 3 else
    'N5' if len(n) - len(n.rstrip('0')) == 2 else
    'N6' if len(n) - len(n.rstrip('0')) == 1 else 'N7'
)

# Reorganiza as colunas do Data Frame
df_with_hierarchy = df_with_zeros.reindex(
    columns=['Grau', 'Codigo', 'Descricao', 'Categoria', 'Data Início', 'Data Fim'])

save_treated_df(df_with_hierarchy, 'NCM_hierarquias.tsv')

#TODO - Descobrir como inserir nos níveis N5 a descrição do grupo