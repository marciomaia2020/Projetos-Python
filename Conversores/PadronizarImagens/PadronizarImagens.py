
#MELHORAR ESTE CÓDIGO ELE ACEITA APENAS UMA IMAGEM POR VEZ...
'''
import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk

def ajustar_imagem(caminho_imagem, nova_largura, nova_altura):
    try:
        # Define o caminho de saída com o novo nome
        caminho_diretorio, nome_arquivo = os.path.split(caminho_imagem)
        nome_base, extensao = os.path.splitext(nome_arquivo)
        caminho_saida = os.path.join(caminho_diretorio, f"{nome_base}_Redimensionada{extensao}")
        
        # Abre a imagem
        imagem = Image.open(caminho_imagem)
        
        # Redimensiona a imagem
        imagem_ajustada = imagem.resize((nova_largura, nova_altura))
        
        # Salva a imagem ajustada
        imagem_ajustada.save(caminho_saida)
        
        messagebox.showinfo("Sucesso", f"Imagem salva em:\n{caminho_saida}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao redimensionar a imagem: {e}")

def exibir_imagem(caminho):
    try:
        imagem_selecionada = Image.open(caminho)
        imagem_selecionada.thumbnail((300, 300))  # Ajustar para visualização
        imagem_exibida = ImageTk.PhotoImage(imagem_selecionada)
        label_imagem.configure(image=imagem_exibida)
        label_imagem.image = imagem_exibida
        label_imagem.text = ""
    except Exception as e:
        label_imagem.configure(text="Erro ao carregar imagem")
        print(f"Erro ao carregar imagem: {e}")

def handle_drag_and_drop(event):
    global caminho_imagem
    
    # Captura o caminho e limpa caracteres extras
    caminho_imagem = event.data.strip()
    
    # Remove chaves ({ e }) se presentes
    if caminho_imagem.startswith("{") and caminho_imagem.endswith("}"):
        caminho_imagem = caminho_imagem[1:-1]
    
    # Verifica se o arquivo realmente existe
    if os.path.exists(caminho_imagem):
        exibir_imagem(caminho_imagem)
    else:
        messagebox.showerror("Erro", f"O caminho da imagem não é válido:\n{caminho_imagem}")

def selecionar_imagem():
    global caminho_imagem
    caminho_imagem = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if caminho_imagem:
        exibir_imagem(caminho_imagem)

def processar_imagem():
    if not caminho_imagem:
        messagebox.showwarning("Aviso", "Nenhuma imagem selecionada!")
        return
    
    try:
        nova_largura = int(entry_largura.get())
        nova_altura = int(entry_altura.get())
        ajustar_imagem(caminho_imagem, nova_largura, nova_altura)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para largura e altura.")

# Interface gráfica
app = TkinterDnD.Tk()  # Usa TkinterDnD para suportar arrastar e soltar
app.title("Redimensionador de Imagens")
app.geometry("400x500")

label_info = Label(app, text="Arraste uma imagem ou clique no botão para selecionar:", wraplength=380)
label_info.pack(pady=10)

# Exibição da imagem
label_imagem = Label(app, text="Nenhuma imagem selecionada", width=40, height=10, relief="solid")
label_imagem.pack(pady=10)

# Botão para selecionar imagem
btn_selecionar = Button(app, text="Selecionar Imagem", command=selecionar_imagem)
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

# Botão para processar imagem
btn_processar = Button(app, text="Redimensionar e Salvar", command=processar_imagem)
btn_processar.pack(pady=20)

# Habilitar arrastar e soltar
app.drop_target_register(DND_FILES)
app.dnd_bind('<<Drop>>', handle_drag_and_drop)

app.mainloop()
'''


#MELHORAR ESTE CÓDIGO ELE ACEITA APENAS UMA IMAGEM POR VEZ...
#AQUI É O MESMO CÓDIGO DO DE CIMA POREM ESTOU VENDO SOMENTE A QUESTÃO
#DAS EXTENSÕES DE IMAGENS.. ACIDIONANDO

'''
import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk

def ajustar_imagem(caminho_imagem, nova_largura, nova_altura):
    try:
        # Define o caminho de saída com o novo nome
        caminho_diretorio, nome_arquivo = os.path.split(caminho_imagem)
        nome_base, extensao = os.path.splitext(nome_arquivo)
        caminho_saida = os.path.join(caminho_diretorio, f"{nome_base}_Redimensionada{extensao}")
        
        # Abre a imagem
        imagem = Image.open(caminho_imagem)
        
        # Redimensiona a imagem
        imagem_ajustada = imagem.resize((nova_largura, nova_altura))
        
        # Salva a imagem ajustada
        imagem_ajustada.save(caminho_saida)
        
        messagebox.showinfo("Sucesso", f"Imagem salva em:\n{caminho_saida}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao redimensionar a imagem: {e}")

def exibir_imagem(caminho):
    try:
        imagem_selecionada = Image.open(caminho)
        imagem_selecionada.thumbnail((300, 300))  # Ajustar para visualização
        imagem_exibida = ImageTk.PhotoImage(imagem_selecionada)
        label_imagem.configure(image=imagem_exibida)
        label_imagem.image = imagem_exibida
        label_imagem.text = ""
    except Exception as e:
        label_imagem.configure(text="Erro ao carregar imagem")
        print(f"Erro ao carregar imagem: {e}")

def handle_drag_and_drop(event):
    global caminho_imagem
    
    # Captura o caminho e limpa caracteres extras
    caminho_imagem = event.data.strip()
    
    # Remove chaves ({ e }) se presentes
    if caminho_imagem.startswith("{") and caminho_imagem.endswith("}"):
        caminho_imagem = caminho_imagem[1:-1]
    
    # Verifica se o arquivo realmente existe
    if os.path.exists(caminho_imagem):
        exibir_imagem(caminho_imagem)
    else:
        messagebox.showerror("Erro", f"O caminho da imagem não é válido:\n{caminho_imagem}")

def selecionar_imagem():
    global caminho_imagem
    caminho_imagem = filedialog.askopenfilename(
        title="Selecione uma imagem",
        #filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif")]
        filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.tif *.webp *.heif *.heic *.avif *.svg")]

    )
    if caminho_imagem:
        exibir_imagem(caminho_imagem)

def processar_imagem():
    if not caminho_imagem:
        messagebox.showwarning("Aviso", "Nenhuma imagem selecionada!")
        return
    
    try:
        nova_largura = int(entry_largura.get())
        nova_altura = int(entry_altura.get())
        ajustar_imagem(caminho_imagem, nova_largura, nova_altura)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para largura e altura.")

# Interface gráfica
app = TkinterDnD.Tk()  # Usa TkinterDnD para suportar arrastar e soltar
app.title("Redimensionador de Imagens")
app.geometry("400x500")

label_info = Label(app, text="Arraste uma imagem ou clique no botão para selecionar:", wraplength=380)
label_info.pack(pady=10)

# Exibição da imagem
label_imagem = Label(app, text="Nenhuma imagem selecionada", width=40, height=10, relief="solid")
label_imagem.pack(pady=10)

# Botão para selecionar imagem
btn_selecionar = Button(app, text="Selecionar Imagem", command=selecionar_imagem)
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

# Botão para processar imagem
btn_processar = Button(app, text="Redimensionar e Salvar", command=processar_imagem)
btn_processar.pack(pady=20)

# Habilitar arrastar e soltar
app.drop_target_register(DND_FILES)
app.dnd_bind('<<Drop>>', handle_drag_and_drop)

app.mainloop()
'''
import os
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox, Listbox, END
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ImageTk

def ajustar_imagens(caminhos_imagens, nova_largura, nova_altura):
    for caminho_imagem in caminhos_imagens:
        try:
            # Define o caminho de saída com o novo nome
            caminho_diretorio, nome_arquivo = os.path.split(caminho_imagem)
            nome_base, extensao = os.path.splitext(nome_arquivo)
            caminho_saida = os.path.join(caminho_diretorio, f"{nome_base}_Redimensionada{extensao}")
            
            # Abre a imagem
            imagem = Image.open(caminho_imagem)
            
            # Redimensiona a imagem
            imagem_ajustada = imagem.resize((nova_largura, nova_altura))
            
            # Salva a imagem ajustada
            imagem_ajustada.save(caminho_saida)
            
            messagebox.showinfo("Sucesso", f"Imagem salva em:\n{caminho_saida}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao redimensionar a imagem {caminho_imagem}:\n{e}")

def exibir_imagens(caminhos):
    listbox_imagens.delete(0, END)  # Limpa a lista atual
    for caminho in caminhos:
        listbox_imagens.insert(END, caminho)

def handle_drag_and_drop(event):
    global caminhos_imagens
    caminhos_imagens = event.data.strip().split()  # Suporta múltiplos caminhos
    caminhos_imagens = [caminho.strip("{}") for caminho in caminhos_imagens]
    exibir_imagens(caminhos_imagens)

def selecionar_imagens():
    global caminhos_imagens
    caminhos_imagens = filedialog.askopenfilenames(
        title="Selecione imagens",
        filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.tif *.webp *.heif *.heic *.avif *.svg")]
    )
    if caminhos_imagens:
        exibir_imagens(caminhos_imagens)

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
