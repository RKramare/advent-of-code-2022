
def get_inputs(path):
    signal = []
    with open(path, 'r') as file:
        signal = file.readline().strip()

    return signal


def get_marker(signal, x):
    chars = ""
    for i, c in enumerate(signal):
        if len(chars) > x - 1:
            chars = ""
        elif c in chars:
            n = chars.index(c)
            chars = chars[n+1:] + c
        else:
            chars += c
            if len(chars) == x:
                return i + 1


if __name__ == "__main__":
    tmp = get_inputs("inputs/day06")
    #tmp = get_inputs("test/test06")

    print(get_marker(tmp, 4))
    print(get_marker(tmp, 14))
