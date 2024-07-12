def check_password_dictionary(value=0):
    with open("easy_passwords.txt", "r", encoding="utf-8") as file:
        return file.read().splitlines()

print(check_password_dictionary())