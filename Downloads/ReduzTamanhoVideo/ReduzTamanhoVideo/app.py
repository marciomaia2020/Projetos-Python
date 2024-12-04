""" SEM INTERFACE GRAFICA (TÉCNICO)

import os
from moviepy.editor import VideoFileClip

def comprimir_video(input_filename, output_filename, tamanho_maximo_mb=16):
    # Caminho da pasta Downloads do usuário atual
    pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    
    # Caminho completo do arquivo de entrada e saída
    input_path = os.path.join(pasta_downloads, input_filename)
    output_path = os.path.join(pasta_downloads, output_filename)
    
    # Verifica se o arquivo de entrada existe
    if not os.path.exists(input_path):
        print(f"Erro: O arquivo '{input_path}' não foi encontrado.")
        return
    
    # Calcula o tamanho do vídeo original
    tamanho_video_original = os.path.getsize(input_path) / (1024 * 1024)  # Tamanho em MB
    print(f"Tamanho original do vídeo: {tamanho_video_original:.2f} MB")
    
    # Carrega o vídeo
    video = VideoFileClip(input_path)
    
    # Se o tamanho já estiver abaixo do limite, apenas salva novamente
    if tamanho_video_original <= tamanho_maximo_mb:
        print(f"O vídeo já está abaixo de {tamanho_maximo_mb} MB.")
        video.write_videofile(output_path, codec="libx264", audio_codec="aac")
        return
    
    # Reduz a resolução do vídeo pela metade
    nova_resolucao = (int(video.size[0] / 2), int(video.size[1] / 2))
    video_reduzido = video.resize(newsize=nova_resolucao)
    
    # Exporta o vídeo comprimido
    video_reduzido.write_videofile(output_path, codec="libx264", audio_codec="aac")
    
    # Calcula o tamanho do vídeo comprimido
    tamanho_video_comprimido = os.path.getsize(output_path) / (1024 * 1024)  # Tamanho em MB
    print(f"Tamanho do vídeo comprimido: {tamanho_video_comprimido:.2f} MB")
    print(f"Vídeo comprimido salvo em: {output_path}")

# Nome do vídeo original e do vídeo comprimido
input_video = "Just Fucking Vol 2.mp4"
output_video = "Just Fucking Vol 2 Comprimido.mp4"

# Comprime o vídeo
comprimir_video(input_video, output_video)
"""

"""


import os
from tkinter import Tk, filedialog
from moviepy.editor import VideoFileClip

def comprimir_video(input_path, output_filename, tamanho_maximo_mb=16):
    # Verifica se o arquivo de entrada existe
    if not os.path.exists(input_path):
        print(f"Erro: O arquivo '{input_path}' não foi encontrado.")
        return
    
    # Caminho da pasta Downloads do usuário atual
    pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    output_path = os.path.join(pasta_downloads, output_filename)
    
    # Calcula o tamanho do vídeo original
    tamanho_video_original = os.path.getsize(input_path) / (1024 * 1024)  # Tamanho em MB
    print(f"Tamanho original do vídeo: {tamanho_video_original:.2f} MB")
    
    # Carrega o vídeo
    video = VideoFileClip(input_path)
    
    # Se o tamanho já estiver abaixo do limite, apenas salva novamente
    if tamanho_video_original <= tamanho_maximo_mb:
        print(f"O vídeo já está abaixo de {tamanho_maximo_mb} MB.")
        video.write_videofile(output_path, codec="libx264", audio_codec="aac")
        return
    
    # Reduz a resolução do vídeo pela metade
    nova_resolucao = (int(video.size[0] / 2), int(video.size[1] / 2))
    video_reduzido = video.resize(newsize=nova_resolucao)
    
    # Exporta o vídeo comprimido
    video_reduzido.write_videofile(output_path, codec="libx264", audio_codec="aac")
    
    # Calcula o tamanho do vídeo comprimido
    tamanho_video_comprimido = os.path.getsize(output_path) / (1024 * 1024)  # Tamanho em MB
    print(f"Tamanho do vídeo comprimido: {tamanho_video_comprimido:.2f} MB")
    print(f"Vídeo comprimido salvo em: {output_path}")

# Função para selecionar o arquivo de vídeo
def selecionar_video():
    # Cria uma janela de diálogo para seleção de arquivos
    root = Tk()
    root.withdraw()  # Oculta a janela principal do tkinter
    
    # Permite selecionar arquivos de vídeo
    input_path = filedialog.askopenfilename(
        title="Selecione um vídeo para comprimir",
        filetypes=[("Arquivos de Vídeo", "*.mp4;*.mov;*.avi;*.mkv")]
    )
    
    # Sai se o usuário não selecionar nenhum arquivo
    if not input_path:
        print("Nenhum arquivo selecionado.")
        return
    
    # Nome do arquivo de saída
    output_filename = "Video_Comprimido.mp4"
    
    # Chama a função de compressão
    comprimir_video(input_path, output_filename)

# Seleciona o vídeo para compressão
selecionar_video()
"""


"""
COM INTERFACE GRAFICA POREM NÃO STISFATÓRIO COMO FALTA DE FEEDBACK

import os
from tkinter import Tk, Label
from tkinterdnd2 import TkinterDnD, DND_FILES
from moviepy.editor import VideoFileClip

def comprimir_video(input_path, output_filename, tamanho_maximo_mb=16):
    # Verifica se o arquivo de entrada existe
    if not os.path.exists(input_path):
        print(f"Erro: O arquivo '{input_path}' não foi encontrado.")
        return
    
    # Caminho da pasta Downloads do usuário atual
    pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    output_path = os.path.join(pasta_downloads, output_filename)
    
    # Calcula o tamanho do vídeo original
    tamanho_video_original = os.path.getsize(input_path) / (1024 * 1024)  # Tamanho em MB
    print(f"Tamanho original do vídeo: {tamanho_video_original:.2f} MB")
    
    # Carrega o vídeo
    video = VideoFileClip(input_path)
    
    # Se o tamanho já estiver abaixo do limite, apenas salva novamente
    if tamanho_video_original <= tamanho_maximo_mb:
        print(f"O vídeo já está abaixo de {tamanho_maximo_mb} MB.")
        video.write_videofile(output_path, codec="libx264", audio_codec="aac")
        return
    
    # Reduz a resolução do vídeo pela metade
    nova_resolucao = (int(video.size[0] / 2), int(video.size[1] / 2))
    video_reduzido = video.resize(newsize=nova_resolucao)
    
    # Exporta o vídeo comprimido
    video_reduzido.write_videofile(output_path, codec="libx264", audio_codec="aac")
    
    # Calcula o tamanho do vídeo comprimido
    tamanho_video_comprimido = os.path.getsize(output_path) / (1024 * 1024)  # Tamanho em MB
    print(f"Tamanho do vídeo comprimido: {tamanho_video_comprimido:.2f} MB")
    print(f"Vídeo comprimido salvo em: {output_path}")

def iniciar_drag_and_drop():
    def drop(event):
        # Obtém o caminho do arquivo arrastado
        input_path = event.data.strip("{}")
        if not os.path.isfile(input_path):
            label.config(text="Erro: Arraste um arquivo válido!")
            return
        
        # Nome do arquivo de saída
        output_filename = "Video_Comprimido.mp4"
        
        # Chama a função de compressão
        comprimir_video(input_path, output_filename)
        label.config(text="Compressão concluída! Verifique a pasta Downloads.")
    
    # Configura a interface gráfica
    root = TkinterDnD.Tk()
    root.title("Arraste o Vídeo Aqui")
    root.geometry("400x200")
    root.resizable(False, False)
    
    # Rótulo de instrução
    label = Label(root, text="Arraste e solte o arquivo de vídeo aqui", bg="lightgray", fg="black", font=("Arial", 14))
    label.pack(expand=True, fill="both")
    
    # Configuração do suporte a DnD
    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", drop)
    
    root.mainloop()

# Inicia o programa
iniciar_drag_and_drop()
"""

""" COM INTERFACE GRÁFICA LEGAL E FUNCIONAL (Estou testanto o código abaixo somente para informar 
o usuário que o video foi salvo na pasta DOWNLOAD) em relação ao nome do video está ok..
import os
from tkinter import Tk, Label
from tkinterdnd2 import TkinterDnD, DND_FILES
from moviepy.editor import VideoFileClip

def comprimir_video(input_path, output_path, tamanho_maximo_mb=16):
    # Calcula o tamanho do vídeo original
    tamanho_video_original = os.path.getsize(input_path) / (1024 * 1024)  # Tamanho em MB
    print(f"Tamanho original do vídeo: {tamanho_video_original:.2f} MB")
    
    # Carrega o vídeo
    video = VideoFileClip(input_path)
    
    # Se o tamanho já estiver abaixo do limite, apenas salva novamente
    if tamanho_video_original <= tamanho_maximo_mb:
        print(f"O vídeo já está abaixo de {tamanho_maximo_mb} MB.")
        video.write_videofile(output_path, codec="libx264", audio_codec="aac")
        return
    
    # Reduz a resolução do vídeo pela metade
    nova_resolucao = (int(video.size[0] / 2), int(video.size[1] / 2))
    video_reduzido = video.resize(newsize=nova_resolucao)
    
    # Exporta o vídeo comprimido
    video_reduzido.write_videofile(output_path, codec="libx264", audio_codec="aac")
    
    # Calcula o tamanho do vídeo comprimido
    tamanho_video_comprimido = os.path.getsize(output_path) / (1024 * 1024)  # Tamanho em MB
    print(f"Tamanho do vídeo comprimido: {tamanho_video_comprimido:.2f} MB")

def iniciar_drag_and_drop():
    def drop(event):
        # Obtém os caminhos dos arquivos arrastados
        input_paths = event.data.strip("{}").split("} {")
        
        # Caminho da pasta Downloads
        pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        
        # Processa cada arquivo
        for input_path in input_paths:
            if not os.path.isfile(input_path):
                status_label.config(text="Erro: Um ou mais arquivos inválidos foram arrastados!")
                return
            
            # Nome do arquivo de saída
            input_filename = os.path.basename(input_path)
            base_name, ext = os.path.splitext(input_filename)
            output_filename = f"{base_name}_Comprimido{ext}"
            output_path = os.path.join(pasta_downloads, output_filename)
            
            # Exibe o nome do arquivo que está sendo processado
            status_label.config(text=f"Processando: {input_filename}")
            root.update_idletasks()
            
            try:
                comprimir_video(input_path, output_path)
                print(f"Vídeo comprimido salvo em: {output_path}")
                status_label.config(text=f"Concluído: {input_filename}")
            except Exception as e:
                print(f"Erro ao processar '{input_filename}': {e}")
                status_label.config(text=f"Erro ao processar: {input_filename}")
    
    # Configura a interface gráfica
    root = TkinterDnD.Tk()
    root.title("Compressor de Vídeos - Arraste e Solte")
    root.geometry("500x300")
    root.resizable(False, False)
    
    # Rótulo de instrução
    instruction_label = Label(root, text="Arraste e solte os arquivos de vídeo aqui", bg="lightblue", fg="black", font=("Arial", 14))
    instruction_label.pack(pady=20, fill="x")
    
    # Rótulo de status
    status_label = Label(root, text="Aguardando vídeos...", bg="white", fg="black", font=("Arial", 12))
    status_label.pack(pady=10, fill="x")
    
    # Configuração do suporte a DnD
    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", drop)
    
    root.mainloop()

# Inicia o programa
iniciar_drag_and_drop()
"""
import os
from tkinter import Tk, Label
from tkinterdnd2 import TkinterDnD, DND_FILES
from moviepy.editor import VideoFileClip

def comprimir_video(input_path, output_path, tamanho_maximo_mb=16):
    # Calcula o tamanho do vídeo original
    tamanho_video_original = os.path.getsize(input_path) / (1024 * 1024)  # Tamanho em MB
    print(f"Tamanho original do vídeo: {tamanho_video_original:.2f} MB")
    
    # Carrega o vídeo
    video = VideoFileClip(input_path)
    
    # Se o tamanho já estiver abaixo do limite, apenas salva novamente
    if tamanho_video_original <= tamanho_maximo_mb:
        print(f"O vídeo já está abaixo de {tamanho_maximo_mb} MB.")
        video.write_videofile(output_path, codec="libx264", audio_codec="aac")
        return
    
    # Reduz a resolução do vídeo pela metade
    nova_resolucao = (int(video.size[0] / 2), int(video.size[1] / 2))
    video_reduzido = video.resize(newsize=nova_resolucao)
    
    # Exporta o vídeo comprimido
    video_reduzido.write_videofile(output_path, codec="libx264", audio_codec="aac")
    
    # Calcula o tamanho do vídeo comprimido
    tamanho_video_comprimido = os.path.getsize(output_path) / (1024 * 1024)  # Tamanho em MB
    print(f"Tamanho do vídeo comprimido: {tamanho_video_comprimido:.2f} MB")

def iniciar_drag_and_drop():
    def drop(event):
        # Obtém os caminhos dos arquivos arrastados
        input_paths = event.data.strip("{}").split("} {")
        
        # Caminho da pasta Downloads
        pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        
        # Processa cada arquivo
        for input_path in input_paths:
            if not os.path.isfile(input_path):
                status_label.config(text="Erro: Um ou mais arquivos inválidos foram arrastados!")
                return
            
            # Nome do arquivo de saída
            input_filename = os.path.basename(input_path)
            base_name, ext = os.path.splitext(input_filename)
            output_filename = f"{base_name}_Comprimido{ext}"
            output_path = os.path.join(pasta_downloads, output_filename)
            
            # Exibe o nome do arquivo que está sendo processado
            status_label.config(text=f"Processando: {input_filename}")
            root.update_idletasks()
            
            try:
                comprimir_video(input_path, output_path)
                print(f"Vídeo comprimido salvo em: {output_path}")
                status_label.config(
                    text=f"Concluído: {input_filename}\nSalvo em: Downloads como {output_filename}"
                )
            except Exception as e:
                print(f"Erro ao processar '{input_filename}': {e}")
                status_label.config(text=f"Erro ao processar: {input_filename}")
    
    # Configura a interface gráfica
    root = TkinterDnD.Tk()
    root.title("Compressor de Vídeos - Arraste e Solte")
    root.geometry("500x300")
    root.resizable(False, False)
    
    # Rótulo de instrução
    instruction_label = Label(root, text="Arraste e solte os arquivos de vídeo aqui", bg="lightblue", fg="black", font=("Arial", 14))
    instruction_label.pack(pady=20, fill="x")
    
    # Rótulo de status
    status_label = Label(root, text="Aguardando vídeos...", bg="white", fg="black", font=("Arial", 12))
    status_label.pack(pady=10, fill="x")
    
    # Configuração do suporte a DnD
    root.drop_target_register(DND_FILES)
    root.dnd_bind("<<Drop>>", drop)
    
    root.mainloop()

# Inicia o programa
iniciar_drag_and_drop()
