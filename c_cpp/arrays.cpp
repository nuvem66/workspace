#include <iostream>
#include <string>

int main () {
    
    /* An array is a data structure that can hold multiple values. Each one is accessed 
    by an "index".
    Arrays have a fixed size!!!
    "kind of like a variable that holds multiple values" */
    
    std::string characters[] = {"Catra", "Adora", "Double Trouble"};
    // An array can only contain one type of data!
    
    std::cout << characters << '\n'; // Memory adress of the array!
    std::cout << characters[1] << '\n'; // Now, we're accessing a value in the array.
    std::cout << characters[-1] << '\n'; // Unlike Python, can't do this (returns nothing, except for the '\n')
    
    // Reazoomssigning values:
    characters[2] = "Glimmer";
    std::cout << characters[2] << '\n'; // Memory adress of the array!
    
    // To declare an array without giving it values, we need to set a fixed size.
    std::string swords[5]; // Can take 5 strings.
    swords[0] = "Rapier";
    swords[1] = "Kodachi";
    swords[2] = "Katana";
    
    std::cout << swords[0] << '\n';
    std::cout << swords[1] << '\n';
    std::cout << swords[2] << '\n';
    
    return 0;
}




