#include <iostream>

void bakePizza(void){
    std::cout << "Here's your pizza!\n";
}

void bakePizza(std::string topping1){
    std::cout << "Here's your pizza with "
        << topping1 << " topping!\n";
}

void bakePizza(std::string topping1, std::string topping2){
    std::cout << "Here's your pizza with "
        << topping1 << " and " << topping2 
        << " toppings!\n";
}

// It's valid for functions to share the same name,
// by having a different set of parameters!
// function name + parameters = funtion signature!

int main(){

    bakePizza();
    bakePizza("pepperoni");
    bakePizza("pepperoni", "mushroom");

    return 0;
}