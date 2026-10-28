import os
from pathlib import Path
import shutil


MAPA_EXTENSOES = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Musicas": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Instaladores": [".exe", ".msi", ".dmg", ".pkg"],
}

def organizar_pasta(caminho_alvo):
    diretorio = Path(caminho_alvo)
    
    if not diretorio.exists():
        print(f"Erro: O diretório '{caminho_alvo}' não existe.")
        return

    print(f"Organizando a pasta: {diretorio.resolve()}\n")

    
    for arquivo in diretorio.iterdir():
        if arquivo.is_file():
            extensao = arquivo.suffix.lower()
            movido = False

            
            for categoria, extensoes in MAPA_EXTENSOES.items():
                if extensao in extensoes:
                    pasta_destino = diretorio / categoria
                    pasta_destino.mkdir(exist_ok=True)

                    destino_final = pasta_destino / arquivo.name
                    
                    
                    if destino_final.exists():
                        print(f"[Aviso] '{arquivo.name}' já existe em '{categoria}'. Ignorado.")
                    else:
                        shutil.move(str(arquivo), str(destino_final))
                        print(f"[Sucesso] {arquivo.name} -> {categoria}/")
                    
                    movido = True
                    break
            
            
            if not movido and extensao != "":
                pasta_outros = diretorio / "Outros"
                pasta_outros.mkdir(exist_ok=True)
                destino_final = pasta_outros / arquivo.name
                
                if not destino_final.exists():
                    shutil.move(str(arquivo), str(destino_final))
                    print(f"[Outros] {arquivo.name} -> Outros/")

    print("\nOrganização concluída!")

if __name__ == "__main__":
    
    pasta_para_organizar = "./teste_downloads" 
    os.makedirs(pasta_para_organizar, exist_ok=True)
    
    organizar_pasta(pasta_para_organizar)