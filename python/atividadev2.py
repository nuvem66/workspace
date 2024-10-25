import random
#random methods module for the rng

numbers = []
even = []
odd = []

for i in range(10): 
 rng = random.randint(-100,100)
 numbers.append(rng)
print(f"Array: {numbers}\n")
numbers.sort() #it's prettier now

for number in numbers:
  if number % 2 == 1:
    odd.append(number)
  elif number % 2 == 0:
    even.append(number)

print(f"Biggest: {numbers[-1]}\nSmallest: {numbers[0]}\n{len(even)} even numbers: {even}\n{len(odd)} odd numbers: {odd}")

