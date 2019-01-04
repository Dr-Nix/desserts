/*
 * Tegel.cpp
 *
 *  Created on: Jan 3, 2019
 *      Author: boris
 */

#include "Tegel.h"

Tegel::Tegel(int top, int right, int bottom, int left)
        : d_rotation(0)
{
    d_opdruk[0] = top;
    d_opdruk[1] = right;
    d_opdruk[2] = bottom;
    d_opdruk[3] = left;
}

Tegel::~Tegel()
{
    // TODO Auto-generated destructor stub
}

int
Tegel::get_top()
{
    return d_opdruk[d_rotation];
}

int
Tegel::get_right()
{
    return d_opdruk[(1 + d_rotation) % 4];
}

int
Tegel::get_bottom()
{
    return d_opdruk[(2 + d_rotation) % 4];
}

int
Tegel::get_left()
{
    return d_opdruk[(3 + d_rotation) % 4];
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
