def ifEmptyString(numbers: str) -> int:
    if not numbers:
        return 0
    if numbers == "0":
        return 0
    return -1

def add(numbers: str) -> int:
    if ifEmptyString(numbers) == 0:
        return 0
    return -1
