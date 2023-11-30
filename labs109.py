# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

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



    