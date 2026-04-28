# 🔎 Mini Nikto - Lightweight Web Scanner in Python

A lightweight web scanner inspired by Nikto, built to discover common endpoints and improve web reconnaissance skills.

---

## 🚀 Features

* Scan for common paths (e.g. `/admin`, `/login`, `/dashboard`)
* Detect HTTP status codes (200, 403, 404)
* Custom wordlist support
* Fast and simple CLI execution

---

## 🛠️ Technologies Used

* Python 3
* requests

---

## 📂 Project Structure

```
mini-nikto/
├── main.py
├── core/
│   ├── scanner.py
│   └── utils.py
├── wordlists/
│   └── wordlist.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Neto-S0/mini-nikto.git
cd mini-nikto
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the scanner:

```bash
python main.py
```

Enter the target URL when prompted:

```
http://localhost:8000
```

---

## 📊 Example Output

```
[200] http://localhost:8000/dashboard
[404] http://localhost:8000/admin
[403] http://localhost:8000/login
```

---

## 🧠 How It Works

The scanner reads a wordlist and sends HTTP requests to each endpoint, identifying valid paths based on response status codes.

---

## 🛡️ Disclaimer

This project is intended for educational purposes only.
Do not use against targets without proper authorization.

---

## 📚 Future Improvements

* Add threading (faster scanning)
* Filter results by status code
* Export results to file
* Add CLI arguments (e.g. `--target`)
* Improve error handling

---

## 👨‍💻 Author

* Neto
* GitHub: https://github.com/Neto-S0

---



## 🇧🇷 Versão em Português

# 🔎 Mini Nikto - Scanner Web Leve em Python

Um scanner web leve inspirado no Nikto, desenvolvido para descobrir endpoints comuns e aprimorar habilidades de reconhecimento em aplicações web.

---

## 🚀 Funcionalidades

* Varredura de caminhos comuns (ex: `/admin`, `/login`, `/dashboard`)
* Detecção de códigos de status HTTP (200, 403, 404)
* Suporte a wordlist personalizada
* Execução simples via terminal (CLI)

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* requests

---

## 📂 Estrutura do Projeto

```id="pt-struct"
mini-nikto/
├── main.py
├── core/
│   ├── scanner.py
│   └── utils.py
├── wordlists/
│   └── wordlist.txt
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalação

Clone o repositório:

```bash id="pt-clone"
git clone https://github.com/Neto-S0/mini-nikto.git
cd mini-nikto
```

Instale as dependências:

```bash id="pt-install"
pip install -r requirements.txt
```

---

## ▶️ Como Usar

Execute o scanner:

```bash id="pt-run"
python main.py
```

Informe a URL alvo quando solicitado:

```id="pt-target"
http://localhost:8000
```

---

## 📊 Exemplo de Saída

```id="pt-output"
[200] http://localhost:8000/dashboard
[404] http://localhost:8000/admin
[403] http://localhost:8000/login
```

---

## 🧠 Como Funciona

O scanner lê uma wordlist e envia requisições HTTP para cada endpoint, identificando caminhos válidos com base nos códigos de resposta.

---

## 🛡️ Aviso

Este projeto é destinado apenas para fins educacionais.
Não utilize contra sistemas sem autorização.

---

## 📚 Melhorias Futuras

* Adicionar threads (scan mais rápido)
* Filtrar resultados por código de status
* Exportar resultados para arquivo
* Adicionar argumentos CLI (ex: `--target`)
* Melhorar tratamento de erros

---

## 👨‍💻 Autor

* https://github.com/Neto-S0

