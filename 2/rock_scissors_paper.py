from util.constant_set import ConstantSet


class MATERIAL(ConstantSet):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"
abc_to_material = {
    "A":MATERIAL.ROCK,
    "B":MATERIAL.PAPER,
    "C":MATERIAL.SCISSORS
}
xyz_to_material = {
    "X":MATERIAL.ROCK,
    "Y":MATERIAL.PAPER,
    "Z":MATERIAL.SCISSORS
}
mat_value = {
    MATERIAL.ROCK:1,
    MATERIAL.PAPER:2,
    MATERIAL.SCISSORS:3
}

class STRATEGY(ConstantSet):
    WIN= 'Z'
    DRAW='Y'
    LOSE='X'

def score(a:MATERIAL, b:MATERIAL):
    if a==b:
        return 3
    if a==MATERIAL.SCISSORS and b==MATERIAL.PAPER:
        return 0
    if a==MATERIAL.PAPER and b==MATERIAL.ROCK:
        return 0
    if a==MATERIAL.ROCK and b==MATERIAL.SCISSORS:
        return 0
    return 6

def get_score_no_strategy():
    v=0
    for line in open("input.txt"):
        line = line.strip("\n")
        abc,xyz = line.split()
        mat1=abc_to_material[abc]
        mat2=xyz_to_material[xyz]
        v1 = mat_value[mat2]
        v2 = score(mat1,mat2)
        v+=v1+v2
    print(v)

def get_mat_for_strategy(mat1:MATERIAL, strat:STRATEGY):
    if strat==STRATEGY.WIN:
        if mat1 == MATERIAL.SCISSORS:
            return MATERIAL.ROCK
        elif mat1 == MATERIAL.ROCK:
            return MATERIAL.PAPER
        elif mat1 == MATERIAL.PAPER:
            return MATERIAL.SCISSORS
    elif strat==STRATEGY.LOSE:
        if mat1 == MATERIAL.SCISSORS:
            return MATERIAL.PAPER
        elif mat1 == MATERIAL.ROCK:
            return MATERIAL.SCISSORS
        elif mat1 == MATERIAL.PAPER:
            return MATERIAL.ROCK
    elif strat==STRATEGY.DRAW:
        return mat1

def get_score_with_strategy():
    #column2 = strategy
    v=0
    for line in open("input.txt"):
        line = line.strip("\n")
        abc,xyz = line.split()
        mat1=abc_to_material[abc]
        strat=xyz
        mat2=get_mat_for_strategy(mat1,xyz)
        v1 = mat_value[mat2]
        v2 = score(mat1,mat2)
        v+=v1+v2
    print(v)

get_score_no_strategy()
get_score_with_strategy()

