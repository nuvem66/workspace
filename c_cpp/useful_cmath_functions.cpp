
// Online C++ Compiler - Build, Compile and Run your C++ programs online in your favorite browser

#include <iostream>
#include <cmath>
// Useful info: https://cplusplus.com/reference/cmath/

int main()
{
    double x = 4;
    double y = 5;
    double z;
    
    const double pi = 3.141592653589793;
    
    // std::max() Returns the biggest value.
    z = std::max(x,y);
    std::cout << "max(x,y) = " << z << '\n';
    
    // std::min() Returns the smallest value.
    z = std::min(x,y);
    std::cout << "min(x,y) = " << z << '\n';
    
    // pow() ~> "Power"
    z = pow(x, 3);
    std::cout << "pow(x, 3) = x³ = " << z << '\n';
    
    // sqrt() ~> "Square Root"
    z = sqrt(512);
    std::cout << "sqrt(512) = 512^(1/2) = " << z << '\n';
    
    // abs() ~> "Absolute Value"
    z = abs(-15);
    std::cout << "abs(-15) = |-15| = " << z << '\n';
    
    // round() ~> Changes value to the nearest integer
    z = round(y/x*pi);
    std::cout << "round(y/x*pi) = " << z << '\n';
    
    // ceil() ~> Changes value to the next integer (always rounds up)
    z = ceil(y/x*pi);
    std::cout << "ceil(y/x*pi) = " << z << '\n';
    
    // floor() ~> Changes value to the previous integer (always rounds down)
    z = floor(y/x*pi);
    std::cout << "floor(y/x*pi) = " << z << '\n';
    
    return 0;    
}