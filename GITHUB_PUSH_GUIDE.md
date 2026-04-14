# 📤 Guia: Upload para GitHub

## ✅ Passos Completados

- ✅ Repositório Git inicializado localmente
- ✅ Arquivo `.gitignore` criado (ignora venv, db.sqlite3, __pycache__, etc)
- ✅ `README.md` completo criado com toda documentação do projeto
- ✅ Arquivo `LICENSE` (MIT) adicionado
- ✅ Primeiro commit feito com sucesso

## 📤 Próximos Passos: Push para GitHub

### Opção 1: Conectar a um Repositório Existente

Se já existe um repositório em `https://github.com/omega-techh/...`:

```bash
# Adicione o repositório remoto
git remote add origin https://github.com/omega-techh/seu-repositorio.git

# Renomeie a branch para 'main' (padrão do GitHub)
git branch -M main

# Faça o push
git push -u origin main
```

### Opção 2: Criar um Novo Repositório no GitHub

1. Acesse [github.com/new](https://github.com/new)
2. Preencha:
   - **Repository name**: `Projeto_OmegaTech` (ou similar)
   - **Description**: Sistema de Gerenciamento de Veículos Autopropelidos
   - **Visibility**: Public
   - **NÃO** inicialize com README (já temos um)
3. Clique "Create repository"

4. Na sequência, execute:

```bash
git branch -M main
git remote add origin https://github.com/omega-techh/Projeto_OmegaTech.git
git push -u origin main
```

### Opção 3: Usando SSH (Mais Seguro)

Se já tiver SSH configurado:

```bash
git remote add origin git@github.com:omega-techh/Projeto_OmegaTech.git
git branch -M main
git push -u origin main
```

---

## 🔑 Autenticação no GitHub

### Com Token (Recomendado)

1. GitHub > Settings > Developer settings > Personal access tokens
2. Gere um novo token (escopo: `repo`)
3. Copie o token
4. Ao fazer push, use o token como senha

```bash
git push -u origin main
# Username: seu_usuario
# Password: seu_token
```

### Com Credenciais Salvas (Windows)

```bash
git config --global credential.helper wincred
```

Depois a próxima vez que fizer push, o Git salva as credenciais automaticamente.

---

## 📊 Verificar Status

```bash
# Ver remoto configurado
git remote -v

# Ver branch atual
git branch

# Ver commits
git log --oneline
```

---

## ✨ Depois do Push

Uma vez no GitHub, você pode:

1. ✅ Adicionar Issues para tracking de bugs
2. ✅ Criar Pull Requests para revisão de código
3. ✅ Usar GitHub Projects para Kanban
4. ✅ Configurar GitHub Actions para CI/CD
5. ✅ Adicionar colaboradores ao repositório

---

## 💡 Dicas

- Sempre faça commits com mensagens descritivas
- Use branches para novas features: `git checkout -b feature/nome`
- Faça pull antes de fazer push se trabalhar em equipe

---

**Precisa de ajuda? Consulte:** https://docs.github.com/pt/get-started

