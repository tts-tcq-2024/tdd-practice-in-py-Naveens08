def ifEmptyString(numbers: str) -> int:
    if not numbers:
        return 0
    if numbers == "0":
        return 0
    return -1

def ifNumberLessThanThousand(numbers: str) -> int:
    if int(num) <= 1000:
        return 0
    return -1

def sumNumList(num_list: list) -> int:
    if ifNumberLessThanThousand == 0:
        return sum(int(num) for num in num_list)
    return -1

def add(numbers: str) -> int:
    if ifEmptyString(numbers) == 0:
        return 0
    num_list = numbers.split(",")
    return sumNumList(num_list)
