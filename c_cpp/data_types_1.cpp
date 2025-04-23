#include <iostream>

int main(){
	// Integers
	int age = 19;
	int number_of_cups = 7;
	int wrong_type = 9.54; // Will be truncated
	
	std::cout << "age: " << age << '\n';
	std::cout << "cups: " << number_of_cups << '\n';
	std::cout << "wrong type: " << wrong_type << '\n';

	// Doubles
	double gravity = 9.87;
	double fun = 3;
	
	std::cout << "gravity: " << gravity << '\n';
	std::cout << "fun: " << fun << '\n';

	// Chars
	char initial = 'K'; // SINGLE QUOTES
	char currency = '$';
	// char error = "Kumi"; would return an overflow error!
	std::cout << "initial: " << initial << currency << '\n';
	
	// Boolean
	bool learning = true;
	bool powered = false;
	
	// Strings
	std::string name = "Pedro";
	std::string fruit = "Maracuja";
	
	std::cout << name << " likes " << fruit << '\n';
	
	return 0;
}
