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
git clone https://github.com/seu-usuario/aula12.git
cd aula12
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
pip install -r requirements.txt
```

---

## 🔐 4️⃣ Gerar SECRET_KEY e criar o arquivo `.env`

### 🔑 Gerar uma SECRET_KEY automaticamente
Após instalar as dependências, execute:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copie a chave gerada.

---

### 📝 Criar o arquivo `.env`

#### **Linux / macOS**
```bash
cat > .env <<EOF
SECRET_KEY=COLE_SUA_CHAVE_AQUI
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
EOF
```

#### **Windows (PowerShell)**
```powershell
"SECRET_KEY=COLE_SUA_CHAVE_AQUI" > .env
"DEBUG=True" >> .env
"ALLOWED_HOSTS=localhost,127.0.0.1" >> .env
"DATABASE_URL=sqlite:///db.sqlite3" >> .env
```

> ⚠️ **Importante:** Não envie o `.env` para o GitHub!  
Adicione ao `.gitignore`:
```bash
echo ".env" >> .gitignore
```

---

### 5️⃣ Execute as migrações do Django
```bash
python manage.py migrate
```

### 6️⃣ Inicie o servidor de desenvolvimento
```bash
python manage.py runserver
```
