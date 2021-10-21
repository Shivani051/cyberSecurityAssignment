# A python program to illustrate Additive Cipher Technique
# Examples :
# PlainText : ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Shift: 23
# CipherText: XYZABCDEFGHIJKLMNOPQRSTUVW
#
# PlainText : ATTACKATONCE
# Shift: 4
# CipherText: EXXEGOEXSRGI

class AddCypher:

    def encrypt(self, text, key):
        cipher_text = ''  # cipher Text
        # traverse the plain text
        for i in range(len(text)):
            char = text[i]
            # Insert whitespaces as it is
            if char == " ":
                cipher_text += " "
            # Encrypt uppercase characters
            elif char.isupper():
                cipher_text += chr((ord(char) + key - 65) % 26 + 65)
            # Encrypting lowercase characters
            else:
                cipher_text += chr((ord(char) + key - 97) % 26 + 97)
        return cipher_text

    def decrypt(self, text, key):
        plain_text = ''
        # traverse the cipher text
        for i in range(len(text)):
            char = text[i]
            # Insert whitespaces as it is
            if char == " ":
                plain_text += " "
            # Decrypt uppercase characters
            elif char.isupper():
                plain_text += chr((ord(char) - key - 65) % 26 + 65)
            # Decrypt lowercase characters
            else:
                plain_text += chr((ord(char) - key - 97) % 26 + 97)
        return plain_text


# driver code
if __name__ == '__main__':
    key = int(input("Enter Key: "))
    additive_cypher = AddCypher()
    plain_text = input("Enter PlainText: ")
    cipher_text = additive_cypher.encrypt(plain_text, key)
    print("CipherText is:-->", cipher_text)

    print("DecryptedText is:-->", additive_cypher.decrypt(cipher_text, key))

# Cybersecurity is the practice of Protecting critical systems and sensitive information from digital attacks
