import os
import math 
import time

its4am = ""

def add(a,b):
    a = float(a)
    b = float(b)
    return a + b

def sub(a,b):
    a = float(a)
    b = float(b)
    return a - b

def mult(a,b):
    a = float(a)
    b = float(b)
    return a * b

def div(a,b):
    a = float(a)
    b = float(b)
    if b != 0:
        return a / b
    else:
        print("Operação inválida.")

def exp(a,b):
    a = float(a)
    b = int(b)
    return a ** b

def root(a):
    a = int(a)
    if a != 0:
        return math.sqrt(a)
    else:
        print("Operação inválida.")

def get_super(x): 
    normal = "0123456789"
    super_s = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    res = x.maketrans(''.join(normal), ''.join(super_s)) 
    return x.translate(res) 

main_text = "Selecione: \n1. ADICIONAR(A+B)\n2. SUBTRAIR(A-B)\n3. MULTIPLICAR(A*B)\n4. DIVIDIR(A/B)\n5. EXPONENCIAR(A^B)\n6. RAÍZ QUADRADA(√A)\n0. SAIR\n\nOpção: "

def wich():
    while True:
        try:
        # tries infinitelly until it gets an integer between 1 and 6        
            choice = int(input(main_text))
            break

        except:
        # gets errors
            print("Essa não é uma opção válida!")
            time.sleep(2)
            os.system('clear')
    
    if choice == 1:
        while True:
        #almost the same as before
            try:
                a = input('Valor de "A": ')
                b = input('Valor de "B": ')
                print(f"{a} + {b} = {add(a, b)}") 
                break
            except:
                print("Input inválido!")
                time.sleep(2)
                os.system('clear')
                print(main_text+"1")

    elif choice == 2:
        while True:
            try:
                a = input('Valor de "A": ')
                b = input('Valor de "B": ')
                print(f"{a} - {b} = {sub(a, b)}")  
                break
            except:
                print("Input inválido!")
                time.sleep(2)
                os.system('clear')
                print(main_text+"2")

    elif choice == 3:
        while True:
            try:
                a = input('Valor de "A": ')
                b = input('Valor de "B": ')
                print(f"{a} * {b} = {mult(a, b):.2f}")  
                break
            except:
                print("Input inválido!")
                time.sleep(2)
                os.system('clear')
                print(main_text+"3")

    elif choice == 4:
        while True:
            try:
                a = input('Valor de "A": ')
                b = input('Valor de "B" (B ≠ 0): ')
                print(f"{a} / {b} = {div(a, b):.2f}")
                break
            except:
                print("Input inválido!")
                time.sleep(2)
                os.system('clear')
                print(main_text+"4")
         
    elif choice == 5:
        while True:
            try:
                a = input('Valor de "A": ')
                b = input('Valor de "B" (B ∈ ℕ0): ')
                print(f"{a}{get_super(b)} = {exp(a, b):.2f}")
                break
            except:
                print("Input inválido!")
                time.sleep(2)
                os.system('clear')
                print(main_text+"5")

    elif choice == 6:
        while True:
            try:
                a = input('Valor de "A" (A ∈ ℕ0): ')
                # all of the a and b repetitions above only exists because of this part
                print(f"√{a} = {root(a):.2f}")
                break
            except:
                print("Input inválido!")
                time.sleep(2)
                os.system('clear')
                print(main_text+"6")
    
    elif choice == 0:
        running = ""
        

    else:
        print("Essa não é uma opção válida!")
        time.sleep(2)
        os.system('clear')
        return wich()

os.system('clear') 
# does the screen-cleaning magic!

running = "n"
while running == "n":
    # basic program loop
    wich()
    running = str(input("\nDeseja sair? S/n\n").lower())

    os.system('clear')

    if running != "n":

        print(its4am+"\nPrograma finalizado.")
        exit() 
    
   

    