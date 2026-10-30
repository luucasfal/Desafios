from cryptography.fernet import Fernet
import os

def main(diretorio):
    with open("chave.key", "rb") as file: 
        chave = file.read()
        file.close()

    for raiz,_,arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz,nome)

            if nome != "ransow.py" and not nome.endswith(".key"):
                f = Fernet(chave)

                with open(caminho, "rb") as file:
                    dados = file.read()
                    file.close()

                decripty = f.decrypt(dados)

                with open(caminho, "wb") as file:
                    file.write(decripty)
                    file.close()

main("test_files")
