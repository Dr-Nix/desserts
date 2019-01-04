/*
 * Veld.cpp
 *
 *  Created on: Jan 3, 2019
 *      Author: boris
 */

#include "Veld.h"

Veld::Veld(const int rows, const int cols)
        : d_rows(rows), d_cols(cols), d_filled(0)
{
    for (int r = 0; r < rows; r++)
    {
        d_tegels.push_back(std::vector<Tegel*>(cols, nullptr));
    }

}

Veld::~Veld()
{
    // TODO Auto-generated destructor stub
}

Tegel *
Veld::get_tegel(int row, int col)
{
    if (row >= 0 and row < d_rows and col >= 0 and col > d_cols)
    {
        return d_tegels[row][col];
    }
    else
    {
        return nullptr;
    }
}

int
Veld::add_tegel(Tegel * t)
{
    if (d_filled == d_rows * d_cols)
    {
        return -1;
    }
    d_tegels[d_filled / d_cols][d_filled % d_cols] = t;
    d_filled++;
    return d_filled;
}

void
Veld::print()
{
    for (int r = 0; r < d_rows; r++)
    {
        std::cout << std::string(d_cols * 5, '*') << std::endl;

        for (int c = 0; c < d_cols; c++)
        {
            std::cout << "* " << d_tegels[r][c]->get_top() << " *";
        }
        std::cout << std::endl;
        for (int c = 0; c < d_cols; c++)
        {
            std::cout << "*"
                      << d_tegels[r][c]->get_left()
                      << " "
                      << d_tegels[r][c]->get_right()
                      << "*";
        }
        std::cout << std::endl;
        for (int c = 0; c < d_cols; c++)
        {
            std::cout << "* " << d_tegels[r][c]->get_bottom() << " *";
        }
        std::cout << std::endl;
        std::cout << std::string(d_cols * 5, '*') << std::endl;
    }
}
