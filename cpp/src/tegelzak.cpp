/*
 * tegelzak.cpp
 *
 *  Created on: Jan 12, 2019
 *      Author: boris
 */

#include "tegelzak.h"
#include <random>
#include <algorithm>

Tegelzak::Tegelzak(set s = set::LEEG)
{
    using D = Tegel::dessert;
    if (s == set::VIER)
    {
        tegels.push_back(std::make_unique<Tegel>(D::muffin, D::taart, D::softijs, D::ijsschaal));
        tegels.push_back(std::make_unique<Tegel>(D::softijs, D::ijsschaal, D::muffin, D::taart));
        tegels.push_back(std::make_unique<Tegel>(D::softijs, D::ijsschaal, D::muffin, D::soesje));
        tegels.push_back(std::make_unique<Tegel>(D::muffin, D::softijs, D::rode_coupe, D::ijsschaal));
    }
}

void
Tegelzak::schud()
{
    std::random_device rd;
    std::mt19937 g(rd());

    std::shuffle(tegels.begin(), tegels.end(), g);
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
