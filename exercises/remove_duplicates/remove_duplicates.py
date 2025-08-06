"""
Write a python script that deletes rows from CSV-file
based on an indicated column, and saves the results in 
the new file.

Example:
```bash
python remove_duplicates.py input.csv output.csv id
id,name,age
1,John,30
2,Jane,25
4,Bob,35
```
"""

# Native solution

import sys

def process_string(x: str) -> list:
    """Given a string like 'a,b,c\n', 
    split it into a list based on delimiter ','
    """
    return [i.strip('\n') for i in x.split(',')]

def remove_duplicates(input_csv: str, 
                      output_csv: str, 
                      column_name: str
                      ) -> int:
    """Given input_csv, remove duplicate rows based on column_name column
    and return a string with filtered rows.
    """
    dupl_check = set()
    dupl_count = 0

    with open(input_csv, 'r') as input, open(output_csv, 'w') as output:
        # First, check which index is the column
        first_line = input.readline()
        columns = process_string(first_line)
        col_index = columns.index(column_name)
        output.write(first_line)
        # Process the rest of the rows
        for line in input:
            line_proc = process_string(line)
            line_value_dup_check = line[col_index]
            if line_value_dup_check not in dupl_check:
                dupl_check.add(line_value_dup_check)
                output.write(line)
            else:
                dupl_count += 1
    print(f"> finished task! Found {dupl_count} duplicate rows based on column '{column_name}'")
    return dupl_count

if __name__ == '__main__':
    # Get arguments from the console
    assert len(sys.argv) == 4, "Please provide three arguments after the script name: input csv file, output csv file, column name"
    input_csv, output_csv, column_name = sys.argv[1], sys.argv[2], sys.argv[3]
    dupl_count = remove_duplicates(input_csv, output_csv, column_name)

