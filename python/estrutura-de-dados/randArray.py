import random

def mkArray(size):
    array = []

    for i in range(size):
        array.append(random.randint(-50,50))

    return array

def mkArray2(size):
    array = []

    for i in range(size):
        x = random.randint(-50,50)
        if x not in array:
            array.append(x)

    return array