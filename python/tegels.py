'''
Created on Dec 29, 2018

@author: boris
'''
import random


class Tegel:
    taart = 1
    softijs = 2
    coupe = 3
    rode_coupe = 4
    hoorntje = 5
    ijsschaal = 6
    soesje = 7
    muffin = 8

    def __init__(self, opdr):
        if type(opdr[0]) == str:
            self.opdruk = opdr
            self.to_int()
        elif type(opdr[0]) == int:
            self.opdruk_int = opdr
        else:
            NameError('verkeerde opdruk!' + str(opdr))

    def __str__(self):
        return 'Tegel' + str(self.opdruk) + ' ' + str(self.opdruk_int)

    def __repr__(self):
        return 'Tegel' + str(self.opdruk)

    def __eq__(self, other):
        return(self.opdruk_int == other.opdruk_int)

    def blockstr(self):
        return ("*---*\n"
                "| {} |\n"
                "|{} {}|\n"
                "| {} |\n"
                "*---*").format(self.opdruk_int[0],
                                self.opdruk_int[3], self.opdruk_int[1],
                                self.opdruk_int[2])

    def to_int(self):
        try:
            self.opdruk_int = tuple(getattr(self, soort) for soort in self.opdruk)
        except AttributeError as ae:
            raise NameError('Invalid dessert specified: ' + str(ae))

    def rotate(self, turns):
        turns = turns % 4
        new_opdruk = self.opdruk_int[turns:] + self.opdruk_int[:turns]
        return Tegel(new_opdruk)


def horcat(tegs):
        splitlist = [t.blockstr().split('\n') for t in tegs]
        transposelist = list(map(list, zip(*splitlist)))
        return '\n'.join(map(''.join, transposelist))


def standaardSet():
    lijst = ('muffin taart softijs ijsschaal',
             'softijs ijsschaal muffin taart',
             'softijs taart ijsschaal ijsschaal',
             'softijs rode_coupe hoorntje taart',
             'softijs ijsschaal muffin soesje',
             'muffin softijs rode_coupe ijsschaal',
             'ijsschaal softijs taart softijs',
             'hoorntje softijs ijsschaal softijs',
             'muffin hoorntje coupe muffin',
             'rode_coupe taart taart hoorntje',
             'taart ijsschaal softijs taart',
             'ijsschaal muffin softijs ijsschaal',
             'muffin soesje softijs ijsschaal',
             'coupe rode_coupe soesje soesje',
             'taart ijsschaal softijs rode_coupe',
             'softijs taart taart ijsschaal')
    return [Tegel(t.split()) for t in lijst]


def set4():
    lijst = ('muffin taart softijs ijsschaal',
             'softijs ijsschaal muffin taart',
             'softijs ijsschaal muffin soesje',
             'muffin softijs rode_coupe ijsschaal')
    return [Tegel(t.split()) for t in lijst]


def tegel_shuffle(tegels, seed=None):
    if seed is not None:
        random.seed(seed)
    random.shuffle(tegels)
    ts = [t.rotate(random.randint(0, 3)) for t in tegels]
    return ts


if __name__ == '__main__':
    tegel = Tegel(('muffin', 'soesje', 'softijs', 'ijsschaal'))
    tegel2 = Tegel(('muffin', 'soesje', 'softijs', 'ijsschaal'))
    print(tegel.rotate(-1))
    print(tegel.rotate(0))
    print(tegel.rotate(1))
    print(tegel.rotate(2))
    print(tegel.rotate(3))
    print(tegel.rotate(4))
    a = set4()
    print(a)
    print(tegel.blockstr())
    print('tegel == tegel2:' + str(tegel == tegel2))
    print('tegel == tegel2rot:' + str(tegel == tegel2.rotate(1)))
    b = standaardSet()
    for t in b:
        print(t)
    print('len b: ' + str(len(b)))
