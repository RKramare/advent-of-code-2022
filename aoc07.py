import sys
sys.setrecursionlimit(1500)

def get_inputs(path):
    inputs = []
    with open(path, 'r') as file:
        inputs = [line.strip("\n").split(" ") for line in file]
    inputs.pop(0)
    return inputs


def navigate(inputs, tree, curr_dir="", prev_dirs=[]):
    if not inputs:
        prev_dir = prev_dirs.pop()
        if curr_dir not in tree[prev_dir][2]:
            tree[prev_dir][0] += tree[curr_dir][0]
            tree[prev_dir][2].append(curr_dir)
        return tree
    line = inputs.pop(0)
    # print(f"line: {line}, cur: {curr_dir}, pre:s: {prev_dirs}\n{tree}\n")
    
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..": #cd up
                prev_dir = prev_dirs.pop()
                if curr_dir not in tree[prev_dir][2]:
                    tree[prev_dir][0] += tree[curr_dir][0]
                    tree[prev_dir][2].append(curr_dir)
                return navigate(inputs, tree, prev_dir, prev_dirs)
            else: # cd down
                next_dir = curr_dir + line[2]
                if next_dir not in tree.keys():
                    tree[next_dir] = [0, [], []]
                prev_dirs.append(curr_dir)
                return navigate(inputs, tree, next_dir, prev_dirs)
        else: #ls
            return navigate(inputs, tree, curr_dir, prev_dirs)

    elif line[0] == "dir":
        d = curr_dir + line[1]
        if not d in tree[curr_dir][1]:
            tree[curr_dir][1].append(d)
        return navigate(inputs, tree, curr_dir, prev_dirs)

    else: # file
        s = int(line[0])
        tree[curr_dir][0] += s
        return navigate(inputs, tree, curr_dir, prev_dirs)
   

def get_sum(inputs):
    tree = navigate(inputs, {"/": [0, [], []]}, "/")

    r = tree["/"][0]
    t = 70000000
    free = 30000000

    space = max((t - r) - free, free - (t - r))
    print(f"f-val: {tree['/'][0]}, space: {space}")

    small = []    
    res = 0
    for v in tree.values():
        s = v[0]
        if s < 100000:
            res += s
        if s > space:
            small.append(s)
    print(small)

    return res, min(small)


if __name__ == "__main__":
    tmp = get_inputs("inputs/day07")
    #tmp = get_inputs("test/test07")

    print(get_sum(tmp))
    

 
"""
 {
    \: (24523, a, b, c)
    a:  (1003, b, e),
    b: (299)
    c: (133, d)
    d: (213)
    e: (1351, f)
    f: (123)
 }
"""