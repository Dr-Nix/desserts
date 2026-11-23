/*
 * tegelzak.h
 *
 *  Created on: Jan 12, 2019
 *      Author: boris
 */

#ifndef TEGELZAK_H_
#define TEGELZAK_H_

#include <vector>
#include <memory>

#include "tegel.h"

class Tegelzak
{
    public:
        enum class set
        {
            LEEG,
            VIER,
            ALLEMAAL
        };
        Tegelzak(set s);
        void schud();
        std::unique_ptr<Tegel> pak_tegel();

    private:
        std::vector<std::unique_ptr<Tegel>> tegels;

};


#endif /* TEGELZAK_H_ */
