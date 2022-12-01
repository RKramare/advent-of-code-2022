
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [line.strip() for line in file]

    return inputs


def get_a(inps):
    
    highest = -1
    curr_tot = 0
    for x in inps:
        if x:
            curr_tot += int(x)
        else:
            if curr_tot > highest:
                highest = curr_tot
            curr_tot = 0
    return highest


def get_b(inps):
    res = []
    curr = 0
    while inps:
        x = inps.pop(0)
        if x:
            curr += int(x)
        else:
            res.append(curr)
            curr = 0
    res.sort()

    print(res[-3:])

    return sum(res[-3:])



if __name__ == "__main__":
    tmp = get_inputs("inputs/day01")
    #tmp = get_inputs("test/test01")

    #print(tmp)
    print(get_b(tmp))

