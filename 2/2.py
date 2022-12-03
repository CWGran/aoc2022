scores = {
    'X': 1, # Rock
    'Y': 2, # Paper
    'Z': 3, # Scissors
    'AY': 6,
    'BX': 0,
    'AZ': 0,
    'CX': 6,
    'BZ': 6,
    'CY': 0,
    'AX': 3,
    'BY': 3,
    'CZ': 3
}


def a(lines):
    score = 0
    for l in lines:
        if l == '':
            break

        game = l.replace(' ', '')
        o, u = game
        
        score += scores[u]
        if o != u:
            score += scores[game]
    print(score)


def b(lines):
    score = 0
    for l in lines:
        if l == '':
            break

        o, r = l.split(' ')
        
        if r == 'X':
            if o == 'A':
                score += 3
            elif o == 'B':
                score += 1
            else:
                score += 2
        elif r == 'Y':
            score += 3
            if o == 'A':
                score += 1
            elif o == 'B':
                score += 2
            else:
                score += 3
        elif r == 'Z':
            score += 6
            if o == 'A':
                score += 2
            elif o == 'B':
                score += 3
            else:
                score += 1
    print(score)


if __name__ == '__main__':
    with open('input') as f:
        b(f.read().split('\n'))
