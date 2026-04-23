# Data Project Foundations

[![CI Pipeline](https://github.com/SamuelzinPires/data-project-foundations/actions/workflows/ci.yml/badge.svg)](https://github.com/SamuelzinPires/data-project-foundations/actions/workflows/ci.yml)

> Projeto fundacional de Engenharia de Dados focado nas melhores práticas de Engenharia de Software: construção de pipeline ETL em Python, isolamento de ambiente com Poetry, testes unitários com Pytest e CI/CD com GitHub Actions.

## Sobre o Projeto

No mercado atual, pipelines de dados quebram silenciosamente por falta de testes e automação. Este repositório foi criado com o objetivo de treinar e desenvolver as minhas habilidades práticas nessas competências.  

**Stack Tecnológica:**
- **Linguagem:** Python 3.12+
- **Gestão de Dependências:** Poetry
- **Testes e Mocks:** Pytest & Pytest-cov (Cobertura > 90%)
- **Manipulação de Dados:** Pandas
- **Integração Contínua (CI):** GitHub Actions

## ⚙️ Como Executar Localmente

**1. Clone o repositório:**
```bash
git clone [https://github.com/SamuelzinPires/data-project-foundations.git](https://github.com/SamuelzinPires/data-project-foundations.git)
cd data-project-foundations
````

**2. Instale as dependências isoladas:**

```bash
poetry install
```

**3. Execute a bateria de testes automatizados:**

```bash
poetry run pytest -v
```

**4. Verifique a cobertura de código:**

```bash
poetry run pytest --cov=src
```

## 📂 Estrutura da Arquitetura

```text
data-project-foundations/
├── src/                     # Código fonte do pipeline ETL
│   ├── extract.py           # Extração de dados brutos
│   ├── transform.py         # Regras de negócio e limpeza
│   ├── load.py              # Consolidação de saída
│   └── pipeline.py          # Orquestrador principal
├── tests/                   # Bateria de testes unitários
│   ├── conftest.py          # Fixtures e mocks compartilhados
│   └── test_pipeline.py     # Casos de uso de extração e falha de I/O
├── .github/workflows/       # Configuração do robô de CI/CD
│   └── ci.yml               # Esteira executada em todo git push
├── data/                    # Dados locais (ignorados via .gitignore)
├── pyproject.toml           # Manifesto do Poetry e dependências
└── README.md                # Documentação do projeto

```
