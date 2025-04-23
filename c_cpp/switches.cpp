#include <iostream>
#include <cstring>
// Switches are an alternative to using many "else if" statements!

int main () {
    int day;
    double completion = 14.3;
    std::cout << "Qual dia da semana é hoje?";
    std::cin >> day;
    
    switch (day) {
    // "char" also works, but I didn't manage to use "std::string" in cases
        case 1:
            completion *= 1;
            break;
        case 2:
            completion *= 2;
            break;
        case 3:
            completion *= 3;
            break;
        case 4:
            completion *= 4;
            break;
        case 5:
            completion *= 5;
            break;
        case 6:
            completion *= 6;
            break;
        case 7:
            completion = 100;
            break;
        default:
            std::cout << '\n' << "Hey! Type only weekdays (1-7)!";
            break;
    }
    std::cout << '\n' << "The week is " << completion << "\% complete!";
    return 0;
}