import random
# function for twenty sided dice
def twenty():
    icos = random.randint(1,20)
    if icos == 20:
        print (icos, 'Critical Success!')
    elif icos == 1: 
        print (icos, 'Critical Failure')
    else:
        print (icos)
# function for twelve sided dice
def twelve():
    dode = random.randint(1,12)
    print(dode)
# function for ten sided dice
def ten():
    deca = random.randint(1,10)
    print(deca)
# function for eight sided dice
def eight():
    octa = random.randint(1,8)
    print(octa)
# function for six sided dice
def six():
    hexa = random.randint(1,6)
    print(octa)
# function for four sided dice
def four():
    tetra = random.randint(1,4)
    print(tetra)
# function for one-hundred sided dice
def onehun():
    zocc = random.randint(0,100)
    print(zocc)