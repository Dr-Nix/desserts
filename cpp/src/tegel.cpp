/*
 * Tegel.cpp
 *
 *  Created on: Jan 3, 2019
 *      Author: boris
 */

#include "tegel.h"
#include <iostream>

Tegel::Tegel(dessert top, dessert right, dessert bottom, dessert left)
        : d_rotation(0)
{
    d_opdruk[0] = top;
    d_opdruk[1] = right;
    d_opdruk[2] = bottom;
    d_opdruk[3] = left;
}

Tegel::dessert
Tegel::get_top()
{
    return d_opdruk[d_rotation];
}

Tegel::dessert
Tegel::get_right()
{
    return d_opdruk[(1 + d_rotation) % 4];
}

Tegel::dessert
Tegel::get_bottom()
{
    return d_opdruk[(2 + d_rotation) % 4];
}

Tegel::dessert
Tegel::get_left()
{
    return d_opdruk[(3 + d_rotation) % 4];
}

std::vector<std::string>
Tegel::print_regels()
{
    std::vector<std::string> v;
    v.push_back("*****");
    v.push_back("* " + std::to_string(static_cast<int>(get_top())) + " *");
    v.push_back("*" + std::to_string(static_cast<int>(get_left()))
                + " "
                + std::to_string(static_cast<int>(get_right()))
                + "*");
    v.push_back("* " + std::to_string(static_cast<int>(get_bottom())) + " *");
    v.push_back("*****");
    return v;
}

void
Tegel::print()
{
    for (auto& regel : print_regels())
    {
        std::cout << regel << std::endl;
    }
}

int
Tegel::get_rotation()
{
    return d_rotation;
}

void
Tegel::set_rotation(int rot)
{
    d_rotation = rot % 4;
}
