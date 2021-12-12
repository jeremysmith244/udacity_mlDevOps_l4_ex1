'''
Factorial module
'''

import logging

logging.basicConfig(
    filename='./logging.log'
)

def factorial(num):
    '''Returns factorial of integer numbers'''

    result = 1
    if num < 0:
        logging.error('ERROR: Negative numbers are invalid!')
        raise ValueError
    if not isinstance(num, int):
        logging.error('ERROR: Only integers are valid!')
        raise ValueError
    while num > 0:
        result *= num
        num -= 1
    return result
