from flask import Flask, render_template, request
import requests

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
        else:
            error = f"Não foi possível encontrar repositórios para o usuário {username}."

    return render_template("index.html", repos=repos, error=error)

if __name__ == "__main__":
    app.run(debug=True)
