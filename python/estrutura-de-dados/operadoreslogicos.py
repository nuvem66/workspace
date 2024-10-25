lotofnumbers = [98,12,0,1,4,6,764,2,4123,5,34]
l = len(lotofnumbers) 
oldl = l

print(f"[lotofnumbers] has {l} numbers inside itself.\n")

for n in lotofnumbers:
    
    
    #newl = oldl - l
    #l = l - 1

    if n != 0:
        if n % 2 == 1:
            print(f"{n} is odd and it has {newl} as its index.")
        else: 
            print(f"{n} is even and it has {newl} as its index.")
    else: 
        print(f"{n} is neither even or odd and it has {newl} as its index.")
