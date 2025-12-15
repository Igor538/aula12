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

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/Igor538/aula12.git
code aula12
```

### 2️⃣ Crie e ative o ambiente virtual
**Windows**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instale as dependências do projeto
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4️⃣ 🔑 Gerar uma SECRET_KEY automaticamente
Após instalar as dependências, execute:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# Copie o valor gerado e substitua a variável SECRET_KEY em settings.py
```

---

### 5️⃣ Ajustar o settings.py
```bash
No settings.py deixe DEBUG = True
```
---

### 6️⃣ Entrar na pasta do projeto
```bash
cd aula12
```
---

### 7️⃣ Execute as migrações do Django
```bash
python manage.py migrate
```

### 8️⃣ Inicie o servidor de desenvolvimento
```bash
python manage.py runserver
```
