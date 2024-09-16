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
