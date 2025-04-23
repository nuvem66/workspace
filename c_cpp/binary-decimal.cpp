#include <iostream>
#include <cmath>

long decimalToBinary (long num) {
    std::string result;
    while (num > 0) {
        num % 2 ? result.insert(0, "1") : result.insert(0, "0");
        num = floor(num/2);
        // std::cout << result << '\n';
    }
    return std::stol(result);
}

int binaryToDecimal (long num) {
    long result = 0;
    char current;
    std::string num_str = std::to_string(num);
    for (int i = 0; i < num_str.length(); i++) { 
        result += ((int) num_str[num_str.length() - i - 1] - '0') * pow(2, i);
        // see: https://stackoverflow.com/questions/5029840/convert-char-to-int-in-c-and-c
        
        // std::cout << i 
        //     << '\t' << num_str[num_str.length() - i - 1] 
        //     << '\t' << pow(2, i) 
        //     << '\t' << result  << '\n';
    }
    return result;
}

int main () {
    bool wannaLeave = false;
    long userNum;
    int option;

    std::cout << "########### Conversor Binário ###########\n\n";

    do {
        std::cout << "1) Converter decimal para binário.\n2) Converter binário para decimal.\n3) Sair.\nEscolha: ";
        std::cin >> option;
        // Fix the thing where it loops when receiving non-numerical datatypes
        switch (option) {
        case 1:
            std::cout << "Número no formato decimal: ";
            std::cin >> userNum;
            std::cout << userNum << "₁₀ = " << decimalToBinary(userNum) << "₂\n\n";
            break;
        case 2:
            std::cout << "Número no formato binário: ";
            std::cin >> userNum;
            std::cout << userNum << "₂ = " << binaryToDecimal(userNum) << "₁₀\n\n";
            break;
        case 3:
            std::cout << "Finalizando.\n";
            wannaLeave = 1;
            break;
        default:
            std::cout << "Opção inválida.\n\n";
        }
    } while (!wannaLeave);
    
    return 0;
}