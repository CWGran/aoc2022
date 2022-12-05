import re


def get_containers(lines):
    indices = {}
    containers = {}

    for m in re.finditer(r'\w', lines[-1]):
        indices[m.start()] = m.group(0)
        containers[m.group(0)] = []

    for l in lines[:-1]:
        for m in re.finditer(r'\w', l):
            containers[indices[m.start()]].append(m.group(0))

    return containers


def a(lines):
    containers = get_containers(lines[:9])

    for instruction in lines[10:]:
        x, y, z = re.match(r'move (\d+) from (\d+) to (\d+)', instruction).groups()
        containers[z] = list(reversed(containers[y][:int(x)])) + containers[z]
        containers[y] = containers[y][int(x):]

    res = ""
    for k in containers.keys():
        res += containers[k][0]
    print(res)


def b(lines):
    containers = get_containers(lines[:9])

    for instruction in lines[10:]:
        x, y, z = re.match(r'move (\d+) from (\d+) to (\d+)', instruction).groups()
        containers[z] = list(containers[y][:int(x)]) + containers[z]
        containers[y] = containers[y][int(x):]

    res = ""
    for k in containers.keys():
        res += containers[k][0]
    print(res)


if __name__ == '__main__':
    with open('input') as f:
        b(f.read().split('\n')[:-1])
