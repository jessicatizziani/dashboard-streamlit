# 📊 **Dashboard Interativo com Streamlit**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-red?style=for-the-badge&logo=streamlit)
![GitHub Repo Size](https://img.shields.io/github/repo-size/jessicatizziani/dashboard-streamlit?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/jessicatizziani/dashboard-streamlit?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 🚀 Sobre o Projeto

Este projeto é um **dashboard interativo** desenvolvido com **Streamlit**, voltado para **visualização dinâmica de dados** a partir de um arquivo CSV.  

O objetivo principal é permitir que usuários explorem dados de forma intuitiva, com **atualizações automáticas** sempre que a base de dados for modificada.

A aplicação segue **boas práticas de desenvolvimento**, incluindo versionamento com **Git/GitHub**, organização modular do código e **deploy em nuvem via Streamlit Cloud**, demonstrando domínio em **Python**, **visualização de dados** e **entrega de soluções analíticas**.

---

## 🎯 Visão Técnica e Profissional

Este projeto foi concebido com foco em **engenharia de dados e analytics**, cobrindo todo o ciclo de vida de uma solução analítica: ingestão de dados, organização de código, versionamento, visualização interativa e deploy automatizado em ambiente cloud.

Ele demonstra minha capacidade de **estruturar projetos de dados de ponta a ponta**, combinando visão analítica, clareza técnica e preocupação com escalabilidade, usabilidade e boas práticas — competências essenciais para ambientes profissionais orientados a dados.

---

## 🛠️ Tecnologias Utilizadas

Tecnologias e ferramentas aplicadas no projeto:

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white) **Python 3.11**  
![Streamlit](https://img.shields.io/badge/Streamlit-1.0-blue?style=for-the-badge&logo=streamlit&logoColor=white) **Streamlit**  
![Pandas](https://img.shields.io/badge/Pandas-1.0-blue?style=for-the-badge&logo=pandas&logoColor=white) **Pandas**  
![Plotly](https://img.shields.io/badge/Plotly-4.0-blue?style=for-the-badge&logo=plotly&logoColor=white) **Plotly (gráficos interativos)**  
![Git](https://img.shields.io/badge/Git-2.0-blue?style=for-the-badge&logo=git&logoColor=white) **Git & GitHub**  
![Streamlit Cloud](https://img.shields.io/badge/Streamlit_Cloud-green?style=for-the-badge&logo=streamlit&logoColor=white) **Streamlit Cloud**

---

## 🗂️ Estrutura do Projeto

```text
dashboard-streamlit/
│
├── app/
│   ├── dashboard.py      # Arquivo principal da aplicação Streamlit
│   └── utils.py          # Funções auxiliares (ex: carregamento de dados)
│
├── data/
│   └── dados.csv         # Base de dados utilizada no dashboard
│
├── .gitignore            # Arquivos ignorados pelo Git
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
▶️ Como Rodar o Projeto Localmente
1️⃣ Clone o repositório
bash
Copiar código
git clone https://github.com/jessicatizziani/dashboard-streamlit.git
cd dashboard-streamlit
2️⃣ Crie e ative o ambiente virtual
bash
Copiar código
python -m venv venv
Windows:

bash
Copiar código
venv\Scripts\activate
Linux / Mac:

bash
Copiar código
source venv/bin/activate
3️⃣ Instale as dependências
bash
Copiar código
pip install -r requirements.txt
4️⃣ Execute o dashboard
bash
Copiar código
streamlit run app/dashboard.py
A aplicação estará disponível em:
👉 http://localhost:8501

🔄 Atualização dos Dados
Os dados podem ser atualizados diretamente no arquivo CSV localizado na pasta data/.

Após realizar alterações, execute:

bash
Copiar código
git add data/
git commit -m "Atualiza dados do dashboard"
git push
O Streamlit Cloud realizará o redeploy automático da aplicação.

🌐 Aplicação Online
👉 Link do Dashboard:
https://dashboarddadosficticios.streamlit.app/

👩‍💻 Autora
Jessica Tizziani
Ciência de Dados | Engenharia de Dados | Gerenciamento de Projetos

Projeto desenvolvido para fins de aprendizado, portfólio profissional e compartilhamento de conhecimento em dados.