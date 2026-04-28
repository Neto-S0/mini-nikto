from utils import load_wordlist
from scanner import scan_url

target = input("Alvo (ex: http://127.0.0.1): ")

paths = load_wordlist("wordlist.txt")

for path in paths:
    # evita // na URL
    url = f"{target.rstrip('/')}/{path}"

    status = scan_url(url)

    # só entra se não deu erro (None)
    if status is not None:
        print(f"[{status}] {url}")

        # salva apenas páginas que existem
        if status == 200:
            with open("report.txt", "a") as f:
                f.write(f"[200] {url}\n")