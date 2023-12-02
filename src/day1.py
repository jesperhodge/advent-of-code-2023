import re

numbers_regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|0|1|2|3|4|5|6|7|8|9))'


char_to_numeric = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def get_input_lines():
    with open('day1_input.txt') as f:
        lines = f.readlines()
    return lines


def get_string_numbers_value(line):
    value = ''
    matches = re.findall(numbers_regex, line)
    first = matches[0] if len(matches) > 0 else ''
    last = matches[-1] if len(matches) > 0 else ''

    if not first.isnumeric():
        value += char_to_numeric[first]
    else:
        value += first
    if not last.isnumeric():
        value += char_to_numeric[last]
    else:
        value += last

    return int(value) if value != '' else 0



def calculate_line_value(line):
    number = get_string_numbers_value(line)
    print(number)
    return number


def calculateCalibrationValue(lines):
    calibrationValue = 0
    for line in lines:
        calibrationValue += calculate_line_value(line)
    return calibrationValue


def main():
    lines = get_input_lines()
    res = calculateCalibrationValue(lines)
    print(res)
    return res



if __name__ == "__main__":
    main()
