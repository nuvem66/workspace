#include <iostream>
#include <ctime>

/*
    Future ideas:
    - Different dificulties (ex: changing the number of tries and the range)
*/

int main () {

    srand(time(NULL));

    int num = rand() % 100; // This is the range
    int guess;
    int tries = 5;
    char keepPlaying;

    std::cout << "######## Number Guessing Game ########\nTry to guess the number between 0-100!\nYou have " << tries << " tries!\n";
    
    while (tries >= 0) {
        std::cout << "\nGuess the number: ";
        std::cin >> guess;

        if (guess == num) {
            std::cout << "\n[ YOU GUESSED IT RIGHT!!! ]\n";
            break;
        } 
        else if (guess > num) {
            std::cout << "Go lower!\n";
        } 
        else if (guess < num) {
            std::cout << "Go higher!\n";
        }

        tries--;
    }
    
    if (tries < 0) {
        std::cout << "You didn't manage to get it... The number was " << num << ", better luck next time!\n";
    }

    std::cout << "\nKeep playing? y/N: ";
    std::cin >> keepPlaying;
    std::cout << std::endl;

    if (keepPlaying == 'y' || keepPlaying == 'Y') {
        main();
    }

    return 0;
}