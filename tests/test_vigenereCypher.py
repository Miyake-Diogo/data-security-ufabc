from unittest import TestCase
from src.vigenereCypher import vigenereCypher

class test_vigenereCypher(TestCase):

    def test_if_key_is_generated_equal_lenght(self):
        keyword_text = "TEXTO"
        vigenere = vigenereCypher(keyword_text)
        output_key = vigenere.generate_key('ABCDE', keyword_text)
        self.assertEqual(output_key, ['T', 'E', 'X', 'T', 'O'])

    def test_if_key_is_generated_different_lenght(self):
        keyword_text = "TEXTO2"
        vigenere = vigenereCypher(keyword_text)
        output_key = vigenere.generate_key('ABCDEFGH', keyword_text)
        self.assertEqual(output_key, "TEXTO2TE")

    def test_if_cipher_text_is_work(self):
        keyword_text = "UFABC"
        vigenere = vigenereCypher(keyword_text)
        key = vigenere.generate_key('ABCDE', keyword_text)
        expected_cipher_text = vigenere.get_cipher_text(keyword_text,key)
        self.assertEqual(expected_cipher_text, "OKACE")

    def test_if_original_text_is_work(self):
        keyword_text = "UFABC"
        vigenere = vigenereCypher(keyword_text)
        key = vigenere.generate_key('ABCDE', keyword_text)
        cipher_text = vigenere.get_cipher_text(keyword_text,key)
        expected_original_text = vigenere.get_original_text(cipher_text, key)
        self.assertEqual(expected_original_text, 'UFABC')