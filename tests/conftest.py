import pytest
import pandas as pd

@pytest.fixture
def mock_df_bruto():
    
    dados_falsos = {
        'NOME': ['JOÃO', 'MARIA', 'PEDRO', None],
        'IDADE': [25, 30, 35, 40],
        'CIDADE': ['SÃO PAULO', 'RIO DE JANEIRO', 'BRASÍLIA', 'CURITIBA']
    }
    
    return pd.DataFrame(dados_falsos)