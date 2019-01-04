//============================================================================
// Name        : desserts-cpp.cpp
// Author      : Boris
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

//#include <iostream>
//#include <string>

#include "Veld.h"

int main() {
    Tegel t1 = Tegel(1, 2, 3, 4);
    Tegel t2 = Tegel(0, 2, 4, 6);
    Tegel t3 = Tegel(5, 6, 7, 8);
    Tegel t4 = Tegel(9, 0, 0, 9);
    Veld v = Veld(2, 2);

    v.add_tegel(&t1);
    v.add_tegel(&t2);
    v.add_tegel(&t3);
    v.add_tegel(&t4);
    v.print();

    return 0;
}
