from stegano import lsb, exifHeader

# # lsb (не работает с кириллицей)
# lsb_secret = lsb.hide('img.png', "Секретное слово")
# lsb_secret.save('secret_img.png')
#
# lsb_result = lsb.reveal('secret_img.png')
# print(lsb_result)

# # exifHeader (работает с кириллицей)
# exifHeader_secret = exifHeader.hide('img_1.jpg', 'secret_img_1.tiff', 'Секретное слово')
#
# result = exifHeader.reveal("secret_img_1.tiff")
# result = result.decode()
# print(result)

from steganocryptopy.steganography import Steganography

Steganography.generate_key("")
secret = Steganography.encrypt("key.key", "img.png", "secret_mess.txt")
secret.save("img_secretm.png")

result = Steganography.decrypt("key.key", "img_secretm.png")
print(result)
