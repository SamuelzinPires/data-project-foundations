# test_pipeline.py

# importar a ferramenta que construímos na outra pasta
from src.pipeline import extract

def test_extracao_dados():
    """Garante que a função extract consegue ler o arquivo e não retorna vazio."""
    
    #Definindo o caminho
    Dados = ("data/input/dados_brutos.csv")
    
    # Extrair os dados usando a função extract
    df = extract(Dados)
    
    # Mensagem de erro embutida para o caso de falha
    assert len(df) > 0
    if AssertionError:
            print("Teste falhou: O DataFrame está vazio. Verifique o caminho do arquivo e o conteúdo.")