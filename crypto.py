"""
Crypto.py
Authors: Jasper Sands, Jackson Kunde, William Akis, Daniel Tan, Colin Skinner
Date:
"""
import math
import string
import random

###Dependencies
# Bit to byte: Takes a tuple of length 8 and converts it into an integer in [0, 255]
def bit_to_byte(bits):
    sum = 0
    for i in range(8):
        if int(bits[i]) == 1:
            sum += (2 ** (7 - i))
    return sum

# Byte to bit: Takes an integer in [0, 255] and converts it into a tuple of length 8
def byte_to_bit(byte):
    bits = []
    byteInt = int(byte)
    for i in range (8):
        x = 7 - i

        if (byteInt - (2 ** x)) >= 0:
            bits.append(1)
            byteInt = byteInt - (2 ** x)
        else:
            bits.append(0)
    return bits

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    encrypted = ""

    for i in plaintext:
        if 64 < ord(i) < 91:
            new_index = ord(i) + offset

            if new_index < 91:
                encrypted = encrypted + chr(new_index)
            else:
                encrypted = encrypted + chr(new_index - 26)
        else:
            encrypted = encrypted + i


    return encrypted

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
    decrypted = ""

    for i in ciphertext:
        if 64 < ord(i) < 91:
            new_index = ord(i) - offset

            if new_index > 64:
                decrypted = decrypted + chr(new_index)
            else:
                decrypted = decrypted + chr(new_index + 26)
        else:
            decrypted = decrypted + i


    return decrypted

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    alphabet = string.ascii_uppercase

    for i in range(0, len(plaintext)):
        index = alphabet.find(keyword[i % len(keyword)])
        index2 = alphabet.find(plaintext[i])
        index3 = int(index + index2)

    encrytped = ""
    encrypted += alphabet[index3 % len(alphabet)]

    return encrypted

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    alphabet = string.ascii_uppercase

    for i in range(0, len(plaintext)):
        index = alphabet.find(keyword[i % len(keyword)])
        index2 = alphabet.find(plaintext[i])
        index3 = int(index2 - index)

    decrypted = ""
    decrypted += alphabet[index3 % len(alphabet)]

    return decrypted

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):

    W = []

    W.append(random.randint(1,100))
    for i in range(n-1):
        W.append(sum(W) + random.randint(1,100))

    private_key = [tuple(W)]
    Q = sum(W) + random.randint(0,100)

    private_key.append(Q)
    R = 0

    for r in range(2,Q):
        if math.gcd(r,Q) == 1:
            R = r
            break

    private_key.append(R)

    return private_key

# Arguments: tuple (W, Q, R)
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):

    public_key = []

    for line in (private_key[0]):
        public_key.append((private_key[2] * line) % private_key[1])

    return public_key

# Arguments: string, B
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    plaintext_num = []

    for i in plaintext:
        let_val = byte_to_bit(ord(i))
        plaintext_num.append(let_val)


# Arguments: list of integers, tuple (W,Q,R)
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():

    # a = input("Word: ").upper()
    # num = int(input("Number: "))
    #
    # yes = encrypt_caesar(a, num)
    #
    # print(decrypt_caesar(yes, num))
    peen = generate_private_key()
    print(peen)
    other_peen = create_public_key(peen)
    print(other_peen)

if __name__ == "__main__":
    main()
