
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [line.strip() for line in file]

    return inputs


def get_top(cals):
    highest = -1
    curr_tot = 0
    for x in cals:
        if x:
            curr_tot += int(x)
        else:
            if curr_tot > highest:
                highest = curr_tot
            curr_tot = 0
    return highest


def get_top3(cals):
    res = []
    curr = 0
    while cals:
        x = cals.pop(0)
        if x:
            curr += int(x)
        else:
            res.append(curr)
            curr = 0
    res.sort()

    return sum(res[-3:])


if __name__ == "__main__":
    cals = get_inputs("inputs/day01")
    cals = get_inputs("test/test01")

    print("Highest:", get_top(cals))
    print("Total for top three:", get_top3(cals))
