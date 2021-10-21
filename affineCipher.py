# A python program to illustrate Affine Cipher Technique

class Inverse:
    def modularInverse(self, a, m):
        if m == 1:
            return -1
        x, gcd, y = self.euclideanAlgo(a, m)  # finding values of eqn using extended euclideanAlgo
        if gcd != 1:
            return None  # modular inverse does not exist
        return x + m if x < 0 else x

    def euclideanAlgo(self, a, b):
        if b == 0:
            return 1, a, 0
        temp_ans = self.euclideanAlgo(b, a % b)
        return temp_ans[2], temp_ans[1], temp_ans[0] - (a // b) * temp_ans[2]


class AffineCipher:
    # encrypting function
    #     C = (a*P + b) % 26 -->> formula for calculating cipher text
    def encrypt(self, text, key):
        cipherText = ''
        # traversing the plain text
        for char in text:
            # Insert whitespaces as it is
            if char == " ":
                cipherText += " "
                # Encrypt uppercase characters
            elif char.isupper():
                cipherText += chr(((key[0] * (ord(char)-ord('A')) + key[1]) % 26) + ord('A'))
                # Encrypt lowercase characters
            else:
                cipherText += chr(((key[0] * (ord(char) - ord('a')) + key[1]) % 26) + ord('a'))
        return cipherText

    # decrypting function
    #     P = (a^-1 * (C - b)) % 26 -->> formula for calculating plain text from cipher text
    def decrypt(self, cipherText, key):
        mv = Inverse()
        plainText = ''
        # traversing the cipherText text
        for char in cipherText:
            # Insert whitespaces as it is
            if char == " ":
                plainText += " "
                # Decrypt uppercase characters
            elif char.isupper():
                plainText += chr(((mv.modularInverse(key[0], 26) * (ord(char) - ord('A') - key[1])) % 26) + ord('A'))
                # Decrypt lowercase characters
            else:
                plainText += chr(((mv.modularInverse(key[0], 26) * (ord(char) - ord('a') - key[1])) % 26) + ord('a'))
        return plainText


# driver code
if __name__ == '__main__':
    cipher = AffineCipher()
    a = int(input("Enter a: "))  # user input for first key value i.e. 'a'
    b = int(input("Enter b: "))   # user input for second key value i.e. 'b'
    key = [a, b]
    text = input("Enter Plain text: ")  # user input of plain text
    ans = cipher.encrypt(text, key)
    #  printing both plain and cipher text
    print("Cipher text:-->", ans, "\nDecrypted text:-->", cipher.decrypt(ans, key))

