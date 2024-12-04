from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

class Animal:
    def __init__(self, raca, cor, patas):
        self.raca = raca
        self.cor = cor
        self.patas = patas

    def informacao(self):
        return f"Olá, a raça do cachorro é {self.raca} e sua cor é {self.cor}. Lembrando que todo cão tem {self.patas} patas!"

@app.route('/', methods=['GET', 'POST'])
def index():
    animais = []
    if request.method == 'POST':
        raca1 = request.form['raca1']
        cor1 = request.form['cor1']
        patas1 = int(request.form['patas1'])
        raca2 = request.form['raca2']
        cor2 = request.form['cor2']
        patas2 = int(request.form['patas2'])
        
        animal1 = Animal(raca1, cor1, patas1)
        animal2 = Animal(raca2, cor2, patas2)
        
        animais.append(animal1.informacao())
        animais.append(animal2.informacao())
    
    return render_template('index.html', animais=animais)

if __name__ == '__main__':
    app.run(debug=True)
