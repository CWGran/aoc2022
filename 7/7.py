import re

command_pat = r'\$\s(\w+)([^\n]*)\n'


def get_results(string):
    res = []
    for l in string.split('\n'):
        if l != '' and l[0] == '$':
            break
        res.append(l)
    return res


def cd(dirs, wd):
    for d in wd:
        dirs = dirs[d][1]
    return dirs


def get_structure(commands):
    dirs = {'/': (0, {})}
    wd = ['/']
    pwd = dirs['/']
    for command in re.finditer(command_pat, commands):
        op, *args = command.groups()
        if op == 'cd':
            arg = args[0].strip()
            if arg == '/':
                wd = ['/']
                pwd = dirs['/'][1]
            elif arg == '..':
                if wd[-1] != '/':
                    wd = wd[:-1]
                    pwd = cd(dirs, wd)
            else:
                wd.append(arg)
                pwd = pwd[arg][1]

        elif op == 'ls':
            res = get_results(commands[command.end():])
            for r in res:
                if r == '':
                    break
                a, b = r.split(' ')
                if a == 'dir':
                    pwd[b] = (0, {})
                else:
                    pwd[b] = (1, int(a))

    return dirs


def du(tree):
    if tree is None:
        return 0

    dirs = []
    size = 0
    for i in tree:
        if tree[i][0] == 0:
            s, d = du(tree[i][1])
            dirs += d
            dirs.append(s)
            size += s
        else:
            size += tree[i][1]

    return size, dirs


def a(commands):
    dirs = get_structure(commands)
    size, dirs = du(dirs)

    total = 0
    for d in dirs:
        if d <= 100000:
            total += d

    print(total)


def b(commands):
    dirs = get_structure(commands)
    size, dirs = du(dirs)

    req = 40000000
    for i, d in enumerate(sorted(dirs)):
        if size - d < req:
            print(d)
            break


if __name__ == '__main__':
    with open('input') as f:
        b(f.read())
