#include <iostream>

int main(){
	std::cout << "hello, world!" << '\n';
	/*
	standard namespace :: char output
	/'/n' is the same as std::endl
	*/
	
	// Variables:
	int my_variable;  // 1) Declaration
	my_variable = 10; // 2) Assignment
	
	int other_variable = 99; // Both steps!
	
	int sum = my_variable + other_variable;
	
	std::cout << "the sum is " << sum << '\n';	
		
	return 0; //returns 0 if done	
}