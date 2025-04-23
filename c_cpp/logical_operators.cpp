#include <iostream>

int main () {
    // and "&&"~> *Both* conditions have to be *true* (1,1)
    // or "||" ~> Only *one* condition has to be *true* (1,0  1,1  0,1)
    // not "!" ~> Reverts the logical state of its operand! (true ~> false, false ~> true)

    double temperature = -786;
    bool dead = false;
    
    if (temperature < -70 || temperature > 44) {
        std::cout << "hooman is ded.";
        dead = !dead;
    } else {
        std::cout << "hooman lives another day. for now.";
    }
    return 0;
    
}