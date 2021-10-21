# Q3 Write a program that can perform a letter frequency attack on an additive cipher
# without human intervention. Your software should produce possible plain text in rough order
# of likelihood. It would be good if your user interface allows user to specify "
# Give me top 10 possible plain texts"

class cipher():
    def frequencyAttcak(self):
        print("@ NOTE = PLEASE ENTER CAPS LETTERS")
        k = input("Enter you cipher-text :")
        print("---------------------------------------------------------")

        # looping in the range(0,26) as we want get every possible plain text with each key
        for j in range(0, 26):
            plain = []    # a list to store alphabets of plain text
            text = " "  # Temporary string to generate one plaintext at a time
            for i in range(0, len(k)):  # traversing the cipher text
                if k[i] == ' ':    # Insert whitespaces as it is
                    y = ' '
                    plain.append(y)
                    continue
                #     decrypting the cipher text
                b = (ord(k[i]) - 65)
                z = (b - j) % 26
                y = (chr(z + 65))
                plain.append(y)   # adding decrypted alphabet to the list

            for x in plain:
                text += x   # adding all the values of list created above in the string named 'text'

            print(f'Encrypted Cipher-text:{text}')  # printing the possible plain text


ad = cipher()
print("Do you want to perform letter frequency Attack on additive cipher??  \n1.yes  \n2.No")
choice = int(input())       # taking choice from user

if choice == 1:
    ad.frequencyAttcak()    # function calling
else:
    print("Thank-you , you choose to Quit.")