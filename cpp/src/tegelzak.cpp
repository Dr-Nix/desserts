/*
 * tegelzak.cpp
 *
 *  Created on: Jan 12, 2019
 *      Author: boris
 */

#include "tegelzak.h"

Tegelzak::Tegelzak(set s = set::LEEG)
{
    using D = Tegel::dessert;
    if (s == set::VIER)
    {
        tegels.push_back(std::make_unique<Tegel>(D::hoorntje, D::soesje, D::taart, D::muffin));
    }
}

void
Tegelzak::schud()
{

}

std::unique_ptr<Tegel>
Tegelzak::pak_tegel()
{
    for (auto& tegel : tegels)
    {
        if (tegel)
        {
            return std::move(tegel);
        }
    }
    return nullptr;
}
