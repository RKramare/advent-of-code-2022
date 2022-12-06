
def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [line.strip("\n") for line in file]

    orders = []

    n = (len(inputs[0])+1)//4
    stacks = {i+1:[] for i in range(n)}

    for line in inputs:
        if "[" in line:
            for i in range(n):
                label = line[i*4+1]
                if label != " ":
                    stacks[i+1].append(label)
        elif "move" in line:
            line = line.split(" ")
            x, y, z = map(int, (line[1], line[3], line[5]))
            orders.append((x, y, z))

    return stacks, orders


def move_crate(stacks, fro, to):
    crate = stacks[fro].pop(0)
    stacks[to].insert(0, crate)
    return stacks


def get_top_9000(stacks, orders):
    for num, fro, to in orders:
        for n in range(num):
            stacks = move_crate(stacks, fro, to)
        
    toppest = ""
    for v in stacks.values():
        toppest += v[0]

    return toppest


def move_stack(stacks, num, fro, to):
    stack = stacks[fro][:num]
    stacks[fro] = stacks[fro][num:]
    stacks[to] = stack + stacks[to]
    return stacks


def get_top_9001(stacks, orders):
    for num, fro, to in orders:
        stacks = move_stack(stacks, num, fro, to)
        
    toppest = ""
    for v in stacks.values():
        toppest += v[0]

    return toppest

if __name__ == "__main__":
    stacks, orders = get_inputs("inputs/day05")
    # stacks, orders = get_inputs("test/test05")

    print(get_top_9001(stacks, orders))

