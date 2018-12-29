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

    def to_int(self):
        try:
            self.opdruk_int = tuple(getattr(self, soort) for soort in self.opdruk)
        except AttributeError as ae:
            raise NameError('Invalid dessert specified: ' + str(ae))


if __name__ == '__main__':
    tegel = Tegel(('muffine', 'soesje', 'softijs', 'ijsschaal'))
    print(tegel)
