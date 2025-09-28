# ControlDesk

## 📌 Sobre o projeto
O **ControlDesk** é uma plataforma de **gestão de despesas corporativas**, pensada especialmente para empresas que possuem colaboradores em viagens.  
O objetivo é oferecer uma solução **simples**, **prática** e **segura** para registrar, controlar e analisar gastos em tempo real.

## 🚀 Funcionalidades
- Perfis de acesso diferenciados (WEB para gestão, WEB-MOBILE para colaboradores).
- Cadastro e gerenciamento de:
  - **Empresas**
  - **Projetos**
  - **Colaboradores**
  - **Usuários**
- Registro de **despesas** com comprovantes em imagem.
- Relatórios automáticos:
  - Gastos mensais por colaborador
  - Gastos por cartão
  - Gastos por projeto
  - Gastos por empresa
- Exportação de relatórios em **PDF** e **Excel**
## 🛠️ Tecnologias
- **Backend:** Flask
- **Frontend (web):** HTML, CSS, JavaScript
- **Banco de Dados:** PostgreSQL

## ⚙️ Instalação e uso
1. Clone o repositório:
   ```bash
   git clone https://github.com/ThiagoHeckler/ControlDesk_Prog4

2. Crie um ambiente virtual
 - python -m venv venv
 - source venv/bin/activate   # Linux/Mac
 - venv\Scripts\activate      # Windows
   
3. Instale as dependências
 - pip install -r requirements.txt

4. Configure as variaveis de ambiente no .env
 - FLASK_ENV=development
 - SECRET_KEY=sua_chave_secreta
 - DATABASE_URL=postgresql://usuario:senha@localhost:5432/controldesk

5. Execute as migrações
- flask db upgrade

6. Inicie o servidor
 - flask run
