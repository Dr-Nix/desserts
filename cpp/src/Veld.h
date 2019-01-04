/*
 * Veld.h
 *
 *  Created on: Jan 3, 2019
 *      Author: boris
 */

#ifndef VELD_H_
#define VELD_H_

#include <iostream>
#include <vector>
#include "Tegel.h"

class Veld
{
    public:
        Veld(const int rows, const int cols);
        virtual ~Veld();
        Tegel * get_tegel(int row, int col);
        int add_tegel(Tegel *t);
        void print();

    private:
        int d_rows;
        int d_cols;
        std::vector<std::vector<Tegel *>> d_tegels;
        int d_filled;
};

#endif /* VELD_H_ */
