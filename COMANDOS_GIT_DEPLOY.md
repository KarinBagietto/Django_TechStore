# 🚀 Comandos Git para Deploy - TechStore

## 📋 Passo a Passo Completo

### ⚡ PASSO 1: Verificar as Alterações

Abra o **PowerShell** na pasta do projeto e execute:

```powershell
cd "C:\Users\Meus Dados\Desktop\WEB-III-Exercicio-II-main"
.\venv\Scripts\Activate.ps1
git status
```

Você deve ver os arquivos modificados:
- `app/templates/index.html` (redes sociais)
- `app/templates/template.html` (footer com contatos)
- `app/templates/contato.html` (dados de contato atualizados)
- `app/static/styles/style.css` (logo maior, cores mais escuras, negrito)

---

### 📦 PASSO 2: Adicionar as Alterações ao Git

```powershell
git add .
```

Isso adiciona todos os arquivos modificados ao staging.

---

### 💾 PASSO 3: Fazer Commit

```powershell
git commit -m "Atualiza logo, cores, redes sociais e informações de contato"
```

**Ou use uma mensagem mais descritiva:**
```powershell
git commit -m "Aumenta logo, escurece verde e cinza, adiciona redes sociais, atualiza contatos e aplica negrito nos textos"
```

---

### 📤 PASSO 4: Enviar para o GitHub

```powershell
git push
```

Se pedir usuário e senha:
- **Usuário**: Seu username do GitHub
- **Senha**: Use um **Personal Access Token** (não a senha normal)

**Como criar um Personal Access Token:**
1. Acesse: https://github.com/settings/tokens
2. Clique em "Generate new token" → "Generate new token (classic)"
3. Dê um nome (ex: "Render Deploy")
4. Marque a opção `repo` (todas as permissões de repositório)
5. Clique em "Generate token"
6. **COPIE O TOKEN** (você só verá uma vez!)
7. Use esse token como senha quando o Git pedir

---

### 🌐 PASSO 5: Fazer Deploy no Render

1. **Acesse o Render Dashboard:**
   - Vá para: https://dashboard.render.com
   - Faça login na sua conta

2. **Encontre seu Serviço:**
   - Procure pelo serviço **Django_TechStore** (ou o nome que você deu)
   - Clique nele

3. **Fazer Deploy Manual:**
   - No topo da página, procure por **"Manual Deploy"** ou **"Deploy"**
   - Clique em **"Deploy latest commit"**
   - Aguarde o build terminar (pode levar 2-5 minutos)

4. **Acompanhar os Logs:**
   - Durante o build, você verá os logs em tempo real
   - Procure por mensagens como:
     - ✅ `pip install -r requirements.txt` (instalando dependências)
     - ✅ `python manage.py collectstatic` (coletando arquivos estáticos)
     - ✅ `python manage.py migrate` (aplicando migrations)
     - ✅ `python manage.py create_admin` (criando superusuário)
     - ✅ `gunicorn projeto.wsgi:application` (servidor iniciado)

5. **Verificar se Funcionou:**
   - Quando aparecer **"Your service is live"**, está pronto!
   - Acesse: https://django-techstore.onrender.com (ou sua URL)
   - Pressione **Ctrl + F5** para limpar o cache e ver as mudanças

---

## 📝 Comandos Rápidos (Copie e Cole Tudo de Uma Vez)

```powershell
# 1. Ir para a pasta do projeto
cd "C:\Users\Meus Dados\Desktop\WEB-III-Exercicio-II-main"

# 2. Ativar venv
.\venv\Scripts\Activate.ps1

# 3. Ver mudanças
git status

# 4. Adicionar tudo
git add .

# 5. Fazer commit
git commit -m "Atualiza logo, cores, redes sociais e informações de contato"

# 6. Enviar para GitHub
git push
```

Depois, vá no Render e faça o deploy manual!

---

## ✅ Checklist de Verificação

Após o deploy, verifique:

- [ ] Logo aparece maior (90px)
- [ ] Texto "TechStore" está em negrito
- [ ] Links de navegação (Home, Sobre, etc.) estão em negrito
- [ ] Verde está 2 tons mais escuro
- [ ] Cinza está 2 tons mais escuro
- [ ] Ícones de redes sociais aparecem na página inicial
- [ ] Footer tem informações de contato atualizadas
- [ ] Página de contato tem dados corretos
- [ ] Site carrega sem erros

---

## ⚠️ Problemas Comuns

### ❌ Erro: "Permission denied" no git push

**Solução**: Verifique se você está autenticado:
```powershell
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

### ❌ Erro: "Authentication failed" no git push

**Solução**: Use um **Personal Access Token** em vez da senha (veja PASSO 4)

### ❌ Render não atualiza após o push

**Solução**: 
1. Verifique se o `git push` foi bem-sucedido
2. No Render, force um novo deploy manual
3. Limpe o cache do navegador (`Ctrl + F5`)

### ❌ Erro no build do Render

**Solução**: 
1. Veja os logs do build no Render
2. Procure por mensagens de erro (geralmente em vermelho)
3. Erros comuns:
   - **"ModuleNotFoundError"**: Falta dependência no `requirements.txt`
   - **"no such column"**: Precisa rodar migrations
   - **"collectstatic error"**: Problema com arquivos estáticos

---

## 🎉 Pronto!

Após seguir esses passos, suas alterações estarão:
- ✅ Salvas no GitHub
- ✅ Publicadas no Render
- ✅ Visíveis no site em produção

**Tempo estimado:** 5-10 minutos (incluindo o build no Render)
