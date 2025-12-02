# 🔐 Como Criar Superusuário no Render - Guia Completo

## ⚠️ Problema: Não consegue acessar o admin

O banco de dados do Render é **separado** do seu computador. Mesmo que você tenha criado o usuário localmente, ele **não existe no Render**.

---

## ✅ SOLUÇÃO 1: Comando Automático (Recomendado)

O comando `create_admin` já está configurado no `render.yaml` e deve executar automaticamente durante o build.

**Verifique nos logs do build se apareceu:**
```
✅ Superusuário "esdrasreis" criado com sucesso!
```

**Se apareceu, use:**
- **Usuário**: `esdrasreis`
- **Senha**: `1234`

---

## ✅ SOLUÇÃO 2: Criar Manualmente via Shell do Render

Se o comando automático não funcionou, siga estes passos:

### Passo 1: Acessar o Shell do Render

1. Acesse: https://dashboard.render.com
2. Vá no seu serviço **Django_TechStore**
3. No menu lateral esquerdo, procure por **"Shell"** ou **"Console"**
4. Clique para abrir o terminal

### Passo 2: Executar o Comando

No shell que abrir, digite:

```bash
python manage.py create_admin
```

Você deve ver:
```
✅ Superusuário "esdrasreis" criado com sucesso!
```

### Passo 3: Testar o Login

Acesse: `https://django-techstore.onrender.com/admin/`

- **Usuário**: `esdrasreis`
- **Senha**: `1234`

---

## ✅ SOLUÇÃO 3: Criar Manualmente com createsuperuser

Se o comando customizado não funcionar, use o comando padrão do Django:

### No Shell do Render:

```bash
python manage.py createsuperuser
```

Quando pedir:
- **Username**: `esdrasreis`
- **Email**: `reis@.com`
- **Password**: `1234` (digite duas vezes)

---

## ✅ SOLUÇÃO 4: Usar o Script Python Direto

Se nenhuma das opções acima funcionar:

### No Shell do Render:

```bash
python create_superuser.py
```

Este script cria o usuário diretamente sem usar comandos Django.

---

## 🔍 Como Verificar se o Usuário Foi Criado

### No Shell do Render:

```bash
python manage.py shell
```

Depois, dentro do shell Python:

```python
from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.filter(username='esdrasreis').first()
if user:
    print(f"✅ Usuário existe! É superusuário: {user.is_superuser}")
    print(f"É staff: {user.is_staff}")
else:
    print("❌ Usuário não encontrado!")
```

Digite `exit()` para sair do shell.

---

## ⚠️ Problemas Comuns

### ❌ Erro: "Command 'create_admin' not found"

**Solução**: O comando não foi reconhecido. Use a **SOLUÇÃO 3** (createsuperuser) ou verifique se os arquivos `app/management/commands/create_admin.py` foram commitados e enviados para o GitHub.

### ❌ Erro: "no such table: auth_user"

**Solução**: As migrations não foram aplicadas. Execute:

```bash
python manage.py migrate
```

### ❌ Erro: "ModuleNotFoundError"

**Solução**: As dependências não foram instaladas. Execute:

```bash
pip install -r requirements.txt
```

### ❌ Login ainda não funciona após criar o usuário

**Solução**: 
1. Verifique se o usuário foi criado (use o código de verificação acima)
2. Tente resetar a senha:
   ```bash
   python manage.py changepassword esdrasreis
   ```
3. Limpe o cache do navegador (`Ctrl + Shift + Delete`)

---

## 📝 Credenciais Padrão

- **Usuário**: `esdrasreis`
- **Senha**: `1234`
- **Email**: `reis@.com`

---

## 🎯 Resumo Rápido

1. **Tente primeiro**: Acesse o admin com `esdrasreis / 1234` (pode já estar criado)
2. **Se não funcionar**: Vá no Shell do Render e execute `python manage.py create_admin`
3. **Se ainda não funcionar**: Use `python manage.py createsuperuser` e crie manualmente
4. **Teste**: Acesse `https://django-techstore.onrender.com/admin/`

---

**Dica**: Sempre verifique os logs do build no Render para ver se o comando `create_admin` foi executado com sucesso!
