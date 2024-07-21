def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = self._extract_delimiter(numbers)
        numbers = self._normalize_numbers(numbers, delimiter)

        num_list = re.split(delimiter, numbers)
        return self._sum_numbers(num_list)

def _extract_delimiter(self, numbers: str) -> str:
default_delimiter = ','
if numbers.startswith('//'):
    delimiter_part, numbers = numbers.split('\n', 1)
    delimiter = delimiter_part[2:]
    if delimiter.startswith('[') and delimiter.endswith(']'):
        delimiter = re.escape(delimiter[1:-1])
    return delimiter
return default_delimiter

def _normalize_numbers(self, numbers: str, delimiter: str) -> str:
if numbers.startswith('//'):
    _, numbers = numbers.split('\n', 1)
return numbers.replace('\n', delimiter)

def _sum_numbers(self, num_list: list) -> int:
total = 0
negatives = []

for num in num_list:
    if num:
        number = int(num)
        if number < 0:
            negatives.append(number)
        elif number <= 1000:
            total += number

return total
