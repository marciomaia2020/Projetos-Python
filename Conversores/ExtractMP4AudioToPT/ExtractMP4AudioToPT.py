from moviepy.editor import VideoFileClip
import speech_recognition as sr
from googletrans import Translator

# Extrai o áudio do vídeo
def extract_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = "audio.wav"
    video.audio.write_audiofile(audio_path, codec="pcm_s16le")
    return audio_path

# Converte o áudio em texto
def audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)  # Lê todo o áudio
    try:
        # Tentando reconhecer a fala no áudio (ajuste de linguagem para português do Brasil)
        text = recognizer.recognize_google(audio, language="pt-BR")
        print("Texto reconhecido:", text)
        return text
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        return None
    except sr.RequestError as e:
        print(f"Erro na requisição para o serviço de reconhecimento de fala: {e}")
        return None

# Traduz o texto para o português
def translate_text(text):
    translator = Translator()
    translated = translator.translate(text, dest="pt")
    return translated.text

# Caminho do vídeo
video_path = r"C:\Users\Marcio Fernando Maia\Videos\Captures\LiveDraws-Nov.07.2024.mp4"  # Use uma string bruta para o caminho

# Processamento
audio_path = extract_audio(video_path)  # Extraindo o áudio do vídeo
text = audio_to_text(audio_path)  # Convertendo áudio em texto
if text:
    translated_text = translate_text(text)  # Traduzindo o texto para o português
    print("Texto traduzido:", translated_text)  # Exibindo o texto traduzido
else:
    print("Não foi possível realizar a transcrição e tradução.")
