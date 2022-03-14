from vigenereCypher import vigenereCypher

"Main code with some tests"
if __name__ == "__main__":
    text_string = "UFABC"
    keyword_text = "ABCDE"
    vigenere = vigenereCypher(keyword_text)
    key = vigenere.generate_key(text_string, keyword_text)
    encripted_text = vigenere.get_encripted_text(text_string,key)
    decripted_text = vigenere.get_decripted_text(encripted_text, key)

    print(f"Key: {key}")
    print(f"Encripted Text : {encripted_text}")
    print(f"Decrypted Text : {decripted_text }")