import os
import pyaes

file_name = "teste.txt.ransonware"
with open(file_name, 'rb') as arq:
    file_data = arq.read()
    arq.close()

os.remove(file_name)

key = b'testeransonwares'
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.decrypt(file_data)

new_file = "teste.txt."
with open(f"{new_file}", "wb") as arq:
    arq.write(crypto_data)
    arq.close()