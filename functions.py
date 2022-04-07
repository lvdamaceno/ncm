from pathlib import Path


def add_zeros(df_without_zeros, column_name):
    # Função que adiciona 0 nos códigos para que fiquem em um padrão de 8 digitos
    df_without_zeros[column_name] = df_without_zeros[column_name].map(
        lambda n: n + ((8 - len(n)) * '0') if len(n) < 8 else n)
    return df_without_zeros


def save_treated_df(data_frame, name):
    # Função para salvar Data Sets com algum tratamento
    path_to_file = f'sheet_files/{name}'
    path = Path(path_to_file)
    if path.is_file():
        print('File exists')
    else:
        data_frame.to_csv('sheet_files/' + name, sep='\t', index=False)
