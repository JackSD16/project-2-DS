import csv
import math
from dataclasses import dataclass
from typing import *
import sys
sys.setrecursionlimit(10_000)


cats = [
        "country",
        "year",
        "electricity_and_heat_co2_emissions",
        "electricity_and_heat_co2_emissions_per_capita",
        "energy_co2_emissions",
        "energy_co2_emissions_per_capita",
        "total_co2_emissions_excluding_lucf",
        "total_co2_emissions_excluding_lucf_per_capita",
    ]

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
def create_linked_list(rows: list[Row]) -> Optional[Node]:
    if rows == []:
        return None
    return Node(rows[0], create_linked_list(rows[1:]))


@dataclass(frozen=True)
class Row:
    country: str
    year: int
    electricity_and_heat_co2_emissions: float
    electricity_and_heat_co2_emissions_per_capita: float
    energy_co2_emissions: float
    energy_co2_emissions_per_capita: float
    total_co2_emissions_excluding_lucf: float
    total_co2_emissions_excluding_lucf_per_capita: float


@dataclass(frozen=True)
class Node:
    value: Row
    next: Node | None

cats = [
        "country",
        "year",
        "electricity_and_heat_co2_emissions",
        "electricity_and_heat_co2_emissions_per_capita",
        "energy_co2_emissions",
        "energy_co2_emissions_per_capita",
        "total_co2_emissions_excluding_lucf",
        "total_co2_emissions_excluding_lucf_per_capita",
    ]



def read_csv_lines(filename: str) -> Optional[Node]:
    """
    read the file and convert each row into the Row class and 
    return a linked-list of nodes with the data.
    
    """

    with open(filename, newline="") as f:
        scanned = csv.reader(f)
        head = next(scanned)
        rows = []

        if head != cats:
            raise ValueError("Must be in the required catagories")

        for metric in scanned:
            rows.append(parse_row(metric))

    return create_linked_list(rows)



def listlen(data: Optional[Node]) -> int:
    """
    find the amount of nodes in the data
    """
    if data is None:
        return 0
    else:
        return 1 + (listlen(data.next))

def filter_rows(data: Optional[Node],field_name: str,comparison: str,value: Union[str, float, int]) -> Optional[Node]:
    """
    return linked list with rows only from input list
    that are relevant to field, comparison, and value.
    
    """

    
    if data is None:
        return None
    
    attr_val = getattr(data.value, field_name)
    next_data = filter_rows(data.next, field_name, comparison, value)

    if attr_val is None:
        return next_data
    if field_name == "country" and comparison != "equal":
        raise ValueError("Cannot compare these attributes")
    if comparison == "equal":
        match = attr_val == value
    elif comparison == "greater_than":
        match = attr_val > value
    elif comparison == "less_than":
        match = attr_val < value
    else:
        raise ValueError("Cannot compare")
    if match:
        return Node(data.value, next_data)

    return next_data




# Then your functions.

# ...

