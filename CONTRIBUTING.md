# 🤝 Guia de Contribuição

Obrigado por querer contribuir com o **OmegaTech**! Este documento fornece diretrizes para contribuir ao projeto.

## 📝 Código de Conduta

Por favor, note que este projeto é lançado com um [Código de Conduta](CODE_OF_CONDUCT.md). Ao participar neste projeto, você concorda em honrar este código.

## 🐛 Encontrou um Bug?

**Não abra uma issue de GitHub se o bug for uma vulnerabilidade de segurança** em vez disso, envie um email para `seguranca@omegatech.com.br`.

Antes de criar uma issue de bug, por favor, faça uma busca no repositório. Ela pode já ter sido reportada.

### Como Reportar um Bug

1. Abra uma [Issue](https://github.com/omega-techh/Projeto_OmegaTech/issues/new)
2. Use um título descritivo
3. Forneça:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento observado
   - Comportamento esperado
   - Screenshots (se aplicável)
   - Versão do Python, Django, OS

---

## 💡 Sugestões e Melhorias

Ressalvas sobre sugestões:

1. Use um título claro e descritivo
2. Forneça descrição detalhada
3. Liste exemplos específicos
4. Descreva o comportamento atual vs esperado
5. Explique por que essa mudança seria útil

---

## 🚀 Contribuições de Código

### Preparação

1. Faça um Fork do repositório
2. Clone sua cópia:
   ```bash
   git clone https://github.com/seu_usuario/Projeto_OmegaTech.git
   ```
3. Configure ambiente virtual e dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   pip install -r requiriments.txt
   ```

### Desenvolvimento

1. Crie uma branch para sua feature:
   ```bash
   git checkout -b feature/descricao-da-feature
   ```

2. Commit suas mudanças:
   ```bash
   git commit -m "type(scope): descrição clara e concisa
   
   Descrição mais detalhada se necessário.
   
   Closes #123
   ```

3. Siga o padrão de commits:
   - `feat:` Nova funcionalidade
   - `fix:` Correção de bug
   - `docs:` Alterações de documentação
   - `style:` Formatação, sem mudanças de lógica
   - `refactor:` Refatoração de código
   - `perf:` Melhorias de performance
   - `test:` Testes
   - `ci:` Configuração CI/CD

### Standards de Código

#### Python

- Siga [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use `black` para formatação: `black .`
- Use `flake8` para linting: `flake8 .`
- Documente suas funções:
  ```python
  def minha_funcao(param1, param2):
      """
      Descrição breve.
      
      Args:
          param1 (str): Descrição do param1
          param2 (int): Descrição do param2
          
      Returns:
          bool: Descrição do retorno
          
      Raises:
          ValueError: Se algo der errado
      """
      pass
  ```

#### Django

- Use ModelSerializer para APIs REST
- Implemente testes para novos endpoints
- Use migrations para alterações de banco de dados
- Documente os endpoints em docstrings

### Testes

```bash
# Executar todos os testes
python manage.py test

# Executar testes específicos
python manage.py test usuario.tests

# Com coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📤 Enviando um Pull Request

1. Faça push para sua branch:
   ```bash
   git push origin feature/descricao
   ```

2. Abra um Pull Request no GitHub

3. Preencha o template de PR:
   - Descrição clara do que foi mudado
   - Por que foi mudado
   - Como testar
   - Screenshots (se aplicável)
   - Checklist de verificação

4. Aguarde revisão de código

5. Faça ajustes se solicitado

6. Uma vez aprovado, sua PR será mergeada

---

## 📚 Estrutura de Diretórios

Quando adicionar nova funcionalidade, respeite a estrutura:

```
nova_funcionalidade/
├── __init__.py
├── models.py          # Modelos Django
├── serializers.py     # Serializadores DRF
├── views.py           # Views/ViewSets
├── urls.py            # URLs
├── admin.py           # Admin Django
├── tests.py           # Testes unitários
├── migrations/        # Migrações
└── apps.py            # Config da app
```

---

## 📋 Checklist antes de Submeter

- [ ] Código segue PEP 8
- [ ] Testes passam: `python manage.py test`
- [ ] Coverage adequada
- [ ] Documentação atualizada
- [ ] `black` aplicado: `black .`
- [ ] `flake8` sem erros: `flake8 .`
- [ ] Commit messages seguem convencionalização
- [ ] Branch está atualizada com `main`
- [ ] Sem conflitos de merge

---

## 🔍 Processo de Revisão

1. Um ou mais mantenedores reviram seu código
2. Solicitações de mudanças ou aprovação
3. Discussão construtiva de possíveis melhorias
4. Merge após aprovação

---

## ❓ Dúvidas?

- Abra uma issue com tag `question`
- Participe das discussões
- Consulte documentação do Django e DRF

---

## 🎖️ Reconhecimento

Contribuidores ativos são reconhecidos em:
- Seção "Contributors" do README
- Release notes
- Comunidade da aplicação

---

**Obrigado por contribuir com OmegaTech! 🚀**
