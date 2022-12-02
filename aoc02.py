
def get_inputs(path):
    guide = []
    with open(path, 'r') as file:
        guide = [line.strip().split(" ") for line in file]

    return guide


def get_point(e, y):
    point = {
        "Rock" : 1,
        "Paper" : 2,
        "Scissor" : 3,
    }
    game = {
        ("Rock", "Scissor") : 0,
        ("Paper", "Rock") : 0,
        ("Scissor", "Paper") : 0,
        ("Rock", "Rock") : 3,
        ("Paper", "Paper") : 3,
        ("Scissor", "Scissor") : 3,
        ("Rock", "Paper") : 6,
        ("Paper", "Scissor") : 6,
        ("Scissor", "Rock") : 6
    }
    return game[(e, y)] + point[y]


def get_rule1(guide):
    symbols = {
        "A" : "Rock",
        "B" : "Paper",
        "C" : "Scissor",
        "X" : "Rock",
        "Y" : "Paper",
        "Z" : "Scissor",
    }
    res = 0

    for elf, you in guide:
        e = symbols[elf]
        y = symbols[you]        
        res += get_point(e, y)

    return res


def get_rule2(guide):
    symbols = {
        "A" : "Rock",
        "B" : "Paper",
        "C" : "Scissor"
    }
    res = 0

    for elf, you in guide:
        e = symbols[elf]
        if you == "X": #lose
            if e == "Rock":
                y = "Scissor"
            elif e == "Paper":
                y = "Rock"
            elif e == "Scissor":
                y = "Paper"
        elif you == "Y": #draw
            y = e
        elif you == "Z": #win
            if e == "Rock":
                y = "Paper"
            elif e == "Paper":
                y = "Scissor"
            elif e == "Scissor":
                y = "Rock"

        res += get_point(e, y)

    return res


if __name__ == "__main__":
    guide = get_inputs("inputs/day02")
    #guide = get_inputs("test/test02")

    print(get_rule1(guide), get_rule2(guide))
