
# 🦇 Projeto Final - Sistema de Gerenciamento de Segurança das Indústrias Wayne

Este é um projeto full stack desenvolvido com **Django**, **HTML** e **CSS** como parte do desafio final do curso DEV FULL STACK. Inspirado pelas necessidades das Indústrias Wayne (sim, do próprio Batman 🦇), o sistema visa otimizar a segurança e o controle interno da empresa.

---

## 🚀 Funcionalidades

### 🔐 Controle de Acesso
- Sistema de **login com autenticação e autorização** por níveis de usuário:
  - Funcionários
  - Gerentes
  - Administradores de segurança
- Acesso restrito a áreas específicas com base no perfil do usuário.

### 🛠️ Gestão de Recursos
- Interface intuitiva para gerenciar:
  - Inventário de equipamentos
  - Veículos e dispositivos de segurança
- Operações de **CRUD** (criar, ler, atualizar, deletar) para recursos internos.

### 📊 Dashboard de Visualização
- Painel visual com dados estratégicos:
  - Atividades recentes
  - Status de segurança
  - Recursos disponíveis
- Interface responsiva e moderna, feita com HTML e CSS puros.

---

## 💻 Tecnologias Utilizadas

| Frontend | Backend | Banco de Dados |
|----------|---------|----------------|
| HTML5 + CSS3 | Django (Python) | SQLite |

---

## 🗂️ Organização do Projeto

\`\`\`bash
.
├── manage.py
├── projeto/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── app/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── static/
└── README.md
\`\`\`

---

## 📦 Como executar o projeto localmente

1. Clone o repositório:
\`\`\`bash
git clone https://github.com/seuusuario/industrias-wayne.git
cd industrias-wayne
\`\`\`

2. Crie um ambiente virtual e ative:
\`\`\`bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
\`\`\`

3. Instale as dependências:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. Rode as migrações e inicie o servidor:
\`\`\`bash
python manage.py migrate
python manage.py runserver
\`\`\`

---

## 👤 Autor

Desenvolvido por **[Seu Nome Aqui]**  
🔗 [Seu LinkedIn] • [Seu Portfólio]

---

## 📌 Observações

Este projeto foi desenvolvido com fins educacionais, focando na prática dos conceitos de desenvolvimento web full stack. É um ótimo exemplo de como aplicar autenticação, autorização e gestão de dados de forma integrada usando Django.

---

## 🌟 Sugestões de melhoria (caso queira evoluir o projeto)

- Adicionar testes automatizados com `pytest-django`.
- Integrar com banco de dados PostgreSQL.
- Implementar responsividade com TailwindCSS ou Bootstrap.
- Adicionar gráficos interativos com Chart.js ou D3.js no dashboard.
- Criar sistema de logs de atividades.

---

🦇 *"Porque até o Batman precisa de um bom sistema de segurança."*
