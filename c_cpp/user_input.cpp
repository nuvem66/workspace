#include <iostream>

// cout << (insertion operator)
// cin >> (extraction operator)

int main(){
	
		std::string name;
		int age;
		
		std::cout << "Qual é seu nome? " << '\n'; 
		std::cin >> name;
		
		std::cout << "Qual é a sua idade? ";
		std::cin >> age;
		
		std::cout << "Seu nome é " << name << ". Você tem " << age << " anos." << '\n';
		// There's a problem with this: once you hit a space while using
		// std::cin >>, it stops reading that string! (or any data type)
		// The std::getline() function can help with this!
		
		// std::getline() ONLY WORKS WITH **STRINGS**!
		
		std::string full_name;
		std::cout << "Agora digita seu nome completo: " << '\n';
		std::getline(std::cin >> std::ws, full_name);
		// >> std::ws grants that we'll only get user input, instead of
		// getting the "\n" character from the buffer. 
		// (yeah, kinda confusing)
		
		std::cout << "Seu nome é \"" << full_name << "\". Você tem " << age << " anos.";
		
	
	return 0;
}
