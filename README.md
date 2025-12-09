# 📝 ListaSimples - Aplicativo de Lista de Afazeres

**ListaSimples** é um aplicativo Django para gerenciar suas tarefas diárias de forma simples e eficiente, com CRUD de tarefas e comentários.

---

## 🛠 Tecnologias

- 🐍 Python 3.x  
- 🌐 Django 5.2.8  
- 📦 Django REST Framework  
- 💾 SQLite (desenvolvimento)  
- 🚀 Gunicorn  
- 🔌 django-cors-headers  

---

## 🚀 Passo a Passo para Rodar o Projeto

```bash
# 1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/aula12.git
cd aula12

# 2️⃣ Crie e ative o ambiente virtual
# Windows:
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac:
python3 -m venv venv
source venv/bin/activate

# 3️⃣ Instale as dependências do projeto
pip install -r requirements.txt

# 4️⃣ Configure as variáveis de ambiente
# Crie um arquivo .env na raiz do projeto com:
echo "SECRET_KEY=sua-chave-secreta" >> .env
echo "DEBUG=True" >> .env
echo "ALLOWED_HOSTS=localhost,127.0.0.1" >> .env
echo "DATABASE_URL=sqlite:///db.sqlite3" >> .env

# 5️⃣ Execute as migrações do Django
python manage.py migrate

# 6️⃣ Inicie o servidor de desenvolvimento
python manage.py runserver

# 7️⃣ Abra o projeto no navegador
# Acesse em: http://127.0.0.1:8000/
