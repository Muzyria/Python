class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26

    def encode(self, text):
        encoded_text = ""
        for char in text:
            if char.isalpha() and char.isascii():
                if char.isupper():
                    encoded_char = chr((ord(char) - 65 + self.shift) % 26 + 65)
                else:
                    encoded_char = chr((ord(char) - 97 + self.shift) % 26 + 97)
                encoded_text += encoded_char
            else:
                encoded_text += char
        return encoded_text

    def decode(self, text):
        decoded_text = ""
        for char in text:
            if char.isalpha() and char.isascii():
                if char.isupper():
                    decoded_char = chr((ord(char) - 65 - self.shift) % 26 + 65)
                else:
                    decoded_char = chr((ord(char) - 97 - self.shift) % 26 + 97)
                decoded_text += decoded_char
            else:
                decoded_text += char
        return decoded_text


cipher = CaesarCipher(5)

print(cipher.encode('Биgeek123'))
print(cipher.decode('Биljjp123'))
