import os
from flask import Flask, render_template, request, send_file
from rembg import remove
from werkzeug.utils import secure_filename
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Configuração para uploads
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Função para verificar extensões permitidas
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para remover fundo da imagem
@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return "No file part", 400
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Processar a imagem para remover o fundo
        with open(file_path, 'rb') as input_file:
            input_image = input_file.read()
            output_image = remove(input_image)
            
            # Convertendo para JPG
            img = Image.open(BytesIO(output_image))
            img = img.convert('RGB')  # Convertendo para RGB (necessário para JPG)
            
            # Salvando a imagem processada em um BytesIO em formato JPEG
            output_image_io = BytesIO()
            img.save(output_image_io, format='JPEG')
            output_image_io.seek(0)  # Resetar o ponteiro do arquivo de imagem

            return send_file(output_image_io, mimetype='image/jpeg', as_attachment=True, download_name='imagem-processada.jpg')
    else:
        return "Invalid file format", 400

if __name__ == '__main__':
    app.run(debug=True)
