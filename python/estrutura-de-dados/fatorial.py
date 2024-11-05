def fator(a):
    b = a
    progression = []

    # [1,..., n-3, n-2, n-1]
    for i in range(b - 1):
        progression.append(i + 1)

    # a = a * (a-1) * (a-2)* ...* 1
    for term in progression:
        a = term * a

    return a

def fatorRecur(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * fatorRecur(a-1)

print(fatorRecur(5))
