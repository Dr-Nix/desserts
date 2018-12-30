'''
Created on Dec 29, 2018

@author: boris
'''


class Tegel:
    taart = 1
    softijs = 2
    coupe = 3
    rode_coupe = 4
    hoorntje = 5
    ijsschaal = 6
    soesje = 7
    muffin = 8

    def __init__(self, opdruk):
        self.opdruk = opdruk
        self.to_int()

    def __str__(self):
        return 'Tegel' + str(self.opdruk) + ' ' + str(self.opdruk_int)

    def __repr__(self):
        return 'Tegel' + str(self.opdruk)

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
        new_opdruk = self.opdruk[turns:] + self.opdruk[:turns]
        return Tegel(new_opdruk)


def standaardSet():
    lijst = ('muffin soesje softijs ijsschaal',
             'muffin taart softijs ijsschaal',
             'softijs ijsschaal muffin taart')
    return [Tegel(t.split()) for t in lijst]


def set4():
    lijst = ('muffin taart softijs ijsschaal',
             'softijs ijsschaal muffin taart',
             'softijs ijsschaal muffin soesje',
             'muffin softijs rode_coupe ijsschaal')
    return [Tegel(t.split()) for t in lijst]


if __name__ == '__main__':
    tegel = Tegel(('muffin', 'soesje', 'softijs', 'ijsschaal'))
    print(tegel.rotate(-1))
    print(tegel.rotate(0))
    print(tegel.rotate(1))
    print(tegel.rotate(2))
    print(tegel.rotate(3))
    print(tegel.rotate(4))
    a = set4()
    print(a)
    print(tegel.blockstr())
