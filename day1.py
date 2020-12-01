with open('resources/day1.txt', 'r') as f:
    lines = f.readlines()

nums = tuple(int(line.rstrip('\n')) for line in lines)


def first_half():
    sums = None
    for x in nums:
        for y in nums:
            if x == y:
                continue
            if x + y == 2020:
                sums = (x, y)
                break
    print(f'{sums[0]} + {sums[1]} = {sums[0] + sums[1]}')
    print(f'{sums[0]} * {sums[1]} = {sums[0] * sums[1]}')


def second_half():
    sums = None
    for x in nums:
        for y in nums:
            for z in nums:
                if x == y or x == z or y == z:
                    continue
                if x + y + z == 2020:
                    sums = (x, y, z)
                    break
    print(f'{sums[0]} + {sums[1]} + {sums[2]} = {sums[0] + sums[1] + sums[2]}')
    print(f'{sums[0]} * {sums[1]} * {sums[2]} = {sums[0] * sums[1] * sums[2]}')


def main():
    print('--- First half ---')
    first_half()
    print('--- Second half ---')
    second_half()


if __name__ == '__main__':
    main()
