
def get_inputs(path):
    data = []
    with open(path, 'r') as file:
        data = [line.strip().split(",") for line in file]
    
    pairs = []
    for p in data:
        a, b = map(int, p[0].split("-"))
        c, d = map(int, p[1].split("-"))
        pairs.append((a, b, c, d))

    return pairs


def find_full_overlap(pairs):
    res = 0
    for a, b, c, d in pairs:
        if (a <= c and b >= d) or (c <= a and d >= b):
            res += 1

    return res


def in_interval(x, y, z):
    return y <= x and x <= z


def find_partial_overlap(pairs):
    res = 0
    for a, b, c, d in pairs:
        if in_interval(a, c, d) or  in_interval(b, c, d) or in_interval(c, a, b) or in_interval(d, a, b):
            res += 1

    return res


if __name__ == "__main__":
    pairs = get_inputs("inputs/day04")
    #pairs = get_inputs("test/test04")

    print(find_full_overlap(pairs))
    print(find_partial_overlap(pairs))

