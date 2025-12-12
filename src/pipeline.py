import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import logging
import os
import json
from .config import MODEL_ID, BATCH_SIZE, CHUNK_LENGTH_S, TFT_KEYWORDS

# Setup Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TranscriptionETL:
    def __init__(self):
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
        logging.info(f"Inizializzazione Pipeline su device: {self.device}")
        self.pipe = self._load_model()

    def _load_model(self):
        # Caricamento ottimizzato del modello
        logging.info(f"Caricamento modello {MODEL_ID}...")
        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            MODEL_ID, torch_dtype=self.torch_dtype, use_safetensors=True, low_cpu_mem_usage=True
        )
        model.to(self.device)
        processor = AutoProcessor.from_pretrained(MODEL_ID)
        
        # Creazione pipeline HuggingFace
        return pipeline(
            "automatic-speech-recognition",
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            max_new_tokens=128,
            chunk_length_s=CHUNK_LENGTH_S,
            batch_size=BATCH_SIZE,
            torch_dtype=self.torch_dtype,
            device=self.device,
        )

    def process_file(self, file_path, output_path):
        try:
            logging.info(f"Inizio elaborazione: {os.path.basename(file_path)}")
            
            # Qui potremmo inserire logica per iniettare i prompt/keywords se supportato dalla versione
            # Attualmente Whisper V3 è molto bravo, ma il prompt engineering si fa qui
            
            result = self.pipe(
                file_path, 
                generate_kwargs={"language": "english"}
            )
            
            # Salvataggio (Load step)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=4)
                
            logging.info(f"Completato: {output_path}")
            return True
            
        except Exception as e:
            logging.error(f"Errore su {file_path}: {str(e)}")
            return False