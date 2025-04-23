#include <iostream>

// Here are some hella cool "std::string" methods!!

int main () {
    std::string name;
    // ".empty()" (vazio) returns "true" or "false"
    while (name.empty() || name.length() < 3){
        std::cout << "Please enter your name: ";
        std::getline(std::cin, name);
    }
    
    // ".erase(start, end)" (apagar) deletes only a given portion of the string
    name.erase(1,1); // It's inclusive [start, end]
    
    // ".append()" (adicionar) adds something to the *end* of the string!
    name.append(" Meow Applesauce");
    std::cout << "\nHello " << name << "! Wanna clear your name? ";
    char answer;
    std::cin >> answer;
    
    // ".at()" (em) gets a specific index from the string
    std::cout << "\nYour initial: " << name.at(0);
    
    // ".insert(index, something)" adds something at a given index
    name.insert(0, "01 ");
    
    // ".find()" (procurar) searches for something in the string 
    // and returns an index for that thing (if found)
    std::cout << "\nThe index for the first [a] in your name: " << name.find("a");
    
    // ".clear()" (limpar) clears the string! Same as " = "" "
    if (answer == 'y' || answer == 'Y') {
        name.clear();
        std::cout << "\nName \"" << name << "\" cleared!";
    }
    
    return 0;
} 