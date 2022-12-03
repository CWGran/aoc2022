def a(data):
    max = 0
    sum = 0
    for l in data.split('\n'):
        if l == '':
            if sum > max:
                max = sum
            sum = 0
        else:
            sum += int(l)
    print(max)
    

def b(data):
    elves = []
    sum = 0
    for l in data.split('\n'):
        if l == '':
            elves.append(sum)
            sum = 0
        else:
            sum += int(l)
    top = sorted(elves, reverse=True)[:3]
    print(top[0] + top[1] + top[2])

if __name__ == '__main__':
    with open('input') as f:
        b(f.read())
