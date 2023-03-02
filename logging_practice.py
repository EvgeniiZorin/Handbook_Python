"""
# Logging

import logging

# 5 levels of logging
### DEBUG: detailed information, typically of interest only when diagnosing problems. 
logging.debug()
### INFO: confirmation that things are working as expected. 
logging.info()
### WARNING: an indication that something unexpected happened, or indicative of some 
### problem in the near future (e.g. 'disk space low'). The software is still working
### as expected.
logging.warning() # default output
### ERROR: due to a more serious problem, the software has not been able to perform some function.
logging.error()
### CRITICAL: a serious error, indicating that the program itself may be unable to continue running.
logging.critical()

"""

import logging

logging.basicConfig(
    level=logging.DEBUG, 
    filename="log.log", 
    filemode='w',
    format="%(asctime)s::%(levelname)s::%(message)s"
) # log at the level of DEBUG or above

def add(x, y):
    return x+y

num_1, num_2 = 5, 10
add_result = add(num_1, num_2)
logging.debug(f'Add {num_1} + {num_2} = {add_result}')

# Logging variables
x = 2
logging.info(f"the value of x is {x}")

# Logging exceptions
try:
    1 / 0
except ZeroDivisionError as e:
    # logging.error("exception: {e}", exc_info=True)
    logging.exception('error is found')

# Create custom loggers
logger = logging.getLogger("name")