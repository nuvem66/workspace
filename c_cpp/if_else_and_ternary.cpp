#include <iostream>

int main()
{
    // if statements!
    int age;
    bool is_legal;
    std::cout << "Enter your age: ";
    std::cin >> age;
    
    if(age <= 0){
      std::cout << '\n' << "You haven't been born yet!";
    } else if(age >= 18){
        is_legal = true;
        std::cout << '\n' << "biiiig boi";
    } else{
        is_legal = false;
        std::cout << '\n' << "small boi";
    }
    if(age == 19){
        std::cout << '\n' << "You're me!!! (but I'm not big...)";
    }
    //ternary operators are shorthands for if/else statements where you only do 1 thing!
    is_legal ? std::cout << "\nYou can enter." : std::cout << "\nYeah, you can't be here!";
    
    return 0;
}
