def a(lines):
    visible = set()

    for x in range(len(lines[0])):
        visible.add((x, 0))
        visible.add((x, len(lines)-1))

    for y in range(len(lines)):
        visible.add((0, y))
        visible.add((len(lines[0])-1, y))

    for x in range(len(lines[0])):
        highest_0 = 0
        highest_1 = 0
        for y in range(len(lines)):
            if int(lines[y][x]) > highest_0:
                visible.add((x, y))
                highest_0 = int(lines[y][x])
            if int(lines[len(lines)-1-y][x]) > highest_1:
                visible.add((x, len(lines)-1-y))
                highest_1 = int(lines[len(lines)-1-y][x])


    for y in range(len(lines)):
        highest_0 = 0
        highest_1 = 0
        for x in range(len(lines[y])):
            if int(lines[y][x]) > highest_0:
                visible.add((x, y))
                highest_0 = int(lines[y][x])
            if int(lines[y][len(lines[y])-1-x]) > highest_1:
                visible.add((len(lines[y])-1-x, y))
                highest_1 = int(lines[y][len(lines[y])-1-x])
    print(len(visible))


def b(lines):
    best = 0
    for y in range(1,len(lines)-1):
        for x in range(1,len(lines[y])-1):
            score = 1

            for xi in range(x-1, -1, -1):
                if int(lines[y][xi]) >= int(lines[y][x]) or xi == 0:
                    score *= x - xi
                    break

            for xi in range(x+1, len(lines[y])):
                if int(lines[y][xi]) >= int(lines[y][x]) or xi == len(lines[y])-1:
                    score *= xi - x
                    break

            for yi in range(y-1, -1, -1):
                if int(lines[yi][x]) >= int(lines[y][x]) or yi == 0:
                    score *= y - yi
                    break

            for yi in range(y+1, len(lines[y])):
                if int(lines[yi][x]) >= int(lines[y][x]) or yi == len(lines[y])-1:
                    score *= yi - y
                    break
            if score > best:
                best = score
    print(best)


if __name__ == '__main__':
    with open('input') as f:
        b(f.read().split('\n')[:-1])
