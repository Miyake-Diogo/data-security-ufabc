"Implementation of Vigenere Cypher in Python "
"Diogo Miyake - 21048813"
"""Responda com suas palavras: por que a expressão algébrica
equivale ao uso da Tabela de Vigenère com lápis e papel?
 
A expressão faz com que a tabela funcione 
de acordo com cada caractere e sua respectiva chave"""

class vigenereCypher:
    def __init__(self, key):
        self.key = key

    def generate_key(self, text, key):
        key = list(key)
        if len(text) == len(key):
            return(key)
        else:
            for i in range(len(text) -
                        len(key)):
                key.append(key[i % len(key)])
        return("" . join(key))
        
    def get_cipher_text(self, original_text, key):
        "Return encripted text"
        
        cipher_text = []
        for i in range(len(original_text)):
            x = (ord(original_text[i]) +
                ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        return("" . join(cipher_text))
        
    def get_original_text(self, cipher_text, key):
        "Return Original Text"
        orig_text = []
        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) -
                ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))
        return("" . join(orig_text))
	
if __name__ == "__main__":
    text_string = "UFABC"
    keyword_text = "ABCDE"
    vigenere = vigenereCypher(keyword_text)
    key = vigenere.generate_key(text, keyword_text)
    cipher_text = vigenere.get_cipher_text(text,key)

    print("Key: ", key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :",
        vigenere.get_original_text(cipher_text, key))

