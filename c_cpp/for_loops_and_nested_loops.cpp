#include <iostream>

int main () {

    // "for (initialization; stopping condition; thing to do) {}"

    // "for" loops are good when you *know* the number of times
    // you'll repeat a given block of code!

    for (int index = 0; index <= 5; index++){
        std::cout << "Iteration Nº." << index << '\n';
    
    }
    
    // A nested loop is just a loop inside another loop
    
    int length;
    int height;
    char symbol;

    std::cout << "Type the length of your rectangle: ";
    std::cin >>  length;

    std::cout << "Type the height of your rectangle: ";
    std::cin >> height;

    std::cout << "Type the symbol you want to use to build your rectangle: ";
    std::cin >> symbol;

    for (int i = 0; i <= height; i++) {
        for (int j = 0; j <= length; j++) {
        // Using sequential characters is a convention for
        // nesting "i" ~> "j" ~> "k" ...
            std::cout << " " << symbol << " ";    
        }
        
        std::cout << '\n';
    }

    return 0;
}