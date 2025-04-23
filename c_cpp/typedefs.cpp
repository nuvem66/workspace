#include <iostream>
#include <vector>

typedef std::vector<std::pair<std::string, int>> pairlist_t;
// Using "_t" for typedefs is a convention.

typedef std::string text_t;
// typedef ˜datatype˜ ˜alias˜;

using text2_t = std::string;
// using ˜alias˜ = ˜datatype˜;

int main(){
	// Typedef is a reserved keyword used to create aliases for
	// another datatype. It improves readability and reduces
	// typos!

	pairlist_t new_pairlist;
	
	text_t lizards = "Lizards are cool as heck.";
	std::cout << lizards << '\n';
	
	// They have been replaced a lot by the "using" keyword tho
	
	text2_t foxes = "Foxes are also cool as heck!";
	std::cout << foxes << '\n';
	
	return 0;	
}