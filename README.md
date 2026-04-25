# Ordem de Serviço Interno

### Como rodar o projeto:
1. Clone o repositório.
2. Crie seu ambiente virtual: `python -m venv venv`.
3. Ative o venv e instale as dependências: `pip install -r requirements.txt`.
4. Crie um arquivo `.env` com suas credenciais locais do PostgreSQL.
5. Execute as migrações: `python manage.py migrate`.
6. Importe os dados iniciais: `python manage.py loaddata dados.json`.
7. Rode o servidor: `python manage.py runserver`.