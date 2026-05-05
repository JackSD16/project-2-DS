import unittest
from proj2 import read_csv_lines, filter_rows, listlen


cats = [
        "country",
        "year",
        "electricity_and_heat_co2_emissions",
        "electricity_and_heat_co2_emissions_per_capita",
        "energy_co2_emissions",
        "energy_co2_emissions_per_capita",
        "total_c o2_emissions_excluding_lucf",
        "total_co2_emissions_excluding_lucf_per_capita",
    ]


def create_linked_list(rows: list[Row]) -> Optional[Node]:
    if rows == []:
        return None
    return Node(rows[0], create_linked_list(rows[1:]))

def parse_row(fields: list[str]) -> Row:
    return Row(
        fields[0],
        int(fields[1]),
        float(fields[2]) if fields[2] != "" else None,
        float(fields[3]) if fields[3] != "" else None,
        float(fields[4]) if fields[4] != "" else None,
        float(fields[5]) if fields[5] != "" else None,
        float(fields[6]) if fields[6] != "" else None,
        float(fields[7]) if fields[7] != "" else None,
    )

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
