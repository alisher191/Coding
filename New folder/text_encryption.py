import pyAesCrypt

password = input('Введите пароль для шифрования файла: ')

#encrypt
# pyAesCrypt.encryptFile('rtext.txt', 'rtext.txt.aes', password)

#decrypt
pyAesCrypt.decryptFile('rtext.txt.aes', 'rtext.txt', password)
