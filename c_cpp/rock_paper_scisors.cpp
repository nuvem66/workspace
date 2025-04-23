#include <iostream>
#include <ctime>
#include <unordered_set>
#include <cstdlib>

int winStreak = 0;
int totalWins = 0;
int totalLosses = 0;

char getComputerChoice () {
    char choices[] = {'r', 'p', 's'};
    return choices[std::rand() % 3];
}

char getUserChoice () {
    std::unordered_set<char> validChoices = {'r', 'p', 's'};
    std::string userInput;

    while (true) {
        std::cout << "| R | for Rock.\n| S | for Scissors.\n| P | for Paper.\nYour choice: ";
        std::cin >> userInput;
        if (userInput.length() == 1 && validChoices.count(tolower(userInput[0]))) {
            return tolower(userInput[0]);
        }
    }
}

void doGame(char userChoice, char computerChoice) {
    
    printf("Computer: %c\n", computerChoice);

    if (userChoice == computerChoice) {
        std::cout << "It's a draw!!!\n";
        return;
    };

    bool victory = (userChoice == 'r' && computerChoice == 's' ||
                    userChoice == 'p' && computerChoice == 'r' ||
                    userChoice == 's' && computerChoice == 'p');

    if (victory) {
        std::cout << "\n[=== CONGRATS!!! ===]\nYou've won this match!\n";
        winStreak ++;
        totalWins ++;
        return;
    }
    else {
        std::cout << "\n[===  DEFEAT...  ===]\nYou've lost this match...\n";
        winStreak = 0;
        totalLosses ++;
    }
}

int main () {
    srand(time(NULL));
    char keepRunning = 'y';
    std::cout 
            << "#################################\n"
            << "###### Rock Paper Scissors ######\n"
            << "#################################\n\n";
    do {
        doGame (getUserChoice(), getComputerChoice());
        printf("Win Streak: %d\tTotal victories: %d\n\n", winStreak, totalWins);
        
        std::cout << "Keep playing? Y/n: ";
        std::cin >> keepRunning;
        keepRunning = tolower(keepRunning);

        if (keepRunning == 'n') {
            break; 
        }
    
    } while (true);

    std::cout << "Thank you for playing!\n";
    
    return 0;
}