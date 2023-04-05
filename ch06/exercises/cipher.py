def encrypt(text):
    cipher = {
        'a': 'm', 'b': 'n', 'c': 'o', 'd': 'p', 'e': 'q', 'f': 'r', 'g': 's',
        'h': 't', 'i': 'u', 'j': 'v', 'k': 'w', 'l': 'x', 'm': 'y', 'n': 'z',
        'o': 'a', 'p': 'b', 'q': 'c', 'r': 'd', 's': 'e', 't': 'f', 'u': 'g',
        'v': 'h', 'w': 'i', 'x': 'j', 'y': 'k', 'z': 'l'
    }
    encrypted = ''
    for char in text:
        if char.isalpha():
            encrypted += cipher[char.lower()]
        else:
            encrypted += char
    return encrypted

phrase = "The quick brown fox jumps over the lazy dog"
encrypted = encrypt(phrase)
with open('encrypted.txt', 'w') as f:
    f.write(encrypted)
