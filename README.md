# GERTECH




USE gertech_db;

-- Tabela para Funcionário
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Tabela para Administrador
CREATE TABLE admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Tabela para Empresa
CREATE TABLE companies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    social_name VARCHAR(255) NOT NULL,
    cnpj VARCHAR(14) NOT NULL,
    sector VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    website VARCHAR(255) NOT NULL,
    logo_url VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);


Tecnologias Utilizadas
Linguagem de Programação: Python
Framework Web: Flask
Banco de Dados: SQLAlchemy 
Front-End: HTML, CSS, Bootstrap
JavaScript
 
Funcionalidades
Para Usuários
Cadastro e autenticação de contas.
Navegação e busca de cursos.
Acesso a material educacional (vídeos, documentos, quizzes, etc.).
Progresso do curso e histórico de conclusão.
Perfil de usuário com informações pessoais.
Para Empresas
Cadastro de conta de empresa.
Atribuição de cursos aos funcionários.
Monitoramento do progresso dos funcionários nos cursos.
Acesso a relatórios e métricas de aprendizado.
Para Administradores
Gerenciamento de cursos (criação, edição, exclusão).
Gerenciamento de contas de empresa.
Administração de contas de usuário e administrador.
Geração de relatórios abrangentes.

Instalação e Execução
Crie um ambiente virtual: python -m venv venv
Ative o ambiente virtual:venv\Scripts\activate (Windows)
Instale as dependências: pip install -r requirements.txt
Configure suas variáveis de ambiente em um arquivo .env.

estrutura:
GERTECH/
    ├── app/
    |   ├── __init__.py
    |   ├── routes.py
    |   ├── templates/
    |   |   ├── adicionar_cursos.html
    |   |   ├── adicionar_funcionario.html
    |   |   ├── cadastroempresa.html
    |   |   ├── cadastrofun.html
    |   |   ├── cadastroadm.html
    |   |   ├── cadastro.html
    |   |   ├── index.html
    |   |   ├── login.html
    |   |   ├── registro.html
    |   |   ├── perfil.html
    |   |   ├── cursos.html
    |   |   ├── detalhes_curso.html
    |   |   ├── editar_cursos.html
    |   |   ├── excluir_cursos.html
    |   |   ├── gerenciar_cursos.html
    |   |   ├── adicionar_curso.html
    |   |   ├── editar_curso.html
    |   |   ├── contato.html
    |   |   ├── inscricao_curso.html
    |   |   ├── comunidade.html
    |   |   ├── suporte.html
    |   |   ├── registro.html
    |   |   ├── termos_uso.html
    |   |   ├── politica_privacidade.html
    |   |   ├── registro.html
    |   ├── views
    |   |   ├── adicionar_cursos.py
    |   |   ├── adicionar_funcionario.py
    |   |   ├── cadastroempresa.py
    |   |   ├── cadastrofun.py
    |   |   ├── cadastroadm.py
    |   |   ├── cadastro.py
    |   |   ├── index.py
    |   |   ├── login.py
    |   |   ├── registro.py
    |   |   ├── perfil.py
    |   |   ├── cursos.py
    |   |   ├── detalhes_curso.py
    |   |   ├── editar_cursos.py
    |   |   ├── excluir_cursos.py
    |   |   ├── gerenciar_cursos.py
    |   |   ├── adicionar_curso.py
    |   |   ├── editar_curso.py
    |   |   ├── contato.py
    |   |   ├── inscricao_curso.py
    |   |   ├── comunidade.py
    |   |   ├── suporte.py
    |   |   ├── registro.py
    |   |   ├── termos_uso.py
    |   |   ├── politica_privacidade.py
    |   |   ├── registro.py
    |   ├── static/
    |   |   ├── css/
    |   |   |   ├── styles.css
    |   |   ├── js/
    |   |   |   ├── script.js
    ├── config.py
    ├── run.py
    ├── models.py
    ├── forms.py
    ├── requirements.txt



