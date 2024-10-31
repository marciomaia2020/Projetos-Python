from pytube import YouTube

def baixar_video(url, caminho='videos/'):
    try:
        # Cria um objeto YouTube com a URL fornecida
        yt = YouTube(url)
        
        try:
            # Tenta acessar informações sobre o vídeo
            print(f'Título: {yt.title}')
            print(f'Tamanho: {yt.length / 60:.2f} minutos')
        except Exception:
            print("Não foi possível acessar o título ou detalhes do vídeo.")

        # Seleciona a melhor resolução disponível para download
        stream = yt.streams.get_highest_resolution()

        # Faz o download para o diretório especificado
        print('Baixando...')
        stream.download(output_path=caminho)
        print('Download concluído!')
    
    except Exception as e:
        print(f'Ocorreu um erro ao tentar baixar o vídeo: {e}')

# Exemplo de uso
url_video = input('Informe a URL do vídeo do YouTube: ')
baixar_video(url_video)


