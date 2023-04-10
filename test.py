
import re

def data_clean(input_data): 
    """This function checks if the input is a word or string"""
    input_data_list = list(input_data)
    pedmas_symbols = ['(', ')', '*', '/', '+', '-' ]

    for data in input_data_list:
        if data not in pedmas_symbols and not data.isdigit():
            return TypeError ("Incorrect input, type in either a number or an operator")
        else:
             return clean_numbers(input_data_list)



def clean_numbers(input_data_list):
    """This function eliminates comma sepration for mutliple digit numbers"""
    return_list = []
    for element in input_data_list:
        if re.match(r"\d", element):
            if return_list and re.match(r"\d", return_list[-1]):
                return_list[-1] += element
            else:
                return_list.append(element)
        else:
            return_list.append(element)
    
    return return_list

example = '(44+(34+2)'
print(data_clean(example
))
