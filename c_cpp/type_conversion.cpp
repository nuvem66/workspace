#include <iostream>

int main(){
	// type conversion = converter um valor de determinado tipo
	//                   de dado para outro.
	//                   Implicit = automático.
	//                   Explicit = "(˜new_datatype˜) ˜value˜".
	
	int x = 3.14158; // Essa é uma conversão implícita.
	std::cout << x << std::endl;
	
	double y = 3.14158; // Tudo normal por aqui.
	std::cout << y << std::endl;
		
	y = (int) y; // Essa é uma conversão explícita!
	std::cout << y << std::endl;
	
	// Mais exemplos abaixo:
	char z = 100; // Converte implicitamente usando ASCII!!!
	std::cout << z << std::endl;

	std::cout << (char) 120 << '\n';
	
	int correct = 7;
	int questions = 10;
	double score = correct/(double)questions * 100; 
	// Sem a conversão, seria uma divisão de inteiros com resultado 0!
	std::cout << score << "%";
	
	return 0; 
}