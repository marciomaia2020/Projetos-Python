"""
from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    repos = []
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)

        if response.status_code == 200:
            repos = response.json()
            # Formatar as datas
            for repo in repos:
                repo['created_at'] = datetime.strptime(repo['created_at'], "%Y-%m-%dT%H:%M:%SZ")
                repo['updated_at'] = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
        else:
            error = f"Não foi possível encontrar repositórios para o usuário {username}."

    return render_template("index.html", repos=repos, error=error)

if __name__ == "__main__":
    app.run(debug=True)
"""

from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    repos = []
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        base_url = f"https://api.github.com/users/{username}/repos"
        page = 1

        while True:
            url = f"{base_url}?per_page=100&page={page}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if not data:  # Se não houver mais repositórios, encerra o loop
                    break
                repos.extend(data)
                page += 1
            else:
                error = f"Não foi possível encontrar repositórios para o usuário {username}."
                break

        # Formatar as datas
        for repo in repos:
            repo['created_at'] = datetime.strptime(repo['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            repo['updated_at'] = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")

    return render_template("index.html", repos=repos, error=error)

if __name__ == "__main__":
    app.run(debug=True)


"""
Nota
Certifique-se de não exceder os limites de taxa da API do GitHub (5000 solicitações por hora para usuários autenticados). Para aumentar esse limite, você pode autenticar-se utilizando um token de acesso pessoal.
Se necessário, implemente autenticação na API com headers, como mostrado abaixo:
python
Copy code
headers = {"Authorization": "token SEU_TOKEN_AQUI"}
response = requests.get(url, headers=headers)

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
"""
"""
from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

# Opcional: Adicione seu token de acesso pessoal aqui
GITHUB_TOKEN = "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"

@app.route("/", methods=["GET", "POST"])
def index():
    repos = []
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        base_url = f"https://api.github.com/users/{username}/repos"
        headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
        page = 1

        while True:
            url = f"{base_url}?per_page=100&page={page}"
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                if not data:  # Se não houver mais repositórios, encerra o loop
                    break
                repos.extend(data)
                page += 1
            else:
                error = f"Não foi possível encontrar repositórios para o usuário {username}."
                break

        # Formatar as datas
        for repo in repos:
            repo['created_at'] = datetime.strptime(repo['created_at'], "%Y-%m-%dT%H:%M:%SZ")
            repo['updated_at'] = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")

    return render_template("index.html", repos=repos, error=error)

if __name__ == "__main__":
    app.run(debug=True)
"""