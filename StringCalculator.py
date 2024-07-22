import re

def ifEmptyString(numbers: str) -> int:
    if not numbers:
        return 0
    if numbers == "0":
        return 0
    return -1

def extract_numbers(string):
    numbers = re.findall(r'\d+', string)
    numbers = list(map(int, numbers))
    return numbers

def sumNumList(num_list: list) -> int:
    return sum(int(num) for num in num_list if int(num) <= 1000)

def add(numbers: str) -> int:
    if ifEmptyString(numbers) == 0:
        return 0
    num_list = extract_numbers(numbers)
    return sumNumList(num_list)
