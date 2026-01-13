
### Criar ambiente virtual
python -m venv venv

### Ativar ambiente virtual
.\venv\Scripts\activate

### Instalar as dependências do projeto
pip install -r .\requirements.txt

### Entrar na pasta core
cd .\core\

### Criar migrações do banco de dados
python .\manage.py migrate
python .\manage.py makemigrations

### Rodar o backend
python .\manage.py runserver