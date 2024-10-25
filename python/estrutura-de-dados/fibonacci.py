def fibonacci(n):
    a=2
    b=1
    c=1
    sequence=[0,1,1]
    for i in range(n):
        a=b+c
        sequence.append(a)
        c=b
        b=a
    return sequence

print(fibonacci(3))