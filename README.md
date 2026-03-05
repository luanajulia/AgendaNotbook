# 💻 Notebook Scheduler - Sistema de Agendamento

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQL Server](https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white)

O **Notebook Scheduler** é uma aplicação web desenvolvida para organizar o empréstimo de equipamentos (notebooks) entre colaboradores. O sistema evita conflitos de horários e garante que os ativos da empresa sejam rastreados corretamente.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python 3.x com Framework **Flask**.
* **Frontend:** HTML5, CSS3 (Design Responsivo).
* **Banco de Dados:** Microsoft SQL Server.
* **ORM/Conector:** Flask-SQLAlchemy ou PyODBC.

---

## ⚙️ Funcionalidades Principal

* **Reserva de Equipamento:** Seleção de data e horário para retirada e devolução.
* **Gestão de Inventário:** Cadastro e status de disponibilidade dos notebooks.
* **Histórico de Uso:** Log de quem utilizou cada máquina e por quanto tempo.
* **Interface Amigável:** Painel visual para consulta rápida de horários vagos.

---

## 🏗️ Estrutura do Banco de Dados



O banco de dados SQL Server armazena as seguintes entidades principais:
* **Users:** Informações de quem está agendando.
* **Notebooks:** Cadastro técnico dos aparelhos (ID, Marca, Modelo).
* **Schedules:** O vínculo entre usuário, máquina e tempo.

---

📂 Estrutura de Pastas
Plaintext
```bash
├── static/          # Arquivos CSS, JS e Imagens
├── templates/       # Arquivos HTML (Jinja2)
├── app.py           # Arquivo principal do Flask
├── models.py        # Definição das tabelas SQL Server
└── requirements.txt # Lista de bibliotecas Python
```
*👩‍💻 Autora Desenvolvido com ❤️ por Luana Julia.*
