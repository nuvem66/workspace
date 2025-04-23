#include <iostream>

int main()
{
	// Const keyword and Operations
	const double PI = 3.14159; 
	// UPPERCASE to constants is a convention 
	double radius = 7;
	
	double circumference = 2 * PI * radius;
	
	std::cout << "Circumference: " << circumference << "cm" << '\n';
	
	radius = 15; // it's ok
	// PI = 3 would return an error! PI is read-only
	circumference = 2 * PI * radius; // doing the calc again
	
	std::cout << "Bigger Circumference: " << circumference << "cm" << '\n';
	
	return 0;
}