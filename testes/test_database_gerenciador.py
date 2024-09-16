import unittest
from unittest.mock import patch, MagicMock
from database_gerenciador import Database

class TestDatabase(unittest.TestCase):

    @patch('database_gerenciador.db.connect')
    def test_init_singleton(self, mock_connect):
        # Mock the database connection and cursor
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Create the first instance of Database
        db1 = Database()
        
        # Ensure the database connection and cursor are set correctly
        mock_connect.assert_called_once_with("Database.db")
        self.assertEqual(db1.banco, mock_conn)
        self.assertEqual(db1.cursor, mock_cursor)
        self.assertTrue(db1.initialized)

        # Create the second instance of Database
        db2 = Database()

        # Ensure the second instance is the same as the first one (singleton)
        self.assertIs(db1, db2)
        self.assertEqual(db2.banco, mock_conn)
        self.assertEqual(db2.cursor, mock_cursor)
        self.assertTrue(db2.initialized)

if __name__ == '__main__':
    unittest.main()