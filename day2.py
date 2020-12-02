with open('resources/day2.txt', 'r') as f:
    lines = f.readlines()
lines = tuple(line.rstrip('\n') for line in lines)


def first_half():
    valid = 0

    for line in lines:
        start_range = int(line.split('-')[0])
        end_range = int(line[line.find('-') + 1:line.find(' ')])
        letter = line[line.find(' ') + 1:line.find(' ') + 2]
        password = line[line.find(': ') + 2:]

        occurrences = password.count(letter)
        if start_range <= occurrences <= end_range:
            valid += 1

    print(f'There are {valid} valid passwords')


def second_half():
    valid = 0

    for line in lines:
        first_pos = int(line.split('-')[0])
        second_pos = int(line[line.find('-') + 1:line.find(' ')])
        letter = line[line.find(' ') + 1:line.find(' ') + 2]
        password = line[line.find(': ') + 2:]

        first_letter = password[first_pos-1:first_pos]
        second_letter = password[second_pos-1:second_pos]
        if (first_letter == letter) ^ (second_letter == letter):
            valid += 1

    print(f'There are {valid} valid passwords')


def main():
    print('--- First half ---')
    first_half()
    print('--- Second half ---')
    second_half()


if __name__ == '__main__':
    main()
