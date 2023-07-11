class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26
        self.__charsA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__charsB = "abcdefghijklmnopqrstuvwxyz"

    def encode(self, text):
        encoded_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    encoded_char = self.__charsB[(self.__charsB.index(char) + self.shift) % 26]
                else:
                    encoded_char = self.__charsA[(self.__charsA.index(char) + self.shift) % 26]
            else:
                encoded_char = char
            encoded_text += encoded_char
        return encoded_text

    def decode(self, text):
        decoded_text = ""
        for char in text:
            if char.isalpha():
                if char.islower():
                    decoded_char = self.__charsB[(self.__charsB.index(char) - self.shift) % 26]
                else:
                    decoded_char = self.__charsA[(self.__charsA.index(char) - self.shift) % 26]
            else:
                decoded_char = char
            decoded_text += decoded_char
        return decoded_text


cipher = CaesarCipher(5)

print(cipher.encode('Beegeek'))      # Gjjljjp
print(cipher.decode('Gjjljjp'))      # Beegeek

print(cipher.encode('Жньъъа123'))    # Южтчххы123
print(cipher.decode('Южтчххы123'))    # Жньъъа123
