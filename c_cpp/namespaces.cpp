#include <iostream>

namespace one{
	int x = 1;
}
namespace two{
	int x = 2;
}

int main()
{
	// Namespaces are aliases for existing datatypes and are used with ::
	using namespace one;
	std::cout<<"x is equal to "<<x<<'\n';
	std::cout<<"now, x is equal to "<<two::x<<'\n';
	
	// NEVER USE "using namespace std ...;" IT'S AN EVIL LINE!!!
	// If needed, prefer things like: 
	// "using std::cout;"
	// "using std::string;" ...
}