'''
Created on Dec 30, 2018

@author: boris
'''
import tegels
import speelveld
import copy


class Oplosser:

    def __init__(self, veld, tegelzak):
        self.veld = veld
        self.tegelzak = tegelzak

    def los_op(self):
        for tegel in self.tegelzak:
            if len(self.tegelzak) == 16:
                print('*')
            # if len(self.tegelzak) == 15:
            #    print('-*')
            for i in range(4):
                self.veld.add_tegel(tegel.rotate(i))
                if self.veld.check_laatste():
                    if len(self.tegelzak) == 1:
                        # print('valid:')
                        # print(self.veld)
                        yield(self.veld)
                    nieuwe_zak = copy.copy(self.tegelzak)
                    nieuwe_zak.remove(tegel)
                    suboplosser = Oplosser(self.veld, nieuwe_zak)
                    yield from suboplosser.los_op()
                else:
                    pass
                    # print('invalid:')
                    # print(self.veld)
                self.veld.del_tegel()

    def run(self):
        oplossingen = []
        for v in self.los_op():
            # print('heb er een:')
            # print(v)
            if any([v.is_rotatie_van(eerdere) for eerdere in oplossingen]):
                pass
                # print('helaas een rotatie.')
            else:
                print('nieuwe originele oplossing:')
                print(v)
                oplossingen.append(copy.deepcopy(v))
        return oplossingen


if __name__ == '__main__':
    tegelzak = tegels.set4()
    veld = speelveld.Speelveld(2, 2)
    op = Oplosser(veld, tegelzak)
    oplossingen = op.run()

    print('en nu allemaal:')
    for v in oplossingen:
        print(v)

    zak2 = tegels.standaardSet()
    veld2 = speelveld.Speelveld(4, 4)
    op2 = Oplosser(veld2, zak2)
    oplossingen2 = op2.run()

    print('en nu allemaal:')
    for v in oplossingen2:
        print(v)
