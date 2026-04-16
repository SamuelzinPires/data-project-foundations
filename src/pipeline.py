import pandas as pd

def extract(file_path: str) -> pd.DataFrame:
    """Extrai os dados de um arquivo CSV."""
    dados= pd.read_csv(file_path)
    return dados

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica as transformações necessárias nos dados."""
    df.columns = df.columns.str.lower()
    df = df.dropna()
    return df

def load(df: pd.DataFrame, output_path: str) -> None:
    """Carrega os dados transformados para o destino."""
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    print("Iniciando a esteira de dados...")
    
    # 1. Extrair
    print("Extraindo...")
    df_bruto = extract("data/input/dados_brutos.csv")
    
    # 2. Transformar
    print("Transformando...")
    df_limpo = transform(df_bruto)
    
    # 3. Carregar
    print("Salvando...")
    load(df_limpo, "data/output/dados_limpos.csv")
    
    print("Sucesso! Verifique a pasta data/output")