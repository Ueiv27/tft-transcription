import yt_dlp
import os

def scarica_audio(link_youtube):
    # Ottieni il percorso della cartella dove si trova QUESTO script (cioè 'input')
    current_folder = os.path.dirname(os.path.abspath(__file__))

    print(f"Salvataggio in: {current_folder}")

    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # Qui diciamo a yt-dlp di salvare nella cartella corrente
        'outtmpl': os.path.join(current_folder, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'no_warnings': True, # Rimuove i warning inutili di prima
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            print(f"Scaricando: {link_youtube}")
            ydl.download([link_youtube])
            print("Download completato!")
    except Exception as e:
        print(f"Errore: {e}")

# --- UTILIZZO ---
link = "https://youtu.be/sx0Y9jKB4KU?si=oVOEaHeOM9_svMf_"
scarica_audio(link)