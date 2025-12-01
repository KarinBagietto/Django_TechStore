# 🚀 Como Rodar o Projeto - Passo a Passo Simples

## ⚡ COMANDOS RÁPIDOS (Copie e Cole)

Abra o **PowerShell** e cole estes comandos **um por vez**:

```powershell
# 1. Ir para a pasta do projeto
cd "C:\Users\Meus Dados\Desktop\WEB-III-Exercicio-II-main"

# 2. Ativar o ambiente virtual
.\venv\Scripts\Activate.ps1

# 3. Aplicar migrations (se ainda não fez)
python manage.py migrate

# 4. Rodar o servidor
python manage.py runserver
```

Depois, abra o navegador em: **http://127.0.0.1:8000/**

---

## 🔍 Se Der Erro, Veja Aqui:

### ❌ Erro: "python não é reconhecido"
**Solução**: O Python não está no PATH. Use:
```powershell
py manage.py runserver
```
ou
```powershell
python3 manage.py runserver
```

### ❌ Erro: "venv não encontrado"
**Solução**: Crie o ambiente virtual:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### ❌ Erro: "ModuleNotFoundError"
**Solução**: Instale as dependências:
```powershell
pip install -r requirements.txt
```

### ❌ Erro: "no such column" ou erro de banco
**Solução**: Aplique as migrations:
```powershell
python manage.py migrate
```

### ❌ Erro: "Port 8000 already in use"
**Solução**: Pare o servidor anterior (Ctrl+C) ou use outra porta:
```powershell
python manage.py runserver 8001
```

### ❌ Erro de permissão no PowerShell
**Solução**: Execute como Administrador ou use:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## ✅ Verificação Rápida

Depois de rodar `python manage.py runserver`, você deve ver:

```
Performing system checks...
System check identified no issues (0 silenced).
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Se aparecer isso, **está funcionando!** ✅

---

## 🛑 Para Parar o Servidor

Pressione: **CTRL + C** no terminal

---

## 📱 Acessar o Site

- **Site**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

---

**Se ainda não funcionar, me diga qual erro aparece no terminal!** 🔧

