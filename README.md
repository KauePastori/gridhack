# ⚡️ GridHack - Simulador Interativo de Falhas em Redes Elétricas

Projeto acadêmico para disciplina de Arquitetura Orientada a Serviço (FIAP 2024).

---

## 📑 Descrição

O **GridHack** é um simulador web que reproduz falhas, isolamento e restauração de nós em uma rede elétrica, integrando conceitos de arquitetura orientada a serviços (SOA). O sistema foi projetado para treinar operadores em cenários críticos (como desastres naturais) utilizando uma aplicação modular e consumo de APIs externas de clima.

- Interface moderna, responsiva e intuitiva.
- Desastres naturais afetam a rede de forma dinâmica.
- Consome dados de clima em tempo real via API pública Open-Meteo.

---

## 🎯 Objetivos de Arquitetura (Como o projeto atende aos critérios)

- **Consumo de API RESTful Externa:** Integração com a Open-Meteo para obtenção dinâmica do clima e simulação de impacto ambiental.
- **Organização Modular:** Separação clara de módulos: _controllers_ (controle/API), _services_ (serviços/lógica), _models_ (dados/entidades).
- **Separação de Camadas:** Camada de controle (FastAPI controllers), camada de serviço (lógica de negócio), camada de dados (modelos Python).
- **Adoção de Padrões:** Uso dos padrões REST, JSON e OpenAPI (Swagger). Código documentado, endpoints padronizados.

---

## 🏗️ Estrutura do Projeto

![image](https://github.com/user-attachments/assets/c77dc64f-853f-4a15-9529-c0cd4ceb6660)



- **controllers/**: Define as rotas e endpoints da API RESTful (controle).
- **services/**: Lógica dos serviços e integração com APIs externas (serviço).
- **models/**: Estruturas de dados da aplicação (dados).
- **static/index.html**: Interface front-end moderna (HTML + JS).
- **main.py**: Ponto de entrada FastAPI.

---

## 💡 Principais Funcionalidades

- **Visualização da Rede Elétrica**: Lista e monitora o status dos nós em tempo real.
- **Isolamento e Restauração**: Isole nós em falha e restaure-os para restabelecer o fornecimento.
- **Simulação de Desastre**: Permite simular desastres naturais que causam falha em nós aleatórios.
- **Consulta de Clima**: Integração com a API Open-Meteo para consulta e impacto real de eventos climáticos na rede.

---

## 🌐 Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI** (API RESTful e documentação automática Swagger)
- **Requests** (consumo de API externa)
- **HTML + CSS + JavaScript** (front-end estático)
- **Open-Meteo API** (https://open-meteo.com/)

---

## 🚀 Como Executar Localmente

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/gridhack-soa.git
   cd gridhack-soa
   
2. **Crie um ambiente virtual:**
   ```sh
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows

3. **Instale as Dependências:**
   ```sh
   fastapi
   uvicorn
   requests

4. **Execute o servidor:**
   ```sh
   uvicorn main:app --reload

5. **Abra o front-end:**
   ```sh
   Abra o arquivo static/index.html no seu navegador.

8. **Acesse a documentação interativa da API (Swagger):**
    ```sh
    http://localhost:8000/docs

**DESENVOLVEDORES**
- Kauê Pastori Teixeira
- Nicolas Nogueira Boni
- Felipe Bressane
