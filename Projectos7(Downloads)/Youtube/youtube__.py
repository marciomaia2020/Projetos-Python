import yt_dlp
import tkinter as tk
from tkinter import simpledialog, messagebox

# Caminho onde os vídeos serão salvos
caminho_download = r"C:\Users\Marcio Fernando Maia\Videos\Captures"

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
root.withdraw()
root.title("Download de Vídeos do YouTube")
root.geometry("500x300")

input_text = simpledialog.askstring("URLs dos vídeos", "Insira as URLs dos vídeos separadas por espaço ou nova linha:")
if input_text:
    urls = input_text.strip().split()
    baixar_videos(urls)
else:
    messagebox.showinfo("Informação", "Nenhuma URL inserida.")


