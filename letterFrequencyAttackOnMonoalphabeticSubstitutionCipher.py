# Q4 Write a program that can perform a letter frequency attack on an monoalphabetic substitution cipher
# without human intervention. Your software should produce possible plain text in rough order
# of likelihood. It would be good if your user interface allows user to specify "
# Give me top 10 possible plain texts"

import matplotlib.pyplot as plt


def printString(text, N):
    # Stores final 10 possible deciphered plaintext
    plaintext = [None] * 10
    # Store the frequency of each letter in cipher text
    freq = [0] * 26
    # Stores the frequency of each letter in cipher text in descending order
    freqSorted = [None] * 26

    # Store which alphabet is used already
    used = [0] * 26
    # list of alphabets
    letters = ["A",  "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    # Traverse the string S
    for i in range(N):
        if text[i] != ' ':
            freq[ord(text[i]) - 65] += 1

    # Copy the frequency array
    for i in range(26):
        freqSorted[i] = freq[i]

    # Stores the string formed from concatenating the english letters in the decreasing frequency
    # in the english language
    T = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    # Sort the array in descending order
    freqSorted.sort(reverse=True)
    # Iterate over the range [0, 5]
    for i in range(10):
        ch = -1
        # Iterate over the range [0, 26]
        for j in range(26):
            if freqSorted[i] == freq[j] and used[j] == 0:  # checking if the alphabet has been used before or not
                used[j] = 1
                ch = j
                break
        if ch == -1:
            break

        # Store the numerical equivalent of letter at ith index of array letter_frequency
        x = ord(T[i]) - 65
        # Calculate the probable shift used in monoalphabetic cipher
        x = x - ch
        # Temporary string to generate one plaintext at a time
        curr = ""

        # Generate the probable ith plaintext string using the shift calculated above
        for k in range(N):
            # Insert whitespaces as it is
            if text[k] == ' ':
                curr += " "
                continue

            # Shift the kth letter of the cipher by x
            y = ord(text[k]) - 65
            y += x

            if y < 0:
                y += 26
            if y > 25:
                y -= 26
            # Add the kth calculated/shifted letter to temporary string
            curr += chr(y + 65)
        plaintext[i] = curr

    # Print the generated 10 possible plaintexts
    for i in range(10):
        print(plaintext[i])

    # plotting the frequency of each alphabet in the given text
    plt.bar(letters, freq, 0.8, color='green')
    plt.title('Bar Chart to Show Frequency of Letters in Ciphertext')
    plt.xlabel('Letter')
    plt.ylabel('Frequency')
    plt.show()


if __name__ == '__main__':
    # Given string
    cipherText = input("Enter cipher Text: ")
    N = len(cipherText)

    # Function Call
    printString(cipherText, N)

# "GFCIVWIGYVMXC MW XLI TVEGXMGI SJ TVSXIGXMRK GVMXMGEP WCWXIQW ERH WIRWMXMZI MRJSVQEXMSR JVSQ HMKMXEP EXXEGOW"