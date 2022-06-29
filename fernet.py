from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('login.py', 'rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)

print(encrypted)

with open('login.py', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# usando a chave
fernet = Fernet(key)

# abrindo o arquivo criptografado
with open('login.py', 'rb') as enc_file:
    encrypted = enc_file.read()

print(encrypted)
# descriptografando o arquivo
decrypted = fernet.decrypt(encrypted)

print(decrypted)

# abrindo o arquivo no modo de gravação e
# gravando os dados descriptografados
with open('login.py', 'wb') as dec_file:
    dec_file.write(decrypted)
