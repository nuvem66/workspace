values = [10,20,30,40,50]
values.append(values[-1]-90)

print(values)

n = values[-1]

if n < 0:
    print(f"{values} is a negative number.")
elif n == 0:
    print(f"{n} is a neutral number (0).")
else:
    print(f"{n} is a positive number.")