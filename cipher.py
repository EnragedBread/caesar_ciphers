from string import ascii_lowercase

import wordninja

alphabet = ascii_lowercase
letter_count = len(ascii_lowercase)

def encode(plaintext,shift):
    ciphertext = []
    for letter in plaintext:
        pos = alphabet.find(letter)
        if pos < 0:
            ciphertext.append(letter)
        else:
            pos = (pos + shift) % letter_count
            ciphertext.append(alphabet[pos])

    return ''.join(ciphertext)

def decode(ciphertext,shift):
    message = encode(ciphertext, -shift).replace(' ', '')
    message = ' '.join(wordninja.split(message))
    return message

def brute_force(ciphertext):
    messages = []
    for shift in range(0, letter_count):
        message = decode(ciphertext, shift)
        messages.append((shift, message))

    return messages