#include <iostream>
#include <cmath>

int main()
{
    // Creating our variables
    double side_a;
    double side_b;
    // double hypothenuse;
    
    std::cout << "This is a Hypothenuse calculator for right angled triangles." << '\n' << "First side's size: ";
    std::cin >> side_a; // See "user_input.cpp" for this line
    
    if (side_a < 0) {
        std::cout << '\n' << "You can't have a size with negative value!";
        return 0;
    }
    
    std::cout << '\n' << "Second side's size: ";
    std::cin >> side_b;
    
     if (side_b < 0) {
        std::cout << '\n' << "You can't have a size with negative value!";
        return 0;
    }
     
    // hypothenuse = sqrt(pow(side_a, 2) + pow(side_b, 2));
    
    std::cout << '\n' << "By using the formula \"a² + b² = c²\", the size of the hypothenuse is: " << sqrt(pow(side_a, 2) + pow(side_b, 2)) << " units!";
    
    return 0;
    
}