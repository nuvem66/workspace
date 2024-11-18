#include <iostream>

int main() {
    int age = 21;
    int year = 2024;
    int days = 7.5;
    std::cout << age<< ", " << year << ", " << days << std::endl;
    // Days gets truncated, because its
    // a float!
}