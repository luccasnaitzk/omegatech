# 🚗 OmegaTech - Sistema de Gerenciamento de Veículos Autopropelidos

<div align="center">

[![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow?style=flat-square)](https://github.com/omega-techh)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)](https://www.python.org/.
[![Django](https://img.shields.io/badge/Django-REST%20API-darkgreen?style=flat-square&logo=django)](https://www.djangoproject.com/)

**Plataforma Inteligente para Monitoramento e Otimização de Infraestruturas Sustentáveis**

[Sobre](#sobre) • [Funcionalidades](#funcionalidades) • [Requisitos](#requisitos) • [Instalação](#instalação) • [Estrutura](#estrutura) • [API](#api) • [Contribuidores](#contribuidores)

</div>

---

## 📋 Sobre

OmegaTech é um **Sistema de Gerenciamento de Veículos Autopropelidos (SGVA)** desenvolvido como solução para mobilidade urbana inteligente em cidades litorâneas. O projeto visa reduzir o fluxo de veículos particulares, melhorar o transporte de turistas e moradores através de frotas de veículos elétricos autônomos circulando em rotas específicas próximas à orla das cidades.

### 🎯 Objetivos

- ✅ Reduzir o fluxo de veículos particulares na região da praia
- ✅ Melhorar o transporte de turistas e moradores
- ✅ Utilizar veículos elétricos e autônomos
- ✅ Modernizar a infraestrutura urbana
- ✅ Promover mobilidade sustentável (ODS 9 - ONU)

### 🌍 Contexto & Problemas Identificados

Cidades litorâneas com grande fluxo turístico (como Balneário Camboriú e Santos) enfrentam desafios:
- Congestionamento nas avenidas da orla
- Dificuldade de circulação de turistas
- Aumento da emissão de poluentes
- Falta de estacionamento em áreas centrais
- Sobrecarga do transporte público

---

## ✨ Funcionalidades

### 👤 Para Usuários (Clientes)

- 📱 **Cadastro e Autenticação**: Registro de usuários com validação de CPF e email
- 🗺️ **Busca de Veículos**: Localizar veículos disponíveis próximos
- 🚗 **Alocação de Veículo**: Reservar e iniciar corrida
- 💳 **Sistema de Crédito**: Gerenciar saldo e realizar transações
- 📊 **Histórico de Corridas**: Visualizar trajetórias e dados de deslocamento
- 🔋 **Status do Veículo**: Monitorar bateria e status em tempo real
- 📧 **Notificações**: Alertas sobre bateria, assinatura e promotions

### 🛠️ Para Administradores

- 👁️ **Monitoramento em Tempo Real**: Localização de todos os veículos no mapa
- 📈 **Análise de Dados**: Número de viagens, tempo de uso, frequência por usuário
- 🚗 **Gerenciamento de Frotas**: Cadastro e status de veículos
- 🔧 **Manutenção**: Alterar status de veículos para manutenção
- 📍 **Postos Estratégicos**: Criar postos de recarga e armazenamento
- 🔑 **Gestão de Usuários**: Controle de acessos e permissões

### ⚙️ Funcionalidades de Sistema

- 🛰️ **Rastreamento GPS**: Sistema de localização em tempo real
- 🔋 **Notificação de Bateria**: Alertas automáticos sobre saúde da bateria
- 📧 **Avisos de Assinatura**: Notificações antes do vencimento
- 💰 **Opção de Assinatura**: Planos flexíveis para usuários
- 📊 **Dashboard Power BI**: Visualizações avançadas de dados

---

## 📋 Requisitos

### Funcionais
- Cadastro de usuários e veículos
- Sistema de crédito e transações
- Armazenamento de trajetórias
- Iniciar/encerrar alocação de veículos
- Sistema de status do veículo
- Cadastro de postos estratégicos (recarga/armazenamento)
- Marcar pontos de saída e chegada
- Alteração de status para manutenção

### Não-Funcionais
- Notificação automática de bateria
- Visualização de status do veículo para clientes
- Aviso por email sobre assinatura
- Opção de planos de assinatura
- Dashboard administrativo com insights
- Rastreamento em tempo real

### 🏢 Regras de Negócios
- Os veículos possuem sistema de rastreamento e localização
- **Sem assinatura ou créditos**, não é permitido usar um veículo
- **Tempo mínimo de locação**: 10 minutos
- Saúde da bateria deve ser monitorada constantemente

---

## 💻 Tecnologias Utilizadas

<table>
<tr>
<td><strong>Backend</strong></td>
<td>
  
- **Python 3.9+**
- **Django 4.x**
- **Django REST Framework**
- **SQLite** (desenvolvimento)
- **PostgreSQL** (produção)

</td>
</tr>
<tr>
<td><strong>Frontend</strong></td>
<td>

- **Vue.JS**
- **Vite**
- **Mapa Interativo** (integração de GPS)
- **Dashboard UI** (modulado)

</td>
</tr>
<tr>
<td><strong>Analytics</strong></td>
<td>

- **Power BI** - Visualizações e relatórios
- **PostgreSQL** - Data warehouse

</td>
</tr>
<tr>
<td><strong>DevOps & Ferramentas</strong></td>
<td>

- **Docker** (containerização)
- **GitHub** (versionamento)
- **Git** (controle de versão)

</td>
</tr>
</table>

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.9+
- pip (gerenciador de pacotes Python)
- Git
- Virtualenv ou venv

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone https://github.com/omega-techh/Projeto_OmegaTech.git
   cd Projeto_OmegaTech
   ```

2. **Crie um ambiente virtual**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requiriments.txt
   ```

4. **Execute as migrações**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

   O servidor estará disponível em: `http://localhost:8000`

---

## 📁 Estrutura do Projeto

```
Projeto_OmegaTech/
├── api/                    # Aplicação de APIs gerais
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── assinatura/            # Módulo de Assinaturas
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── carteira/              # Módulo de Carteira/Crédito
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── corrida/               # Módulo de Corridas/Locações
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── localizacao/           # Módulo de Localização/GPS
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── manutencao/            # Módulo de Manutenção
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── plano/                 # Módulo de Planos de Assinatura
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── sgva/                  # Configuração principal do Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── transacao/             # Módulo de Transações
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── usuario/               # Módulo de Usuários
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── veiculo/               # Módulo de Veículos
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── manage.py              # Gerenciador Django
├── db.sqlite3             # Banco de dados (dev)
├── requiriments.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

---

## 🔌 API Endpoints

### Usuários
```
POST   /api/usuarios/              # Criar usuário
GET    /api/usuarios/              # Listar usuários
GET    /api/usuarios/{id}/         # Detalhar usuário
PUT    /api/usuarios/{id}/         # Atualizar usuário
DELETE /api/usuarios/{id}/         # Deletar usuário
```

### Veículos
```
POST   /api/veiculos/              # Cadastrar veículo
GET    /api/veiculos/              # Listar veículos
GET    /api/veiculos/{id}/         # Detalhar veículo
PUT    /api/veiculos/{id}/         # Atualizar veículo
PATCH  /api/veiculos/{id}/status/  # Alterar status
```

### Corridas
```
POST   /api/corridas/              # Iniciar corrida
GET    /api/corridas/              # Listar corridas
GET    /api/corridas/{id}/         # Detalhar corrida
PUT    /api/corridas/{id}/         # Finalizar corrida
GET    /api/corridas/{id}/rota/    # Obter rota da corrida
```

### Localização
```
GET    /api/localizacao/           # Localização em tempo real
GET    /api/localizacao/{id}/      # Localização específica do veículo
POST   /api/postos/                # Cadastrar posto estratégico
GET    /api/postos/                # Listar postos
```

### Carteira
```
GET    /api/carteira/              # Saldo atual
POST   /api/carteira/adicionar/    # Adicionar crédito
GET    /api/carteira/historico/    # Histórico de transações
```

### Assinatura
```
GET    /api/planos/                # Listar planos
POST   /api/assinatura/            # Contratar assinatura
GET    /api/assinatura/            # Detalhes da assinatura
```

### Manutenção
```
POST   /api/manutencao/            # Criar manutenção
GET    /api/manutencao/            # Listar manutenções
GET    /api/transacao/             # Histórico de transações
```

---

## 🗄️ Modelo de Banco de Dados

O projeto utiliza as seguintes tabelas principais:

| Tabela | Descrição |
|--------|-----------|
| `usuario` | Dados dos usuários (nome, email, CPF, data) |
| `veiculo` | Informações dos veículos (modelo, bateria, status) |
| `corrida` | Registro de corridas (data início, fim, valor) |
| `localizacao` | Posição GPS dos veículos |
| `carteira` | Saldo de créditos dos usuários |
| `assinatura` | Planos de assinatura |
| `transacao` | Histórico de transações |
| `manutencao` | Registros de manutenção |
| `porto` | Postos de recarga/armazenamento |
| `plano` | Tipos de planos oferecidos |

---

## 👥 Contribuidores

<table>
<tr>
    <td align="center">
        <strong>Eduardo K. M. C.</strong>
        <br><small>116473</small>
    </td>
    <td align="center">
        <strong>Felipe F. C.</strong>
        <br><small>116734</small>
    </td>
    <td align="center">
        <strong>Henrique Lopes de Freitas</strong>
        <br><small>117539</small>
    </td>
</tr>
<tr>
    <td align="center">
        <strong>Lincon Samuel de Andrade</strong>
        <br><small>116545</small>
    </td>
    <td align="center">
        <strong>Luccas Naitzk Silva</strong>
        <br><small>116552</small>
    </td>
    <td align="center">
        <strong>Matheus Francisco Cordeiro</strong>
        <br><small>117637</small>
    </td>
</tr>
</table>

---

## 🔄 Ciclo de Vida do Projeto

O projeto segue metodologia **SCRUM** orientada por sprints iterativas:

1. **Planejamento**: Definição de requisitos e escopo
2. **Desenvolvimento**: Implementação de funcionalidades
3. **Testes**: Validação e aprovação
4. **Deploy**: Implementação em produção

---

## 📊 Status do Projeto

**Fase Atual:** 2ª Fase do Projeto Técnico

- ✅ Banco de dados estruturado
- ✅ APIs REST implementadas
- ✅ Protótipos de frontend
- 🔄 Integração frontend-backend (em progresso)
- 🔄 Testes completos (em progresso)
- ⏳ Deploy em produção (próximo)
  
---

## 📄 Licença

Este projeto está sob licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---