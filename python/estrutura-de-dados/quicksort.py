import randArray

numbers = randArray.mkArray(10)

def get_mean(x):
    total = 0
    for n in x:
        total += n
    if total == 0:
        return 1
    mean = total//len(x)
    return mean

def quick_sort(x):
    left = []
    repeated = []
    right = []

    piv = get_mean(x)

    if len(x) <= 1:
         return x # Breaks the recursion
    
    for i in x:
        if i < piv:
            left.append(i)
        elif i == piv:
            repeated.append(i) 
        elif i > piv:
            right.append(i)
    return quick_sort(left) + repeated + quick_sort(right)

for i in range(10):
    numbers = randArray.mkArray(10)
    print(f'Unsorted:     {numbers}')
    print(f'Quick-sorted: {quick_sort(numbers)}\n')