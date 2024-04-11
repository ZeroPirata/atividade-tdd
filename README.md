1º Baixar o repositorio para o local:

```bash
    git clone https://github.com/ZeroPirata/atividade-tdd
```

2º Criar ambiente virutal com o python (recomendo o python 3.12) e baixar as dependencias do projeto

```bash
    python3.12 -m venv .venv
    
    win: .venv\Scripts\activate
    linux: source .venv\bin\activate

    (.venv) pip install -r requirements.txt
```

3º Rodar o teste que deseja:

```bash
    # Rodar todos ao mesmo tempo
    pytest
    # Rodar Exercicio Um
    pytest test\pytest test\triangulo_test.py
    # Rodar Exercicio Dois
    pytest test\persona_test.py
    # Rodar Exercicio Três
    pytest test\salario_test.py    
```
