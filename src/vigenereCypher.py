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

        key_generated = ("" . join(key))
        return key_generated
        
    def get_encripted_text(self, original_text, key):
        "Return encripted text"
        
        cipher_text = []
        for i in range(len(original_text)):
            x = (ord(original_text[i]) +
                ord(key[i])) % 26
            x += ord('A')
            cipher_text.append(chr(x))
        encripted = ("" . join(cipher_text))
        return encripted
        
    def get_decripted_text(self, cipher_text, key):
        "Return Original Text"
        orig_text = []
        for i in range(len(cipher_text)):
            x = (ord(cipher_text[i]) -
                ord(key[i]) + 26) % 26
            x += ord('A')
            orig_text.append(chr(x))

        decripted = ("" . join(orig_text))
        return decripted
	