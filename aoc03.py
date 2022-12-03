
def get_inputs(path):
    rucksacks = []
    with open(path, 'r') as file:
        rucksacks = [line.strip() for line in file]

    return rucksacks


def get_sum(same):
    val = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = 0
    for c in same:
        res += val.index(c)+1
    return res


def find_item(rucks):
    same = []
    for ruck in rucks:
        comp1 = ruck[0:len(ruck)//2]
        comp2 = ruck[len(ruck)//2:]
        for c in comp1:
            if c in comp2:
                same.append(c)
                break

    return get_sum(same)


def find_threes(rucks):
    same = []
    for i in range(len(rucks)//3):
        r1 = rucks[3*i]
        r2 = rucks[3*i+1]
        r3 = rucks[3*i+2]
        for c in r1:
            if c in r2 and c in r3:
                same.append(c)
                break
    
    return get_sum(same)


if __name__ == "__main__":
    rucks = get_inputs("inputs/day03")
    #rucks = get_inputs("test/test03")

    print(find_item(rucks), find_threes(rucks))
