import re


pat = r'(\d+)\-(\d+)'


def a(lines):
    num = 0
    for pair in lines:
        a, b = re.findall(pat, pair)
        ai = set(range(int(a[0]), int(a[1])+1))
        bi = set(range(int(b[0]), int(b[1])+1))
        if ai <= bi or bi <= ai:
            num += 1
    print(num)


def b(lines):
    num = 0
    for pair in lines:
        a, b = re.findall(pat, pair)
        ai = set(range(int(a[0]), int(a[1])+1))
        bi = set(range(int(b[0]), int(b[1])+1))
        if len(ai & bi) > 0:
            num += 1
    print(num)


if __name__ == '__main__':
    with open('input') as f:
        b(f.read().split('\n')[:-1])
