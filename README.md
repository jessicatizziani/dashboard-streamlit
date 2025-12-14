# 📊 **Dashboard Interativo com Streamlit**

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-red?style=for-the-badge&logo=streamlit)
![GitHub Repo Size](https://img.shields.io/github/repo-size/jessicatizziani/dashboard-streamlit?style=for-the-badge)
![Last Commit](https://img.shields.io/github/last-commit/jessicatizziani/dashboard-streamlit?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)


## 🚀 Sobre o projeto

Este projeto é um **dashboard interativo** criado com **Streamlit**, desenvolvido para **visualização dinâmica de dados** a partir de um arquivo CSV. O objetivo principal é permitir que usuários visualizem e interajam com dados em tempo real, com **atualizações automáticas** sempre que a planilha for alterada.

A aplicação está organizada de forma a utilizar **boas práticas** de desenvolvimento, como **versionamento com Git** e **deploy na nuvem** com **Streamlit Cloud**. O projeto foi criado para demonstrar meu domínio em **Python**, **Streamlit**, e **processamento de dados**.

---

## 🛠️ **Tecnologias Utilizadas**

Tecnologias e ferramentas usadas no projeto, com seus respectivos ícones:

- ![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white) **Python 3.11**
- ![Streamlit](https://img.shields.io/badge/Streamlit-1.0-blue?style=for-the-badge&logo=streamlit&logoColor=white) **Streamlit**
- ![Pandas](https://img.shields.io/badge/Pandas-1.0-blue?style=for-the-badge&logo=pandas&logoColor=white) **Pandas**
- ![Plotly](https://img.shields.io/badge/Plotly-4.0-blue?style=for-the-badge&logo=plotly&logoColor=white) **Plotly (para gráficos interativos)**
- ![Git](https://img.shields.io/badge/Git-2.0-blue?style=for-the-badge&logo=git&logoColor=white) **Git & GitHub**
- ![Streamlit Cloud](https://img.shields.io/badge/Streamlit_Cloud-green?style=for-the-badge&logo=streamlit&logoColor=white) **Streamlit Cloud**

---

## 🗂️ **Estrutura do Projeto**

Aqui está um **organograma** do projeto, representando a estrutura das pastas e arquivos em **Markdown**:

```mermaid
graph TB
    A[Dashboard] --> B[app]
    A[Dashboard] --> C[data]
    A[Dashboard] --> D[.gitignore]
    A[Dashboard] --> E[README.md]
    A[Dashboard] --> F[requirements.txt]

    B --> B1[dashboard.py]
    B --> B2[utils.py]
    C --> C1[dados.csv]

▶️ Como Rodar o Projeto Localmente

1️⃣ Clone o repositório

git clone https://github.com/jessicatizziani/dashboard-streamlit.git
cd dashboard-streamlit

2️⃣ Crie e ative o ambiente virtual

python -m venv venv

# Para Windows
venv\Scripts\activate

# Para Linux / Mac
source venv/bin/activate

3️⃣ Instale as dependências
bash

pip install -r requirements.txt

4️⃣ Execute o dashboard

streamlit run app/dashboard.py

A aplicação estará disponível em http://localhost:8501.

🔄 Atualização dos Dados
Os dados podem ser atualizados diretamente no arquivo CSV localizado na pasta data/.

Após atualizar o arquivo, execute:

bash
Copiar código
git add data/
git commit -m "Atualiza dados do dashboard"
git push
O Streamlit Cloud fará o redeploy automático.

🌐 Aplicação Online
👉 Link do Dashboard:
(adicione o link gerado pelo Streamlit Cloud após o deploy)

👩‍💻 Autora
Jessica Tizziani
Analista de Custos | Ciência de Dados | Engenharia de Dados

Projeto desenvolvido para fins de aprendizado, portfólio e compartilhamento de conhecimento em dados.