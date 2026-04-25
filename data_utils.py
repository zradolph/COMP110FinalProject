"""Data related utility functions."""

__author__ = ["730799088", ""]

from csv import DictReader


def get_keys(
    input_dict: (
        dict[str, list[str]]
        | dict[str, list[int]]
        | dict[str, list[str | int]]
        | dict[str, int]
        | dict[str, str]
    ),
) -> list[str]:
    result: list[str] = []
    for key in input_dict:
        result.append(key)

    return result


def convert_columns_to_int(
    data: dict[str, list[str]], columns_conv: list[str]
) -> dict[str, list[str | int]]:
    """Convert the data in the selected columns to be of type int."""
    # Create new table to store converted data
    data_converted: dict[str, list[int | str]] = {}

    # Iterate through column names (keys of the dictionary)
    for col_name in data:
        # Create new list to append converted values to
        data_converted[col_name] = []

        # Declare the converted value with a type of either int or str
        converted_value: int | str

        # Iterate through data values in the column
        for value in data[col_name]:
            # If this column is in the list of columns to be converted,
            # cast it to an int
            if col_name in columns_conv:
                converted_value = int(value)
            else:
                converted_value = value

            # Add it to the new column of values, the list we created
            # that we have a reference to at data_converted[col_name]
            data_converted[col_name].append(converted_value)

    return data_converted

"""These are the functions we wrote/will write in class!"""
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings.
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        item: str = row[column]
        result.append(item)

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result

def head(table: dict[str, list[str]], num: int) -> dict[str, list[str]]:
    """Show only the top nums of a table."""
    result: dict[str, list[str]] = {}

    for column in table:
        values: list[str] = []
        if num > len(table[column]):
            raise IndexError("Error: Not enough rows in table.")
            # Edge case taken care of.
        for row in range(num):
            values.append(table[column][row])
        result[column] = values

    return result

def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Creates a new table with only the list of columns selected."""
    result: dict[str, list[str]] = {}

    for col in columns:
        if col not in table:
            raise IndexError("Error: Column not in table.")
        result[col] = table[col]
        # Literally takes the values from the table.
    
    return result

def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two tables together into one."""
    result: dict[str, list[str]] = {}

    for column in table1:
        result[column] = table1[column]
        
    for column in table2:
        if column in result:
            result[column] = table1[column] + table2[column]
        else:
            result[column] = table2[column]
    
    return result

def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list."""
    result: dict[str, int] = {}

    for number in values:
        if number in result:
            result[number] += 1
        else:
            result[number] = 1
    
    return result

def specify(table: dict[str, list[str]], column: str, values: list[str]) -> dict[str, list[str]]:
    """Filters a table based on a column and some specific given values."""
    result: dict[str, list[str]] = {}

    for key in table:
        result[key] = []

    for i in range(len(table[column])):
        if table[column][i] in values:
            for key in table:
                result[key].append(table[key][i])
    
    return result

def specify_not(table: dict[str, list[str]], column: str, values: list[str]) -> dict[str, list[str]]: 
    """Filters a table based on a column and some specific given values."""
    result: dict[str, list[str]] = {}

    for key in table:
        result[key] = []

    for i in range(len(table[column])):
        if table[column][i] not in values:
            for key in table:
                result[key].append(table[key][i])
    
    return result