#include <iostream>

int main(){
	// Arithmetic operators = return the result of a specific
	//                        arithmetic operation (+ - * /)
	int minus_seven = 1000;
	int lolipops = 999;
	// keys_pressed = keys_pressed + 1;
	// Same as:
	lolipops += 1; // 1000
	
	// And we can also use the increment operator (++):
	lolipops++; // 1001
	
	// Decrement operator is the same (--):
	minus_seven -= 6; // 994
	minus_seven--; // 993
	
	// Multiplication and division:
	lolipops*=3; // 3003
	lolipops/=5; // 600 (gets truncated)
	
	// You can get the remainder with modules!
	int remainder = lolipops % 7;
	
	std::cout << "Doces: " << lolipops << '\n';
	std::cout << "Quanto é? " << minus_seven << '\n';
	std::cout << "O restante: " << remainder << '\n';
	
	// Operadores possuem uma ordem de resolução:
	// 1) Parêntesis
	// 2) Multiplicação e divisão  
	// 3) Adição e subtração 
	int big_operation = 9 + 1 * 7 - 4 / 2 + 4 * (10/2);
	std::cout << big_operation << '\n';
	
	return 0;
}