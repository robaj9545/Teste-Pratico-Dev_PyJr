# To-Do List Application

Uma aplicação web moderna de gerenciamento de tarefas com funcionalidades avançadas, desenvolvida com Django REST Framework no backend e React no frontend.

## 🚀 Funcionalidades

### ✅ Funcionalidades Obrigatórias (20 pontos):
- **CRUD de Tarefas (5 pontos)**: Criar, ler, atualizar e deletar tarefas
- **Sistema de Autenticação (5 pontos)**: Registro e login de usuários
- **Marcar tarefas como concluídas (2 pontos)**: Toggle de status das tarefas
- **Filtragem de Tarefas (1 ponto)**: Filtros por status, prioridade e categoria
- **Paginação (1 ponto)**: Navegação paginada de tarefas
- **React Frontend (3 pontos)**: Interface moderna e responsiva
- **Django REST Framework (3 pontos)**: API robusta e bem estruturada

### ✅ Funcionalidades Opcionais:
- **Categorias (2 pontos)**: Sistema completo de categorias coloridas
- **Compartilhamento de tarefas (2 pontos)**: Compartilhar tarefas com outros usuários
- **Docker (3 pontos)**: Containerização completa com Docker Compose

## 🏗️ Arquitetura

### Backend (Django REST Framework)
- **Framework**: Django 4.2 + Django REST Framework
- **Banco de dados**: PostgreSQL
- **Autenticação**: JWT (JSON Web Tokens)
- **Documentação**: Swagger/OpenAPI

### Frontend (React)
- **Framework**: React 18
- **Gerenciamento de Estado**: React Query
- **UI Framework**: React Bootstrap
- **Roteamento**: React Router
- **Formulários**: React Hook Form

### DevOps
- **Containerização**: Docker + Docker Compose
- **Banco de dados**: PostgreSQL 14

## 📁 Estrutura do Projeto

```
app-tasks/
├── backend/                    # Django REST API
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── taskmanager/          # Configurações principais
│   ├── accounts/              # Autenticação
│   ├── tasks/                 # Tarefas
│   ├── categories/            # Categorias
│   └── tests/                 # Testes
├── frontend/                  # React Application
│   ├── package.json
│   ├── Dockerfile
│   ├── public/
│   └── src/
│       ├── components/        # Componentes React
│       ├── services/          # API calls
│       ├── contexts/          # Context providers
│       └── utils/             # Utilitários
├── docker-compose.yml         # Orquestração de containers
└── README.md
```

## 🛠️ Configuração e Instalação

### Pré-requisitos
- Docker e Docker Compose
- Git

### Instalação Rápida com Docker

1. **Clone o repositório**:
```bash
git clone [URL_DO_REPOSITORIO]
cd nome da pasta
```

2. **Execute a aplicação**:
```bash
docker-compose up --build
```

3. **Acesse a aplicação**:
- Frontend: http://localhost:3000
- API: http://localhost:8000/api/docs/
- Admin Django: http://localhost:8000/admin

### Configuração Manual

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```




## 🔧 Decisões de Design

### Backend
1. **Django REST Framework**: Escolhido pela robustez, documentação excelente e ecossistema maduro
2. **JWT Authentication**: Mais escalável que sessions, adequado para SPAs
3. **PostgreSQL**: Banco relacional robusto, adequado para produção
4. **Separação por Apps**: `accounts`, `tasks`, `categories` para melhor organização
5. **ViewSets**: Padrão DRF para operações CRUD consistentes
6. **Filtros Django-filter**: Filtragem flexível e reutilizável
7. **Paginação**: Performance otimizada para grandes datasets

### Frontend
1. **React Query**: Gerenciamento de estado servidor/cliente, cache automático
2. **React Bootstrap**: UI consistente com menos código customizado
3. **Context API**: Gerenciamento de autenticação simples e eficaz
4. **React Hook Form**: Performance otimizada para formulários
5. **Date-fns**: Manipulação de datas lightweight
6. **React Select**: Multi-select para compartilhamento de tarefas

### DevOps
1. **Docker Multi-stage**: Builds otimizados
2. **Health Checks**: Garantir que serviços estejam prontos
3. **Volumes**: Persistência de dados e hot-reload em desenvolvimento
4. **Environment Variables**: Configuração flexível

## 🔒 Segurança

- **CORS**: Configurado para desenvolvimento e produção
- **JWT**: Tokens com expiração automática
- **Validação**: Sanitização de dados no backend
- **Permissões**: Usuários só acessam suas próprias tarefas
- **HTTPS**: Ready para produção (configurar proxy reverso)

```

## 🚀 Deploy em Produção

### Variáveis de Ambiente
```bash
# Backend
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=seudominio.com
DB_NAME=taskmanager_prod
DB_USER=seu_usuario
DB_PASSWORD=sua_senha_segura
DB_HOST=seu_host_db
DB_PORT=5432

# Frontend
REACT_APP_API_URL=https://seudominio.com/api
```

### Comandos de Deploy
```bash

# Subir aplicação
docker-compose up --build -d
```


## 📝 Melhorias Futuras

- [ ] Notificações push
- [ ] Anexos em tarefas
- [ ] Tags personalizadas
- [ ] Dashboard com estatísticas
- [ ] API GraphQL
- [ ] PWA (Progressive Web App)
- [ ] Integração com calendários
- [ ] Importação/Exportação de dados

## 🐛 Problemas Conhecidos

- Corrigir Taks do frontend do APP

---

**Desenvolvido com ❤️ para a Advice Health**