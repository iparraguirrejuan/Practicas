"""
Instructions
Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the letters in the alphabet using an integer key between 0 and 26. Using a key of 0 or 26 will always yield the same output due to modular arithmetic. The letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly used rotational cipher is ROT13."""

def rotate(texto, clave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    texto_rotado = ""

    for caracter in texto:
        if caracter.isalpha():
            if caracter.isupper():
                indice = alfabeto.index(caracter.lower())
                caracter_rotado = alfabeto[(indice + clave) % 26].upper()
            else:
                indice = alfabeto.index(caracter)
                caracter_rotado = alfabeto[(indice + clave) % 26]
            texto_rotado += caracter_rotado
        else:
            texto_rotado += caracter

    return texto_rotado

rotate("The quick brown fox jumps over the lazy dog.", 13)