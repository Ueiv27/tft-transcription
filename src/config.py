# Configurazioni centralizzate
MODEL_ID = "openai/whisper-large-v3"
#MODEL_ID = "openai/whisper-tiny"
CHUNK_LENGTH_S = 30
BATCH_SIZE = 24  # Ottimizzato per T4 GPU
LANGUAGE = "en"
#LANGUAGE = "it"
# Il famoso vocabolario per TFT
TFT_KEYWORDS = [
    "TFT", "Teamfight Tactics", "Riot Games", "high roll", "slow roll", 
    "hyper roll", "econ", "augment", "comp", "pivot", "inting", 
    "griefing", "BIS items", "Choncc", "board", "carousel"
]