import randArray

numbers =  randArray.mkArray(10)

def get_mean(x):
    total = 0
    for n in x:
        total += n
    mean = total//len(x)
    return mean

def quick_sort(x):
    right = []
    left = []

    piv = get_mean(x)

    if len(x) <= 1 or (len(x) == 2 and x[0] == x[1]):
         return x # Breaks the recursion
    
    for i in x:
        if i > piv:
                right.append(i)
        elif i <= piv:
                left.append(i)
    
    return quick_sort(left) + quick_sort(right)
        

    

print(f'Unsorted:     {numbers}')
print(f'Quick-sorted: {quick_sort(numbers)}')