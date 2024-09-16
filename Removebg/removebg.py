from flask import Flask, render_template, request, jsonify, send_file
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para remover o fundo da imagem
@app.route('/remove-bg', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({"error": "Nenhuma imagem enviada!"}), 400

    image_file = request.files['image']
    
    try:
        # Carregar a imagem
        img = Image.open(image_file.stream)
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        # Remover o fundo
        result = remove(img_bytes.getvalue())  # Utilizando o rembg para remover o fundo
        
        # Criar um objeto BytesIO para a imagem processada
        img_io = io.BytesIO(result)
        img_io.seek(0)
        
        # Retornar a imagem sem fundo
        return send_file(img_io, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": f"Erro ao processar a imagem: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
