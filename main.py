from datetime import datetime
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

    
    timestamp_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_execucao = [
        f"=== Relatório de Organização de Arquivos ===",
        f"Data/Hora: {timestamp_inicio}",
        f"Diretório: {diretorio.resolve()}",
        "-" * 40
    ]
    
    sucessos = 0
    ignorados = 0
    erros = 0

    
    for arquivo in diretorio.iterdir():
        if arquivo.is_file():
            
            if arquivo.name == "relatorio_organizacao.txt":
                continue

            extensao = arquivo.suffix.lower()
            movido = False

            
            for categoria, extensoes in MAPA_EXTENSOES.items():
                if extensao in extensoes:
                    pasta_destino = diretorio / categoria
                    pasta_destino.mkdir(exist_ok=True)

                    destino_final = pasta_destino / arquivo.name
                    
                    if destino_final.exists():
                        msg = f"[Aviso] '{arquivo.name}' já existe em '{categoria}'. Ignorado."
                        print(msg)
                        log_execucao.append(msg)
                        ignorados += 1
                    else:
                        try:
                            shutil.move(str(arquivo), str(destino_final))
                            msg = f"[Sucesso] {arquivo.name} -> {categoria}/"
                            print(msg)
                            log_execucao.append(msg)
                            sucessos += 1
                        except PermissionError:
                            msg = f"[Erro de Permissão] '{arquivo.name}' está em uso ou sem acesso."
                            print(msg)
                            log_execucao.append(msg)
                            erros += 1
                        except Exception as e:
                            msg = f"[Erro Inesperado] Falha ao mover '{arquivo.name}': {e}"
                            print(msg)
                            log_execucao.append(msg)
                            erros += 1
                    
                    movido = True
                    break
            
            
            if not movido and extensao != "":
                pasta_outros = diretorio / "Outros"
                pasta_outros.mkdir(exist_ok=True)
                destino_final = pasta_outros / arquivo.name
                
                if not destino_final.exists():
                    try:
                        shutil.move(str(arquivo), str(destino_final))
                        msg = f"[Outros] {arquivo.name} -> Outros/"
                        print(msg)
                        log_execucao.append(msg)
                        sucessos += 1
                    except PermissionError:
                        msg = f"[Erro de Permissão] '{arquivo.name}' está em uso."
                        print(msg)
                        log_execucao.append(msg)
                        erros += 1
                    except Exception as e:
                        msg = f"[Erro Inesperado] Falha ao mover '{arquivo.name}': {e}"
                        print(msg)
                        log_execucao.append(msg)
                        erros += 1

    
    log_execucao.append("-" * 40)
    log_execucao.append(f"Resumo: {sucessos} movidos | {ignorados} ignorados | {erros} erros")
    
    
    caminho_log = diretorio / "relatorio_organizacao.txt"
    try:
        with open(caminho_log, "w", encoding="utf-8") as f:
            f.write("\n".join(log_execucao))
        print(f"\n[Relatório Gerado] Salvo em: {caminho_log.name}")
    except Exception as e:
        print(f"\n[Aviso] Não foi possível salvar o arquivo de log: {e}")

    print("\nOrganização concluída!")

if __name__ == "__main__":
    pasta_para_organizar = "./teste_downloads" 
    os.makedirs(pasta_para_organizar, exist_ok=True)
    
    organizar_pasta(pasta_para_organizar)