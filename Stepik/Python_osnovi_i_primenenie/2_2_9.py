from simplecrypt import decrypt


with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

for password in open("passwords.txt", "r"):
    try:
        print(decrypt(password[:-1], encrypted).decode("utf8"))
    except Exception:
        pass
    else:
        print(password, 'is correct')




