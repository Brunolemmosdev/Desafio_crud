# Desafio_crud
# Desafio CRUD Funcionários

Este projeto é uma aplicação web desenvolvida com Flask utilizando a arquitetura MRV (Model-Router-View) para realizar operações de CRUD (Create, Read, Update, Delete) em uma tabela de funcionários integrada a um banco de dados MySQL.

## Estrutura do Projeto

```
d:\desafio-crud
│
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── funcionario.py
│   ├── routes/
│   │   └── funcionario_routes.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── listar.html
│   │   ├── inserir.html
│   │   └── atualizar.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
├── tabelas.py
└── requirements.txt
```

## Funcionalidades

- Cadastro de funcionários
- Listagem de funcionários
- Atualização de dados de funcionários
- Exclusão de funcionários
- Interface web estilizada com HTML e CSS
- Integração total com banco de dados MySQL

## Como executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure o banco de dados MySQL:**
   - Crie um banco chamado `funcionarios` e a tabela conforme esperado pelo model.
   - Ajuste as credenciais de acesso no arquivo `app/models/funcionario.py` se necessário.

4. **Execute o programa:**
   ```bash
   python tabelas.py
   ```

5. **Acesse no navegador:**
   ```
   http://127.0.0.1:5000
   ```

## Observações

- Para ambiente de produção, utilize um servidor WSGI como Gunicorn.
- O projeto está pronto para ser expandido com novas funcionalidades.

---

**Desenvolvido para fins de estudo
