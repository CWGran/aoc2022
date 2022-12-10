import re

checkpoints = [20, 60, 100, 140, 180, 220]


def check_sprite(x, cycle):
    cycle -= 1
    x -= 1
    if cycle % 40 >= x and cycle % 40 <= x + 2:
        return '#'
    else:
        return ' '


def a(lines):
    cycle = 1
    total = 0
    x = 1
    for l in lines:
        if 'noop' in l:
            cycle += 1
            if cycle in checkpoints:
                total += cycle * x
        if 'add' in l:
            num = int(l.split(' ')[-1])
            cycle += 1
            if cycle in checkpoints:
                total += cycle * x
            cycle += 1
            x += num
            if cycle in checkpoints:
                total += cycle * x
    print(total)


def b(lines):
    cycle = 1
    x = 1
    crt = ''
    for l in lines:
        if 'noop' in l:
            crt += check_sprite(x, cycle)
            if cycle % 40 == 0 and cycle != 0:
                crt += '\n'
            cycle += 1
        if 'add' in l:
            num = int(l.split(' ')[-1])
            crt += check_sprite(x, cycle)
            if cycle % 40 == 0 and cycle != 0:
                crt += '\n'
            cycle += 1
            crt += check_sprite(x, cycle)
            if cycle % 40 == 0 and cycle != 0:
                crt += '\n'
            cycle += 1
            x += num
    print(crt)




if __name__ == '__main__':
    with open('input') as f:
        b(f.read().split('\n')[:-1])
