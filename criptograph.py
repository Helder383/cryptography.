import hashlib
from cryptography.fernet import Fernet


# Generate a key
key = Fernet.generate_key()
fernet = Fernet(key)

# Input method that allows you to insert any text to encrpt
text = str(input("Insert the text you want to encryt: ")).encode()

# Encrypt using AES
text_encryted = fernet.encrypt(text)

sha_256 = hashlib.sha256(text).hexdigest() # Encrypt using SHA_256
md5_encrypt = hashlib.md5(text).hexdigest() # Encrypt using MD5

# Dencrypt using AES
text_dencrypt = fernet.decrypt(text_encryted)
while True:
    opt = int(input("Which algorithm do you want to use:\n"
                    "[1] == MD5\n[2] == SHA_256\n[3] == AES\n\nType here: "))
    if opt == 1:
        print()
        print("Using Md5: ", md5_encrypt)
        break
    elif opt == 2:
        print()
        print("Using sha256: ", sha_256)
        break
    elif opt == 3:
        print()
        print("Encrypt using AES: ", text_encryted)
        opt2 = input("Would like to dencrypt too: ").capitalize()
        if opt2 == "Y":
            print()
            print("Dencrypt using AES: ", text_dencrypt)
            break
        else:
            print()
            print("Thank you for using our app")
            break
    else:
        print()
        print("Sorry we don't have that option!!!")
        print()
        opt = int(input("Which algorithm do you want to use:\n "
                        "[1] == MD5\n[2] == SHA_256\n[3] == AES\n\nType here: "))
print()
print("++++++++++++++ Always consider using AES to encrypt your password +++++++++++++++++++")
