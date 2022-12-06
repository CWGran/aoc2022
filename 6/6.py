def check(string, n):
    return len(set(string)) == n


def a(string):
    for i in range(0, len(string) - 4):
        if check(string[i:i+4], 4):
            print(i + 4)
            break


def b(string):
    for i in range(0, len(string) - 14):
        if check(string[i:i+14], 14):
            print(i + 14)
            break


if __name__ == '__main__':
    with open('input') as f:
        b(f.read())
