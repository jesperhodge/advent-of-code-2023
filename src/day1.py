def get_input_lines():
    with open('day1_input.txt') as f:
        lines = f.readlines()
    return lines


def get_first_numeric(line):
    for char in line:
        if char.isnumeric():
            return char
    return ''

def calculate_line_value(line):
    numeric = ''
    numeric += get_first_numeric(line)
    
    reversed_line = line[::-1]
    numeric += get_first_numeric(reversed_line)

    return int(numeric)


def calculateCalibrationValue(lines):
    calibrationValue = 0
    for line in lines:
        calibrationValue += calculate_line_value(line)
    return calibrationValue


def main():
    lines = get_input_lines()
    print(calculateCalibrationValue(lines))


if __name__ == "__main__":
    main()
