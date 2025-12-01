# 🚀 Guia Completo: Como Rodar o Projeto TechStore

## 📋 Pré-requisitos

1. **Python 3.8+** instalado
2. **Git** instalado
3. Terminal (PowerShell no Windows)

---

## 🔧 PASSO 1: Configurar o Ambiente Local

### 1.1. Abrir o Terminal

No Windows, abra o **PowerShell** ou **Prompt de Comando**.

### 1.2. Navegar até a Pasta do Projeto

```bash
cd "C:\Users\Meus Dados\Desktop\WEB-III-Exercicio-II-main"
```

### 1.3. Ativar o Ambiente Virtual

```bash
.\venv\Scripts\Activate.ps1
```

**OU** se der erro de permissão:

```bash
venv\Scripts\activate
```

Você deve ver `(venv)` no início da linha do terminal.

---

## 🗄️ PASSO 2: Configurar o Banco de Dados

### 2.1. Aplicar as Migrations

```bash
python manage.py migrate
```

Isso cria todas as tabelas no banco de dados.

### 2.2. Criar um Superusuário (para acessar o admin)

```bash
python manage.py createsuperuser
```

Quando pedir:
- **Username**: `esdrasreis`
- **Email**: `reis@.com` (ou qualquer email)
- **Password**: `1234` (ou a senha que você quiser)

---

## ▶️ PASSO 3: Rodar o Servidor Local

### 3.1. Iniciar o Servidor

```bash
python manage.py runserver
```

Você verá algo como:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### 3.2. Acessar o Site

Abra o navegador e acesse:

```
http://127.0.0.1:8000/
```

### 3.3. Acessar o Admin

```
http://127.0.0.1:8000/admin/
```

- **Usuário**: `esdrasreis`
- **Senha**: `1234` (ou a que você criou)

---

## 📦 PASSO 4: Adicionar Dados no Admin

### 4.1. Criar uma Página (Pagina)

1. No admin, clique em **Paginas** → **Add Pagina**
2. Preencha:
   - **Nome do Site**: `TechStore`
   - **Texto de Chamada**: `A melhor tecnologia, com o melhor preço`
   - **Texto Sobre**: `Somos apaixonados por tecnologia...` (o texto que você quiser)
   - **Endereço**: Seu endereço
   - **E-mail**: Seu email
   - **WhatsApp**: Seu WhatsApp
3. Clique em **Save**

### 4.2. Adicionar Produtos

1. No admin, clique em **Produtos** → **Add Produto**
2. Preencha:
   - **Nome**: Ex: `iPhone 15 Pro`
   - **Preço**: Ex: `8999.00`
   - **Estoque**: Ex: `10`
   - **Descrição**: Descrição do produto
   - **Foto**: Faça upload de uma imagem
3. Clique em **Save**

---

## 🚢 PASSO 5: Fazer Deploy no Render

### 5.1. Verificar Mudanças

```bash
git status
```

### 5.2. Adicionar Mudanças

```bash
git add .
```

### 5.3. Fazer Commit

```bash
git commit -m "Corrige templates e carrossel"
```

### 5.4. Enviar para o GitHub

```bash
git push
```

### 5.5. Deploy no Render

1. Acesse: https://dashboard.render.com
2. Vá no seu serviço **Django_TechStore**
3. Clique em **Manual Deploy** → **Deploy latest commit**
4. Aguarde o build terminar (pode levar 2-5 minutos)

---

## 🔍 PASSO 6: Verificar se Funcionou

Após o deploy, acesse:

```
https://django-techstore.onrender.com
```

**O que deve aparecer:**
- ✅ Logo "TechStore" (não mais "Framework Django")
- ✅ Carrossel com imagens (mesmo que seja a imagem padrão)
- ✅ Página "Sobre" com conteúdo
- ✅ Produtos (se você adicionou no admin)

---

## ⚠️ Problemas Comuns

### Erro: "ModuleNotFoundError"

**Solução**: Instale as dependências:

```bash
pip install -r requirements.txt
```

### Erro: "no such column"

**Solução**: Aplique as migrations:

```bash
python manage.py migrate
```

### Erro: "Port already in use"

**Solução**: Pare o servidor com `CTRL + C` e rode novamente, ou use outra porta:

```bash
python manage.py runserver 8001
```

### Site no Render não atualiza

**Solução**: 
1. Verifique se fez `git push`
2. No Render, force um novo deploy
3. Limpe o cache do navegador (`Ctrl + F5`)

---

## 📝 Comandos Úteis

```bash
# Ativar venv
.\venv\Scripts\Activate.ps1

# Rodar servidor
python manage.py runserver

# Parar servidor
CTRL + C

# Ver mudanças no git
git status

# Adicionar tudo
git add .

# Fazer commit
git commit -m "Sua mensagem aqui"

# Enviar para GitHub
git push

# Aplicar migrations
python manage.py migrate

# Criar migrations (se mudou models.py)
python manage.py makemigrations
```

---

## ✅ Checklist Final

Antes de fazer deploy, verifique:

- [ ] Servidor local funciona (`http://127.0.0.1:8000/`)
- [ ] Admin funciona (`http://127.0.0.1:8000/admin/`)
- [ ] Logo mostra "TechStore" (não "Framework Django")
- [ ] Carrossel aparece (mesmo que com imagem padrão)
- [ ] Página "Sobre" tem conteúdo
- [ ] Fez `git add .` e `git commit`
- [ ] Fez `git push`
- [ ] Deploy no Render foi feito

---

**Pronto! Agora você sabe rodar o projeto localmente e fazer deploy no Render.** 🎉
