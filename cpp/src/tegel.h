/*
 * Tegel.h
 *
 *  Created on: Jan 3, 2019
 *      Author: boris
 */

#ifndef TEGEL_H_
#define TEGEL_H_

#include <string>
#include <vector>

class Tegel
{
    public:
        enum class dessert
        {
            taart = 1,
            softijs = 2,
            coupe = 3,
            rode_coupe = 4,
            hoorntje = 5,
            ijsschaal = 6,
            soesje = 7,
            muffin = 8
        };

        Tegel(dessert top, dessert right, dessert bottom, dessert left);
        dessert get_top();
        dessert get_right();
        dessert get_bottom();
        dessert get_left();
        std::vector<std::string> print_regels();
        void print();

        int get_rotation();
        void set_rotation(const int rot);

    private:
        dessert d_opdruk[4];
        int d_rotation;
};

#endif /* TEGEL_H_ */
