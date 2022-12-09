def calc_movement(T, H):
    if H[0] - 1 > T[0]:
        T[0] += 1
        if H[1] > T[1]:
            T[1] += 1
        elif H[1] < T[1]:
            T[1] -= 1
    elif H[0] + 1 < T[0]:
        T[0] -= 1
        if H[1] > T[1]:
            T[1] += 1
        elif H[1] < T[1]:
            T[1] -= 1
    if H[1] - 1 > T[1]:
        T[1] += 1
        if H[0] > T[0]:
            T[0] += 1
        elif H[0] < T[0]:
            T[0] -= 1
    elif H[1] + 1 < T[1]:
        T[1] -= 1
        if H[0] > T[0]:
            T[0] += 1
        elif H[0] < T[0]:
            T[0] -= 1
    return T


def a(lines):
    T = [0, 0]
    H = [0, 0]
    steps = set()
    for instruction in lines:
        d, s = instruction.split(' ')
        s = int(s)

        for i in range(s):
            if d == 'U':
                H[1] += 1
            elif d == 'D':
                H[1] -= 1
            elif d == 'L':
                H[0] -= 1
            else:
                H[0] += 1

            T = calc_movement(T, H)
            steps.add((T[0], T[1]))
    print(len(steps))


def b(lines):
    rope = [[0, 0] for i in range(10)]
    steps = set()

    for instruction in lines:
        d, s = instruction.split(' ')
        s = int(s)

        for i in range(s):
            if d == 'U':
                rope[0][1] += 1
            elif d == 'D':
                rope[0][1] -= 1
            elif d == 'L':
                rope[0][0] -= 1
            else:
                rope[0][0] += 1

            for i in range(1, len(rope)):
                rope[i] = calc_movement(rope[i], rope[i-1])
            if i == 1:
                return
            steps.add((rope[-1][0], rope[-1][1]))
    print(len(steps))


if __name__ == '__main__':
    with open('input') as f:
        b(f.read().split('\n')[:-1])
