# Concelho+ Limpo

> 🇵🇹 Português | 🇬🇧 [English below](#english)

---

## 🇵🇹 Português

### Descrição

**Concelho+ Limpo** é uma aplicação web desenvolvida para facilitar a gestão de resíduos a nível municipal de forma segura e privada.

O projeto resolve um problema real: muitos residentes evitam pedir a recolha de resíduos especiais (monos domésticos, entulho, etc.) por não quererem expor publicamente a sua morada ou dados pessoais. Esta aplicação permite submeter pedidos de forma confidencial, diretamente à câmara municipal, sem exposição pública.

### Funcionalidades

- **Pedido de Recolha** — O residente submete um pedido de recolha de resíduos indicando o tipo de resíduo, morada, e contacto (telefone ou email). Os dados são confidenciais e apenas visíveis pela administração municipal.
- **Reportar Contentor** — Qualquer pessoa pode reportar um contentor negligenciado ou danificado, com localização e fotografia.
- **Mapa de Ecopontos** — Mapa interativo (Google Maps) com a localização de todos os ecopontos e contentores do concelho.
- **Painel de Administração** — Área reservada a funcionários municipais com login protegido. Permite visualizar e gerir todos os pedidos de recolha, ocorrências reportadas e ecopontos.

### Stack Tecnológica

- **Backend:** Python 3, Flask
- **Base de Dados:** MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Mapa:** Google Maps API

### Instalação

**Pré-requisitos:** Python 3.x, MySQL

```bash
# Clonar o repositório
git clone https://github.com/FilipeCacador2/Concelho-Limpo.git
cd Concelho-Limpo

# Instalar dependências
pip install -r requirements.txt

# Configurar a base de dados
# Importar o ficheiro concelho_limpo.sql no MySQL

# Iniciar a aplicação
python app.py
```

A aplicação ficará disponível em `http://localhost:5000`.

### Configuração da Base de Dados

Antes de iniciar, configure as credenciais MySQL no ficheiro `app.py`:

```python
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",       # A sua password
        database="concelho_limpo"
    )
```

### Estrutura do Projeto

```
Concelho-Limpo/
├── app.py                  # Aplicação principal Flask
├── concelho_limpo.sql      # Estrutura e dados da base de dados
├── requirements.txt        # Dependências Python
├── templates/
│   ├── index.html          # Página pública (pedidos e mapa)
│   ├── admin.html          # Painel de administração
│   └── login.html          # Login de administrador
└── static/
    ├── css/                # Estilos
    ├── js/                 # Scripts (incluindo integração Google Maps)
    └── icons/              # Ícones e favicon
```

### Licença

Este projeto está licenciado sob a **GNU General Public License v3.0**.
Desenvolvido por **Filipe Caçador** — © 2025

---

## 🇬🇧 English <a name="english"></a>

### Description

**Concelho+ Limpo** is a web application designed to facilitate municipal waste management in a secure and privacy-focused way.

The project addresses a real problem: many residents avoid requesting special waste collection (bulky items, rubble, etc.) because they don't want to publicly expose their address or personal data. This application allows submissions to be made confidentially, directly to the local council, without any public exposure.

### Features

- **Collection Request** — Residents submit a waste collection request specifying the type of waste, address, and contact details (phone or email). Data is confidential and only visible to municipal staff.
- **Report a Container** — Anyone can report a neglected or damaged waste container, with location and photo.
- **Recycling Point Map** — Interactive map (Google Maps) showing the location of all recycling points and containers in the municipality.
- **Admin Dashboard** — A protected area for municipal employees with login authentication. Allows viewing and managing all collection requests, reported incidents, and recycling points.

### Tech Stack

- **Backend:** Python 3, Flask
- **Database:** MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Map:** Google Maps API

### Installation

**Prerequisites:** Python 3.x, MySQL

```bash
# Clone the repository
git clone https://github.com/FilipeCacador2/Concelho-Limpo.git
cd Concelho-Limpo

# Install dependencies
pip install -r requirements.txt

# Set up the database
# Import concelho_limpo.sql into MySQL

# Run the application
python app.py
```

The application will be available at `http://localhost:5000`.

### Database Configuration

Before running, configure your MySQL credentials in `app.py`:

```python
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",       # Your password
        database="concelho_limpo"
    )
```

### Project Structure

```
Concelho-Limpo/
├── app.py                  # Main Flask application
├── concelho_limpo.sql      # Database schema and data
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html          # Public page (requests and map)
│   ├── admin.html          # Administration dashboard
│   └── login.html          # Admin login
└── static/
    ├── css/                # Stylesheets
    ├── js/                 # Scripts (including Google Maps integration)
    └── icons/              # Icons and favicon
```

### License

This project is licensed under the **GNU General Public License v3.0**.
Developed by **Filipe Caçador** — © 2025
