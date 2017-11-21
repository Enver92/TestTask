import re
import pprint

# Task #1
def handle_numbers(num1, num2, num3):
    """ Returns the count of integers that are divisible by num3
    in range [num1, num2] (including num3)"""
    if num3 != 0:
        digits_num = len([x for x in range(num1,num2+1) if x%num3==0])
        print('Result: ' + str(digits_num))
    else:
        print("You cannot divide by 0")

# Task #2
def handle_string(value):
    """A function that takes sentense as a parameter (e.g. handle_string(value))
     and count number of letters and digits"""

    if value:
        regex_letters = r'[a-zA-Z]'
        regex_digits = r'\d'

        number_of_letters = len(re.findall(regex_letters, value))
        number_of_digits = len(re.findall(regex_digits, value))
        print('Result:\nLetters - {0}\nDigits - {1}'.format(number_of_letters, number_of_digits))

    else:
        print('The string is empty')

# Task #3
def handle_list_of_tuples(list_of_tuples):
    '''a function that takes list of tuples (e.g. handle_list_of_tuples(list))
    and sort it based on the next rules:
    name / age / height / weight'''
    pp = pprint.PrettyPrinter()
    pp.pprint(sorted(list_of_tuples, key=lambda x: (x[0], -int(x[1]), -int(x[2]), -int(x[3]))))
