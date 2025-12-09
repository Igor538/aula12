# 📝 ListaSimples - Aplicativo de Lista de Afazeres

**ListaSimples** é um aplicativo Django para gerenciar suas tarefas diárias de forma simples e eficiente, com CRUD de tarefas e comentários.

---

## 🛠 Tecnologias

- Python 3.x  
- Django 5.2.8  
- Django REST Framework  
- SQLite (desenvolvimento)  
- Gunicorn  
- django-cors-headers  

---

## 🚀 Passo a Passo

1️⃣ **Clone o repositório**  
```bash
git clone https://github.com/seu-usuario/aula12.git
cd aula12

2️⃣ Crie e ative o ambiente virtual

Windows:

bash
Copiar código
python -m venv venv
.\venv\Scripts\activate
Linux/Mac:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate

3️⃣ Instale as dependências

bash
Copiar código
pip install -r requirements.txt

4️⃣ Configure as variáveis de ambiente
Crie um arquivo .env na raiz do projeto:

env
Copiar código
SECRET_KEY=sua-chave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3

5️⃣ Execute as migrações

bash
Copiar código
python manage.py migrate

6️⃣ Inicie o servidor de desenvolvimento

bash
Copiar código
python manage.py runserver

7️⃣ Acesse o projeto
Abra o navegador em http://127.0.0.1:8000/
