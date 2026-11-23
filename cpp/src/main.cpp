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
#include "tegelzak.h"

int main() {
    Veld v = Veld(2, 2);
    Tegelzak tz(Tegelzak::set::VIER);

    v.add_tegel(tz.pak_tegel());
    v.add_tegel(tz.pak_tegel());
    v.add_tegel(tz.pak_tegel());
    v.print();

    return 0;
}
