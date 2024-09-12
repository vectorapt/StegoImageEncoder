#Steganography image encoding
#This is a basic python program using concepts of steganography to encode a secret message into an image
#For the purpose of this task i have used the Vault-Tec Security company logo for encoding a secret image

from stegano import lsb
secret=lsb.hide("VSLogo.png","Image encoded Succesfully, Task completed")
secret.save("New_VSLogo.png")

secret_data=lsb.reveal("new_VSLogo.png")
print(secret_data)
