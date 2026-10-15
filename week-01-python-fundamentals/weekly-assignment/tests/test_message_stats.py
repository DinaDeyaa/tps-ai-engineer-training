import unittest
import tempfile
from pathlib import Path
from message_stats import calculate_stats


class TestMessageStats(unittest.TestCase):

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.csv_path = Path(self.folder.name) / "messages.csv"

    def tearDown(self):
        self.folder.cleanup()

    def test_correct_input(self):
        self.csv_path.write_text("message_id,text\n1,Hi\n2,Hello\n")

        result = calculate_stats(self.csv_path)

        self.assertEqual(result["message_count"], 2)
        self.assertEqual(result["average_length"], 3.5)
        self.assertEqual(result["longest_message"], "Hello")

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            calculate_stats(self.csv_path)

    def test_empty_file(self):
        self.csv_path.write_text("")

        with self.assertRaises(ValueError):
            calculate_stats(self.csv_path)

    def test_empty_message(self):
        self.csv_path.write_text("message_id,text\n1,\n2,Hello\n")

        result = calculate_stats(self.csv_path)

        self.assertEqual(result["message_count"], 2)
        self.assertEqual(result["average_length"], 2.5)
        self.assertEqual(result["longest_message"], "Hello")

    def test_malformed_input(self):
        self.csv_path.write_text("wrong_column,text\n1,Hello\n")

        with self.assertRaises(ValueError):
            calculate_stats(self.csv_path)


if __name__ == "__main__":
    unittest.main()