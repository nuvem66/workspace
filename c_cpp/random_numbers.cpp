#include <iostream>
#include <ctime>

int main () {

    // Btw those are just pseudo-random. Not really random,
    // but random enought

    //"srand(~seed~)" the "seed" (semente) is the thing that generates
    // the number!
    
    srand(time(NULL));

    int rngNum = rand();

    std::cout << rngNum << '\n';

    // we can modify the range by using the remainder
    // ("%") operator!

    
    int sides;
    int numOfRolls = 1;
    int maxLoops = 5;
    do {
        std::cout << "How many sides the dice has? ";
        std::cin >> sides;
        
        std::cout << "How many rolls do you want to do? ";
        std::cin >> numOfRolls;

        if (sides < 3 || numOfRolls < 1) {
            std::cout << "That's not a possible number of sides or rolls for a real 3D dice!\n";
            std::cout << maxLoops << " more tries.\n";
        }
        maxLoops --;
        if (maxLoops < 0) {
            return 0;
        }
    } while ((sides < 3 || numOfRolls < 1) && maxLoops >= 0);
    
    for (int i = 0; i <= numOfRolls; i++) {
        std::cout << "Rolling the dice...\nThe number is: " << (rand() % sides) << "\n";
    }

    return 0;
}