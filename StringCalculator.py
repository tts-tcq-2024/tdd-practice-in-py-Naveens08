import re

def ifEmptyString(numbers: str) -> int:
    if not numbers:
        return 0
    if numbers == "0":
        return 0
    return -1

def extract_numbers(string):
    numbers = re.findall(r'-?\d+', string)
    numbers = list(map(int, numbers))
    return numbers

def CheckNegativeNumbers(num_list: list):
    NegativeNum = []
    for num in num_list:
        if int(num) < 0:
            NegativeNum.append(int(num))
    if NegativeNum:
        raise ValueError(f"Negatives not allowed: {','.join(map(str, NegativeNum))}")
    
def sumNumList(num_list: list, max_value) -> int:
    NumSum = 0
    CheckNegativeNumbers(num_list)
    for num in num_list:
        if int(num) <= max_value:
            NumSum = NumSum + int(num)
    
    return NumSum

def add(numbers: str) -> int:
    if ifEmptyString(numbers) == 0:
        return 0
    num_list = extract_numbers(numbers)
    return sumNumList(num_list, 1000)
