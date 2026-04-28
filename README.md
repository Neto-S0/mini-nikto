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
