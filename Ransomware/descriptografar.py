from cryptography.fernet import Fernet
import os
def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_descriptogrados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptogrados)
def encontrar_arquivos(diretorio):
    lista=[]
    for raiz, _, arquivos in os.walk(diretorio):
        for name in arquivos:
            caminho = os.path.join(raiz, name)
            if name != "descriptografar.py" and not name.endswith(".key"):
                lista.append(caminho)
    return lista

def main():
        chave = carregar_chave()
        arquivos = encontrar_arquivos("test_files")
        for arquivo in arquivos:
            descriptografar_arquivo(arquivo, chave)
        print("Arquivos descriptografados com sucesso!")

if __name__ == "__main__":
    main()
