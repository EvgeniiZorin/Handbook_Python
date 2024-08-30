import argparse
import pandas as pd

parser = argparse.ArgumentParser(description="Run the program like this: `python cmd_line_prog.py -n 'Jack Jones' -a 10 -i 'whatever_file.csv'` ")
parser.add_argument(
    '-n', 
    '--name', 
    help='Your name here', 
    default='Stranger',
    type=str, # you have to input this data type of value. If it's not the specified data type, returns error
    required=True, # you have to specify this argument (name)
    choices=['Stranger', 'Jack Jones'] # returns an error if any other value is passed
)
parser.add_argument(
    '-a',
    '--age',
    type=int,
    required=True
)
parser.add_argument(
    '-i', 
    '--input', 
    help='File input'
)

args = parser.parse_args()

print(f"Hello, {args.name}! {type(args.name)}")
print(f"Your age is: {args.age} {type(args.age)}")
print(f"You want me to open the file: {args.input}")