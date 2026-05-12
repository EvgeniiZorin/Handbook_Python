"""
Note: this is NOT a CLI program, 
but if you pass it some arguments while running it,
it can use it.
"""
import sys 

terminal_args = sys.argv

# Name of the script
print(f"Name of the script: {terminal_args[0]}")

if len(terminal_args) > 1:
    print(f'You passed in the following arguments in the command line: {terminal_args[1:]}')
else:
    print(f"You didn't pass in any arguments.")
