import yt_dlp
import tkinter as tk
from tkinter import messagebox
import os

# Caminho onde os vídeos serão salvos
# caminho_download = r"C:\Users\Marcio Fernando Maia\Videos\Captures"

# Determinar o caminho da pasta Downloads do usuário
caminho_download = os.path.join(os.path.expanduser("~"), "Downloads")

# Configurações do yt-dlp para baixar somente um formato completo
ydl_opts = {
    'outtmpl': f'{caminho_download}/%(title)s.%(ext)s',
    'format': 'best[ext=mp4]',  # Baixar o melhor formato mp4 disponível
    'noplaylist': True,  # Para evitar o download de playlists inteiras
}

def baixar_videos(urls):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                ydl.download([url])
                print(f"Download de vídeo concluído para URL: {url}")
            except Exception as e:
                print(f"Ocorreu um erro ao tentar baixar o vídeo: {url}. Erro: {e}")

# Interface Tkinter para entrada de URLs
root = tk.Tk()

# Título e configuração da janela
root.title("Download de Vídeos do YouTube")
root.geometry("600x400")  # Janela maior (600x400)

# Título para o campo de entrada com fonte maior (semelhante ao h1)
label = tk.Label(root, 
                 text="Insira as URLs dos vídeos separados por espaço ou nova linha", 
                 font=("Helvetica", 13, "bold"))  # Fonte maior e em negrito
label.pack(pady=20)  # Adiciona um pouco de espaçamento entre o título e a caixa de texto

# Campo de entrada maior
input_text = tk.Text(root, height=10, width=50)  # Aumentando a área de entrada (10 linhas, 50 colunas)
input_text.pack(pady=10)

# Função para baixar vídeos
def iniciar_download():
    urls = input_text.get("1.0", "end-1c").strip().splitlines()  # Captura as URLs e separa por linha
    urls = [url.strip() for url in urls if url.strip()]  # Limpa espaços extras

    if urls:
        baixar_videos(urls)
    else:
        messagebox.showinfo("Informação", "Nenhuma URL válida foi inserida.")

# Botão para iniciar o download
download_button = tk.Button(root, text="Baixar Vídeos", command=iniciar_download)
download_button.pack(pady=20)

# Manter a janela aberta até o usuário fechá-la
root.mainloop()
