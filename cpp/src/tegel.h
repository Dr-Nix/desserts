/*
 * Tegel.h
 *
 *  Created on: Jan 3, 2019
 *      Author: boris
 */

#ifndef TEGEL_H_
#define TEGEL_H_

class Tegel
{
    public:
        Tegel(int top, int right, int bottom, int left);
        virtual ~Tegel();
        int get_top();
        int get_right();
        int get_bottom();
        int get_left();

        int get_rotation();
        void set_rotation(const int rot);

    private:
        int d_opdruk[4];
        int d_rotation;
};

#endif /* TEGEL_H_ */
