from pydub import AudioSegment
import speech_recognition as sr
from fpdf import FPDF

# Caminho do arquivo de áudio original
audio_path = r"D:\Back_up-Apire-3-A315-53-333H\Cursos\Logica_de_Programacao\audio.wav"

# Converte o arquivo MP3 para WAV
sound = AudioSegment.from_mp3(audio_path)
wav_path = audio_path.replace(".mp3", ".wav")
sound.export(wav_path, format="wav")

# Inicializando o reconhecedor de fala
recognizer = sr.Recognizer()

# Carregando o arquivo de áudio convertido
with sr.AudioFile(wav_path) as source:
    audio = recognizer.record(source)

try:
    # Transcrevendo o áudio para texto
    text = recognizer.recognize_google(audio, language="pt-BR")
    print("Transcrição: ", text)

    # Salvando a transcrição em um arquivo PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    
    # Nome do arquivo PDF
    pdf_file_path = audio_path.replace(".mp3", ".pdf")
    pdf.output(pdf_file_path)
    print(f"Arquivo PDF salvo em: {pdf_file_path}")

except sr.UnknownValueError:
    print("Google Speech Recognition não conseguiu entender o áudio")
except sr.RequestError as e:
    print(f"Erro ao solicitar resultados do serviço de reconhecimento; {e}")
