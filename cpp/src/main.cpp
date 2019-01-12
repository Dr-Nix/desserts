//============================================================================
// Name        : desserts-cpp.cpp
// Author      : Boris
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

//#include <iostream>
//#include <string>

#include "veld.h"
#include "tegel.h"

int main() {
    Tegel t1 = Tegel(Tegel::dessert::hoorntje,
                     Tegel::dessert::ijsschaal,
                     Tegel::dessert::soesje,
                     Tegel::dessert::taart);
    using D = Tegel::dessert;
    Tegel t2 = Tegel(D::hoorntje, D::soesje, D::taart, D::muffin);
    Tegel t3 = Tegel(D::coupe, D::rode_coupe, D::soesje, D::muffin);
    Tegel t4 = Tegel(D::rode_coupe, D::ijsschaal, D::coupe, D::softijs);
    Veld v = Veld(2, 2);

    v.add_tegel(&t1);
    v.add_tegel(&t2);
    v.add_tegel(&t3);
    v.add_tegel(&t4);
    v.print();

    return 0;
}
