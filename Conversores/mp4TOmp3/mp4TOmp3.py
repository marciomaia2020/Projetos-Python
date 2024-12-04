import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
import os

def select_files():
    # Abre uma janela para seleção de múltiplos arquivos de vídeo
    filepaths = filedialog.askopenfilenames(
        title="Selecione arquivos de vídeo",
        filetypes=[("Vídeos", "*.mp4 *.avi *.mov *.mkv *.flv")]
    )
    if filepaths:
        extract_audio(filepaths)
    else:
        messagebox.showinfo("Aviso", "Nenhum arquivo foi selecionado!")

def extract_audio(filepaths):
    # Obtém o caminho da pasta Downloads
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    
    # Verifica se a pasta Downloads existe
    if not os.path.exists(downloads_folder):
        messagebox.showerror("Erro", "A pasta Downloads não foi encontrada!")
        return
    
    for filepath in filepaths:
        try:
            # Carrega o vídeo e extrai o áudio
            video_clip = VideoFileClip(filepath)
            audio = video_clip.audio

            # Define o nome de saída na pasta Downloads
            output_filename = os.path.basename(os.path.splitext(filepath)[0]) + ".mp3"
            output_path = os.path.join(downloads_folder, output_filename)

            # Salva o áudio em .mp3
            messagebox.showinfo("Processando", f"Extraindo áudio de: {filepath}\nPor favor, aguarde...")
            audio.write_audiofile(output_path)
            audio.close()
            video_clip.close()

            # Informa ao usuário que o áudio foi extraído
            messagebox.showinfo("Sucesso", f"Áudio extraído com sucesso!\nSalvo em: {output_path}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar o arquivo {filepath}:\n{e}")

# Criação da interface gráfica com tkinter
root = tk.Tk()
root.title("Extrator de Áudio - Vídeo para MP3")
root.geometry("400x150")
root.resizable(False, False)

# Título explicativo
label = tk.Label(root, text="Selecione arquivos de vídeo para extrair o áudio como MP3", wraplength=380, justify="center")
label.pack(pady=10)

# Botão para selecionar arquivos de vídeo
select_button = tk.Button(root, text="Selecionar Vídeos", command=select_files, width=20, height=2)
select_button.pack(pady=20)

# Inicia a interface
root.mainloop()
