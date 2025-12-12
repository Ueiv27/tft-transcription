import os
import glob
import argparse
from src.pipeline import TranscriptionETL

def main(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    # Inizializza la pipeline
    etl = TranscriptionETL()
    
    # Lista file audio
    extensions = ['*.mp3', '*.m4a', '*.wav']
    files = []
    for ext in extensions:
        files.extend(glob.glob(os.path.join(input_dir, ext)))
    
    print(f"Trovati {len(files)} file nella coda.")
    
    for file_path in files:
        filename = os.path.basename(file_path)
        output_filename = os.path.splitext(filename)[0] + ".json"
        output_path = os.path.join(output_dir, output_filename)
        
        # Check Idempotenza (Se esiste, skippa)
        if os.path.exists(output_path):
            print(f"SKIPPING: {filename} già elaborato.")
            continue
            
        etl.process_file(file_path, output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    args = parser.parse_args()
    
    main(args.input_dir, args.output_dir)