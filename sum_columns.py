import csv
import re
import sys

def is_numeric(value):
    return re.match(r"-?\d+(\.\d+)?", value)

def analyze_csv(filename, column_number):
    numeric_sum = 0
    non_numeric_count = 0
    empty_count = 0

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        column_name = header[column_number]

        for row in reader:
            if len(row) > column_number:
                field = row[column_number].strip()
                if field == "":
                    empty_count += 1
                elif is_numeric(field):
                    numeric_sum += float(field)
                else:
                    non_numeric_count += 1

    return column_name, numeric_sum, non_numeric_count, empty_count

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py filename column_number")
        sys.exit(1)

    filename = sys.argv[1]
    column_number = int(sys.argv[2])

    try:
        column_name, numeric_sum, non_numeric_count, empty_count = analyze_csv(filename, column_number)
        
        total_message = f'The total amount of{column_name} column is {numeric_sum:,.1f}'
        print(total_message)

    except FileNotFoundError:
        print("ERROR: The specified file was not found.")
    except IndexError:
        print("ERROR: The specified column does not exist in the CSV file.")
    except Exception as e:
        print(f"An error occurred: {e}")
