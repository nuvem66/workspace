
// Online C++ Compiler - Build, Compile and Run your C++ programs online in your favorite browser

#include <iostream>
#include <cmath>

int binaryToDecimal(int binary){
    std::string binary_s = std::to_string(binary);
    std::string currentChar;
    int currentValue;
    int total = 0;
    
    for(int i = binary_s.length() - 1; i >= 0; i--){
        currentChar = binary_s[i];
        currentValue = std::stoi(currentChar);
        total += pow(2, i) * currentValue;
        std::cout << i << '\t' << total << '\t' << binary_s[i] <<'\n';
    
    }
    return 0;
}

int decimalToBinary(){
    return 0;
}

int main()
{
    int binary;
    int decimal;
    
    binaryToDecimal(1001010);
    
    return 0;
}
