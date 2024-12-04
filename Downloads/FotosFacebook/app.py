"""
from flask import Flask, render_template, request, send_file
import os
import requests

app = Flask(__name__)

# Caminho para salvar as imagens
DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Função para baixar fotos do Facebook
def download_facebook_photos(profile_url, access_token):
    profile_id = extract_profile_id(profile_url)
    if not profile_id:
        return None
    
    url = f'https://graph.facebook.com/{profile_id}/photos?type=uploaded&access_token={access_token}'
    response = requests.get(url)
    
    if response.status_code == 200:
        photos = response.json().get('data', [])
        filenames = []
        
        for photo in photos:
            photo_url = photo['images'][0]['source']  # URL da imagem
            filename = os.path.join(DOWNLOAD_FOLDER, f"{photo['id']}.jpg")
            img_data = requests.get(photo_url).content
            with open(filename, 'wb') as f:
                f.write(img_data)
            filenames.append(filename)
        
        return filenames
    else:
        return None

# Função para extrair o ID do perfil a partir da URL do Facebook
def extract_profile_id(url):
    # Aqui você pode usar uma regex ou lógica mais robusta para extrair o ID do perfil
    # Supondo que a URL seja do tipo 'facebook.com/{id_do_perfil}'
    if 'facebook.com' in url:
        parts = url.strip('/').split('/')
        return parts[-1]
    return None

@app.route('/download', methods=['POST'])
def download():
    profile_url = request.form['profile_url']
    access_token = request.form['access_token']
    
    # Baixando as fotos
    files = download_facebook_photos(profile_url, access_token)
    
    if files:
        # Compactar as fotos ou enviar como zip
        # Para simplificação, vamos apenas enviar o primeiro arquivo baixado
        return send_file(files[0], as_attachment=True)
    else:
        return 'Erro ao baixar as fotos ou perfil não encontrado.'

if __name__ == '__main__':
    app.run(debug=True)
"""
import os
import requests

# Função para obter fotos do Facebook
def obter_fotos_facebook(profile_id, access_token):
    # URL para pegar fotos de um perfil do Facebook
    url = f'https://graph.facebook.com/{profile_id}/photos?type=uploaded&access_token={access_token}'
    
    # Envia uma requisição GET para a Graph API
    response = requests.get(url)
    
    # Verifica se a resposta foi bem-sucedida
    if response.status_code == 200:
        # Retorna os dados JSON com as fotos
        return response.json()
    else:
        # Retorna um erro caso a requisição falhe
        return f"Erro: {response.status_code}, {response.text}"

# Função para baixar imagens do Facebook
def baixar_imagens(fotos):
    # Cria um diretório para salvar as imagens
    if not os.path.exists('fotos_facebook'):
        os.makedirs('fotos_facebook')

    # Para cada foto retornada
    for foto in fotos['data']:
        for imagem in foto['images']:
            # Obtém o link da imagem
            url_imagem = imagem['source']
            
            # Nome do arquivo da imagem (baseado no ID da foto)
            nome_arquivo = f"fotos_facebook/{foto['id']}.jpg"
            
            # Baixa a imagem
            img_response = requests.get(url_imagem)
            
            if img_response.status_code == 200:
                with open(nome_arquivo, 'wb') as f:
                    f.write(img_response.content)
                    print(f"Imagem salva como {nome_arquivo}")
            else:
                print(f"Erro ao baixar a imagem: {url_imagem}")

# Exemplo de uso
profile_id = 'MYlapckySXCbVqL0aGA5sz'  # Substitua com o ID ou nome do perfil
access_token = 'EAATl3ixaFNkBOzvDk0LpDDGRfVDco8oLTA8FTkCX4MYY5zlr1vXeL2a7EtfZA1cS2VGDil4idzOQWUwKEC0FVQlcdOFXSXaWBVJkWZAWop6XOFhrIzWNHs3ZCos2hmEpmGxGW5fOQZB2o2xvIGmp0u1ZA1zh6YQsXRdBES9MbFFOnRLPiGGjv0MxEoiiviL4IiTZAW6CohGYZCq8gJZCNZBMZD'  # Substitua com seu token de acesso

# Chama a função para obter as fotos
fotos = obter_fotos_facebook(profile_id, access_token)

# Baixa as imagens
if isinstance(fotos, dict):
    baixar_imagens(fotos)
else:
    print(fotos)

