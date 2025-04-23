#include <iostream>

int main () {

    // "break" (quebrar) = break out of a loop
    // "continue" (continuar) = skips an iteration 

    for (int i = 0; i <= 100; i++) {

        if (i == 4) {
            std::cout << "This one is a bad number!!\n";
            continue;
        } 
        
        else if (i > 10) {
            std::cout << "Done! I only want to count 10 numbers.\n";
            break;
        }

        std::cout << i << '\n';
    }

    return 0;
}