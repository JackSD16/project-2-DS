import unittest
from proj2 import read_csv_lines, filter_rows, listlen, create_linked_list, parse_row, cats


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.filename = "some-ghg-emissions.csv"

    def test_read_csv_lines_length(self):
        data = read_csv_lines(self.filename)
        self.assertTrue(listlen(data) > 0)

    def test_read_csv_lines_types(self):
        data = read_csv_lines(self.filename)
        self.assertIsNotNone(data.value.country)
        self.assertIsInstance(data.value.year, int)
    def test_filter_country_equal(self):
        data = read_csv_lines(self.filename)
        read = filter_rows(data, "country", "equal", "Samoa")
        cur = read
        
        while cur is not None:
            self.assertEqual(cur.value.country, "Samoa")
            cur = cur.next

    def test_filter_year_greater_than(self):
        data = read_csv_lines(self.filename)
        filtered = filter_rows(data, "year", "greater_than", 2000)

        current = filtered
        while current is not None:
            self.assertTrue(current.value.year > 2000)
            current = current.next

    def test_invalid_country_comparison(self):
        data = read_csv_lines(self.filename)
        with self.assertRaises(ValueError):
            filter_rows(data, "country", "greater_than", "Zambia")

if __name__ == "__main__":
    unittest.main()
