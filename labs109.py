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
# def colour_trio(colours):
#     combinations = {
#         'rr': 'r',
#         'rb': 'y',
#         'ry': 'b',
#         'bb': 'b',
#         'br': 'y',
#         'by': 'r',
#         'yy': 'y',
#         'yb': 'r',
#         'yr': 'b'
#     }
#     while len(colours) > 1:
#         new_str = ""
#         for i in range(len(colours) - 1):
#             tmp = colours[i] + colours[i + 1]
#             new_str += combinations[tmp]
#         colours = new_str
    
#     return colours

# 7
def colour_trio(colours):
    options = "byr"
    while len(colours) > 1:
        new_str = ""
        for i in range(len(colours) - 1):
            if colours[i] == colours[i + 1]:
                new_str += colours[i]
            else:
                tmp = colours[i] + colours[i + 1]
                res = "".join(set(options) - set(tmp))
                new_str += res
        colours = new_str
    
    return colours


# 8
def count_dominators(items):
    max_item = items[-1]
    count = 1
    for i in range(len(items) - 2, -1, -1):
        if items[i] > max_item:
            max_item = items[i]
            count += 1
    return count


# 9
def extract_increasing(digits):
    digits = [int(x) for x in digits]
    extracted = [digits[0]]
    i = 0
    while i < len(digits) - 1:
        if digits[i + 1] > extracted[-1]:
            extracted.append(digits[i + 1])
            i += 1
        else:
            combined = ""
            for j in range(i + 1, len(digits)):
                combined += str(digits[j])
                if int(combined) > extracted[-1]:
                    extracted.append(int(combined))
                    i = j
                    break
                if j == len(digits) - 1:
                    i = j
    return extracted

    



