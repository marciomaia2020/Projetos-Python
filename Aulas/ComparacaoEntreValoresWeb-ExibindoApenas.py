from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    a = 10  # Exemplo
    b = 5   # Exemplo
    mensagem = f"{a} é maior que {b}" if a > b else f"{b} é maior que {a}"
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="pt">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Comparação de Números</title>
        </head>
        <body>
            <h1>Comparação de Números</h1>
            <p>{{ mensagem }}</p>
        </body>
        </html>
    ''', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)
