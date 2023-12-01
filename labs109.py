# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

# 1
def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


# 3
def riffle(items, out=True):
    if len(items) < 1:
        return []
    mid = len(items) // 2
    first_half = items[:mid]
    second_half = items[mid:]
    shuffled = []
    for i in range(mid):
        if out:
            shuffled.append(first_half[i])
            shuffled.append(second_half[i])
        else:
            shuffled.append(second_half[i])
            shuffled.append(first_half[i])
    return shuffled


# 4
def only_odd_digits(n):
    odd = True
    while odd:
        last_digit = n % 10
        n = n // 10
        if last_digit % 2 == 0:
            odd = False
        elif n <= 0:
            break
    return odd


# 5
def is_cyclops(n):
    n = str(n)
    if len(n) % 2 == 0:
        return False
    mid = len(n) // 2
    if n[mid] != str(0):
        return False
    for index, digit in enumerate(n):
        digit = int(digit)
        if digit == 0 and index != mid:
            return False
    return True


# 6
def domino_cycle(tiles):
    if len(tiles) < 1:
        return True
    if len(tiles) == 1:
        if tiles[0][0] == tiles[0][1]:
            return True
        else:
            return False
    if tiles[-1][1] != tiles[0][0]:
        return False
    for i in range(len(tiles) - 1):
        if tiles[i][1] != tiles[i + 1][0]:
            return False
    return True


# 7
def color_trio(colours):
    combinations = {
        'rr': 'r',
        'rb': 'y',
        'ry': 'b',
        'bb': 'b',
        'br': 'y',
        'by': 'r',
        'yy': 'y',
        'yb': 'r',
        'yr': 'b'
    }
    new_str = ""
    if len(colours) == 1:
        return colours
    for i in range(len(colours) - 1):
        tmp = colours[i] + colours[i + 1]
        if tmp in combinations:
            new_str += combinations[tmp]
    return new_str


