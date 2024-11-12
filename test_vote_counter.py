# test_vote_counter.py
"Renzo Felix Aponte y Rodrigo Meza Félix Gavilán"
import unittest
from unittest.mock import patch, mock_open
from vote_counter import leer_documento, imprimir_votos, imprimir_ganador, count_votes
 # Assuming starter version is in `vote_counter.py`

class TestVoteCounter(unittest.TestCase):


    @patch("builtins.print")
    def test_count_votes_valid_file(self, mock_print):
        mock_csv = """city,candidate,votes
        Springfield,Alice,1200
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")
        
        # Expected output after tallying votes
        mock_print.assert_any_call("Alice: 3200 votes")
        mock_print.assert_any_call("Bob: 3250 votes")
        mock_print.assert_any_call("winner is Bob")
        self.assertEqual(mock_print.call_count, 3)
    def test_leer_documento(self):
        datos=leer_documento("votes.csv")
        datos_esperado=[('Springfield', 'Alice', 1200),
                        ('Springfield', 'Bob', 750),
                        ('Shelbyville', 'Alice', 2000),
                        ('Shelbyville', 'Bob', 2500),
                        ('Capital City', 'Alice', 1100),
                        ('Capital City', 'Bob', 2100)]
        self.assertEqual(datos,datos_esperado)

    @patch("builtins.print")
    def test_leer_documento_nofound(self, mock_print):
        datos = leer_documento("noexistente.csv")
        datos_esperado = []
        self.assertEqual(datos, [])
        mock_print.assert_called_once_with("el archivo no se encontro en la ruta")


    @patch("builtins.print")
    def test_count_votes_invalid_votes(self, mock_print):
        # Simulate a CSV file with invalid votes data
        mock_csv = """city,candidate,votes
        Springfield,Bob,750
        Shelbyville,Alice,2000
        Springfield,Alice,invalid
        Shelbyville,Bob,2500"""
        with patch("builtins.open", mock_open(read_data=mock_csv)):
            count_votes("votes.csv")

        # Expect Alice to be skipped due to invalid data, only Bob's votes should print correctly
        mock_print.assert_any_call("Bob: 3250 votes")
        mock_print.assert_any_call("Alice: 2000 votes")
        mock_print.assert_any_call("winner is Bob")
        self.assertEqual(mock_print.call_count, 3)




    @patch("builtins.print")
    def test_imprimir_ganador(self, mock_print):
        results = {"Alice": 1200, "Bob": 750}
        imprimir_ganador(results)
        mock_print.assert_called_with("winner is Alice")

if __name__ == "__main__":
    unittest.main()

