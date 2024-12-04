import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, Listbox, END
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk

def ajustar_imagens(caminhos_imagens, nova_largura, nova_altura):
    for caminho_imagem in caminhos_imagens:
        try:
            # Normaliza o caminho para garantir que as barras invertidas sejam tratadas corretamente
            caminho_imagem = os.path.normpath(caminho_imagem.strip())  # Normaliza o caminho
            
            # Verifica se o caminho é válido
            if not os.path.exists(caminho_imagem):
                raise ValueError(f"O caminho da imagem não existe: {caminho_imagem}")

            # Define o caminho de saída com o novo nome
            caminho_diretorio, nome_arquivo = os.path.split(caminho_imagem)
            nome_base, extensao = os.path.splitext(nome_arquivo)
            caminho_saida = os.path.join(caminho_diretorio, f"{nome_base}_Redimensionada{extensao}")
            
            # Abre a imagem
            imagem = Image.open(caminho_imagem)
            
            # Verifique se a imagem foi aberta corretamente
            if imagem is None:
                raise ValueError("Falha ao abrir a imagem.")
            
            # Redimensiona a imagem
            imagem_ajustada = imagem.resize((nova_largura, nova_altura))
            
            # Salva a imagem ajustada
            imagem_ajustada.save(caminho_saida)
            
            # Exibe a mensagem de sucesso
            messagebox.showinfo("Sucesso", f"Imagem salva em:\n{caminho_saida}")
        except Exception as e:
            # Exibe o erro detalhado para cada imagem com informações sobre o caminho
            messagebox.showerror("Erro", f"Erro ao redimensionar a imagem {caminho_imagem}:\n{e}")
            print(f"Erro ao processar {caminho_imagem}: {e}")

def exibir_imagens(caminhos):
    listbox_imagens.delete(0, END)  # Limpa a lista atual
    for caminho in caminhos:
        listbox_imagens.insert(END, caminho)  # Exibe o caminho da imagem sem quebras de linha

def handle_drag_and_drop(event):
    global caminhos_imagens

    # Captura os caminhos dos arquivos e remove as chaves { e } que aparecem nos caminhos arrastados
    caminhos_imagens = event.data.strip()

    # Substitui os delimitadores '}{' por uma quebra de linha
    caminhos_imagens = caminhos_imagens.replace("}{", "\n")  # Substitui a junção dos caminhos por quebra de linha
    
    # Remove as chaves extras que podem aparecer no início ou no final
    caminhos_imagens = caminhos_imagens.strip("{}")  # Remove as chaves de abertura e fechamento

    # Agora, dividimos a string em uma lista de caminhos, separando por novas linhas
    caminhos_imagens = caminhos_imagens.split("\n")  # Quebra a string em uma lista de caminhos

    # Exibe as imagens, uma por linha, sem quebras de linha ou separações erradas
    exibir_imagens(caminhos_imagens)

def selecionar_imagens():
    global caminhos_imagens
    caminhos_imagens = filedialog.askopenfilenames(
        title="Selecione imagens",
        filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.tif *.webp *.heif *.heic *.avif *.svg")]
    )
    if caminhos_imagens:
        exibir_imagens(caminhos_imagens)  # Exibe as imagens no listbox

def processar_imagens():
    if not caminhos_imagens:
        messagebox.showwarning("Aviso", "Nenhuma imagem selecionada!")
        return
    
    try:
        nova_largura = int(entry_largura.get())
        nova_altura = int(entry_altura.get())
        ajustar_imagens(caminhos_imagens, nova_largura, nova_altura)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para largura e altura.")

# Interface gráfica
app = TkinterDnD.Tk()  # Usa TkinterDnD para suportar arrastar e soltar
app.title("Redimensionador de Imagens")
app.geometry("500x600")

label_info = Label(app, text="Arraste imagens ou clique no botão para selecionar:", wraplength=480)
label_info.pack(pady=10)

# Lista de imagens
listbox_imagens = Listbox(app, height=10, width=60)
listbox_imagens.pack(pady=10)

# Botão para selecionar imagens
btn_selecionar = Button(app, text="Selecionar Imagens", command=selecionar_imagens)
btn_selecionar.pack(pady=5)

# Campos para largura e altura
label_largura = Label(app, text="Largura:")
label_largura.pack(pady=5)
entry_largura = Entry(app)
entry_largura.pack(pady=5)

label_altura = Label(app, text="Altura:")
label_altura.pack(pady=5)
entry_altura = Entry(app)
entry_altura.pack(pady=5)

# Botão para processar imagens
btn_processar = Button(app, text="Redimensionar e Salvar", command=processar_imagens)
btn_processar.pack(pady=20)

# Habilitar arrastar e soltar
app.drop_target_register(DND_FILES)
app.dnd_bind('<<Drop>>', handle_drag_and_drop)

app.mainloop()
