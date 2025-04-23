#include <iostream>

/*
 Functions have a defined structure:
    "void" means it doesn't need to return anything! It can also be
    used as a parameter.
    "int" would mean it returns an int and so on

    the parameters are optional, they're used to make the 
    function aware of data outside of its scope. When you pass
    something while calling the function (like "funtionName(thing);")
    the thing is called an *argument*

    std::string functionName (type parameter) {
        blockOfCode;
        return stringDatatype;
    }

    I REALLY recomend you to read: https://cplusplus.com/doc/tutorial/functions/
*/

long factorial(long a) {
  // "long" is a datatype for biiiig numbers.
  if(a > 1) {
    return (a * factorial (a-1));
    // A function that calls itself is
    // a recursive one! 
  }
  else {return 1;}
  // the "return" keyword returns a value back to the spot where you called
  // the encompassing (include, abranger) function. It also stops the function,
  // indepently of where it is.
}

// by declaring the function before the main()
// function, we can write her later!
int sum(int a); // 1) Initialization

double area(double length, double height);
//   ^ again, this is the return type!!
// "void" means "no return"

// main () is the ONLY function called automatically!
int main () {

    std::cout << factorial(10) << '\n';
    std::cout << sum(100) << '\n';
    std::cout << area(9.56, 12.78) << '\n';
    return 0;
}

int sum (int a) { // 2) Definition
  if(a > 1){
    return (a + (sum(a - 1)));
  } else { return 1; }
}

double area(double length, double height) {
  return length * height;
}