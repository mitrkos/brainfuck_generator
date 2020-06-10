import argparse


def add_nl(format_out: bool):
    return '\n' if format_out else ''


def generate_brainfuck(phrase: str, format_out: bool):
    symbs_num = {char: ord(char) for char in set(phrase)}

    decades = sorted(list({int(num / 10) for num in symbs_num.values()}))

    result = '+' * 10 + add_nl(format_out)
    result += '[' + add_nl(format_out)
    for decade in decades:
        result += '>' + '+' * decade + add_nl(format_out)
    result += '<' * len(decades) + '-' + add_nl(format_out)
    result += ']' + add_nl(format_out)

    current_decade_pos = 0
    for symb in phrase:
        num = symbs_num[symb]

        num_decade_pos = decades.index(int(num / 10)) + 1
        step_to_decade_pos = num_decade_pos - current_decade_pos
        if step_to_decade_pos > 0:
            result += '>' * step_to_decade_pos
        elif step_to_decade_pos < 0:
            result += '<' * (-step_to_decade_pos)
        current_decade_pos = num_decade_pos

        num_ones = num % 10
        result += '+' * num_ones + '.' + '-' * num_ones + add_nl(format_out)

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Brainfuck code to print inputted ascii string')
    parser.add_argument(
        'string',
        type=str,
        help='String for printing'
    )
    parser.add_argument(
        '-f',
        action='store_true',
        help='Format printing (with \\n)'
    )
    args = parser.parse_args()

    result = generate_brainfuck(args.string, args.f)
    print(result)
