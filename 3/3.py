def get_priority(c):
    val = ord(c.upper()) - 38
    if c == c.lower():
        val -= 26
    print(c, val)
    return val


def a(lines):
    sum = 0
    for rucksack in lines:
        r1 = set(rucksack[:len(rucksack)//2])
        r2 = set(rucksack[len(rucksack)//2:])
        common = list(r1 & r2)
        sum += get_priority(common[0])
    print(sum)


def b(lines):
    sum = 0
    for i in range(0, len(lines), 3):
        common = list(set(lines[i]) & set(lines[i+1]) & set(lines[i+2]))
        sum += get_priority(common[0])
    print(sum)


if __name__ == '__main__':
    with open('input') as f:
        b(f.read().split('\n')[:-1])
