import argparse
import pandas as pd

parser = argparse.ArgumentParser(
    description = "Run the program like this: `python cmd_line_prog.py -n 'Jack Jones' -a 10 -i 'whatever_file.csv'` "
)
parser.add_argument(
    '-n', 
    '--name', 
    help = 'Your name here', 
    type = str, # you have to input this data type of value. If it's not the specified data type, returns error
    required = True, # you have to specify this argument (name)
    choices = ['Stranger', 'Jack Jones'], # returns an error if any other value is passed
    dest = 'first_name' # specify the name you want this argument to have in your namespace / parsed args
)
parser.add_argument(
    '-a',
    '--age',
    default = 10,
    type = int,
    required = False,
)
parser.add_argument(
    '-i', 
    '--input', 
    help = 'File input',
    required = False,
    default = 'unknown-file'
)
parser.add_argument(
    '--sq',
    help = 'list of numbers to square',
    nargs = '*', # take in 0 or more arguments; if you specify '+', it means i need at least 1 value 
    type = float
)

# Add a group of mutually-exclusive arguments, i.e. only one of them is required and you cannot use the other ones
group = parser.add_mutually_exclusive_group(
    # required = True # if you enable this, it will require you to specify one of these mutually-exclusive arguments
)
group.add_argument(
    '-v', 
    '--verbose',
    help = 'Enable verbose mode',
    action = 'store_true'
)
group.add_argument(
    '-q', 
    '--quiet',
    action = 'store_true' # default = True, but if you pass in the argument, it becomes False
)

# Here, if you don't specify any argument, it will look for the passed arguments
# in sys.argv
args = parser.parse_args()

if args.verbose:
    print(f"[INFO] You passed in the arguments: {args}")
if args.quiet:
    print(f"[INFO] Quiet mode enabled.")

first_name, age, input = args.first_name, args.age, args.input

print(f"Hello, {first_name}! {type(first_name)}")
print(f"Your age is: {age} {type(age)}")
print(f"You want me to open the file: {input}")

if args.sq:
    squares = [n**2 for n in args.sq]
    print(f"You provided a list of numbers, squared is: {squares}")
else:
    print("No numbers provided - no squared!")
