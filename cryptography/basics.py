# Caesar Cipher Implementation
# A Caesar Cipher shifts characters by a fixed number of places.
def caesar_encrypt(plaintext, shift):
    result = ""
    for char in plaintext:
        if 'A' <= char <= 'Z':  # Uppercase letters
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':  # Lowercase letters
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:  # Non-alphabetic characters remain unchanged
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Example Usage
# plaintext = "Hello, World!"
# shift = 3
# ciphertext = caesar_encrypt(plaintext, shift)
# decrypted = caesar_decrypt(ciphertext, shift)

# print("Plaintext:", plaintext)
# print("Ciphertext:", ciphertext)
# print("Decrypted:", decrypted)


# Vigenère Cipher Implementation
# A Vigenère Cipher uses a keyword to vary the shift for each character.
def vigenere_encrypt(plaintext, keyword):
    result = ""
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    for i, char in enumerate(plaintext):
        if 'A' <= char <= 'Z':
            shift = ord(keyword_repeated[i].upper()) - ord('A')
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            shift = ord(keyword_repeated[i].lower()) - ord('a')
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def vigenere_decrypt(ciphertext, keyword):
    result = ""
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]
    for i, char in enumerate(ciphertext):
        if 'A' <= char <= 'Z':
            shift = ord(keyword_repeated[i].upper()) - ord('A')
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            shift = ord(keyword_repeated[i].lower()) - ord('a')
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
    return result

# Example Usage
# plaintext = "Hello, World!"
# keyword = "KEY"
# ciphertext = vigenere_encrypt(plaintext, keyword)
# decrypted = vigenere_decrypt(ciphertext, keyword)

# print("Plaintext:", plaintext)
# print("Ciphertext:", ciphertext)
# print("Decrypted:", decrypted)

# Substitution Cipher Implementation
# A substitution cipher replaces each letter with a randomly mapped letter.
def generate_substitution_key():
    import random
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shuffled = alphabet[:]
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled)), dict(zip(shuffled, alphabet))

def substitution_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.upper() in key:
            encrypted_char = key[char.upper()]
            result += encrypted_char if char.isupper() else encrypted_char.lower()
        else:
            result += char
    return result

def substitution_decrypt(ciphertext, reverse_key):
    return substitution_encrypt(ciphertext, reverse_key)

# Example Usage
# key, reverse_key = generate_substitution_key()
# plaintext = "Hello, World!"
# ciphertext = substitution_encrypt(plaintext, key)
# decrypted = substitution_decrypt(ciphertext, reverse_key)

# print("Plaintext:", plaintext)
# print("Ciphertext:", ciphertext)
# print("Decrypted:", decrypted)
