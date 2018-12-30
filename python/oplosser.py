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
            for i in range(4):
                self.veld.add_tegel(tegel.rotate(i))
                if self.veld.check_laatste():
                    if len(self.tegelzak) == 1:
                        print('valid:')
                        print(self.veld)
                    nieuwe_zak = copy.copy(self.tegelzak)
                    nieuwe_zak.remove(tegel)
                    suboplosser = Oplosser(self.veld, nieuwe_zak)
                    suboplosser.los_op()
                else:
                    pass
                    # print('invalid:')
                    # print(self.veld)
                self.veld.del_tegel()


if __name__ == '__main__':
    tegelzak = tegels.set4(shuffle=True, seed=1)
    veld = speelveld.Speelveld(2, 2)
    op = Oplosser(veld, tegelzak)
    op.los_op()
