import pytest
# test_pipeline.py

# importar a ferramenta que construímos na outra pasta
from src.pipeline import extract, transform, load

def test_extracao_dados():
    """Garante que a função extract consegue ler o arquivo e não retorna vazio."""
    
    #Definindo o caminho
    Dados = ("data/input/dados_brutos.csv")
    
    # Extrair os dados usando a função extract
    df = extract(Dados)
    
    # Mensagem de erro embutida para o caso de falha
    assert len(df) > 0
    print("Teste falhou: O DataFrame está vazio. Verifique o caminho do arquivo e o conteúdo.")

def test_transformacao_dados(mock_df_bruto):
    df_sujo = mock_df_bruto
    df_limpo = transform(df_sujo)
    assert len(df_limpo) == 3, "Teste falhou: A função transform não removeu os dados nulos."
    assert df_limpo is not None, "Teste falhou: A função transform retornou None."
    assert df_limpo.columns.str.lower().tolist() == ['nome', 'idade', 'cidade'], "Teste falhou: As colunas não foram padronizadas para minúsculas."

@pytest.mark.parametrize("no_folder", [ 
    "pasta_falsa/arquivo_null.csv",
    "diretorio_inexistente/dados.csv"
])
def test_extracao_arquivo_inexistente(no_folder):
    
    with pytest.raises(FileNotFoundError):
        extract(no_folder)

def test_load_dados(mock_df_bruto, tmp_path):

    saida = tmp_path/"saida_teste.csv"
    load(mock_df_bruto, saida)
    assert saida.exists(), "A função load não criou o arquivo de saída."
