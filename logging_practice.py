"""
# Logging

import logging

# 5 levels of logging

DEBUG < INFO < WARNING < ERROR < CRITICAL

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
    level=logging.DEBUG, # This specifies the lowest level of log message that you want to include in your log file. DEBUG - include all; INFO - (skip debug) info and above; WARNING - (skip debug, info) warning and above; 
    filename="log.log", 
    filemode='w',
    format="%(asctime)s::%(levelname)s::%(message)s",
    force=True ### In e.g. jupyter notebook, need this line to not restart the kernel if you delete the file 
)

def add(x, y):
    return x+y

num_1, num_2 = 5, 10
add_result = add(num_1, num_2)
logging.debug(f'Add {num_1} + {num_2} = {add_result}')
logging.info('The function is working as expected.')
logging.warning('This is a warning!!!')
logging.error('This is an error!')
logging.critical('this is a critical state!')

# Logging exceptions
try:
    1 / 0
except ZeroDivisionError as e:
    # logging.error("exception: {e}", exc_info=True)
    logging.exception('error is found')

# Create custom loggers
logger = logging.getLogger("name")

logging.info('adsf')
