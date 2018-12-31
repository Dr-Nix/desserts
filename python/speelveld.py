'''
Created on Dec 30, 2018

@author: boris
'''
import tegels


class Speelveld:

    def __init__(self, rows, cols):
        if rows < 1:
            raise NameError('rows should be >= 1')
        if cols < 1:
            raise NameError('cols should be >= 1')
        self.rows = rows
        self.cols = cols
        self.tegels = []
        # self.set_connections()

    def add_tegel(self, T):
        if len(self.tegels) == self.rows * self.cols:
            return NameError('veld vol!')
        self.tegels.append(T)

    def del_tegel(self):
        self.tegels.pop()

    def roteer(self):
        if len(self.tegels) != self.rows * self.cols:
            NameError('kan alleen roteren met vol veld')
            return

        # make list of lists:
        tegel_ll = [[n for n in self.tegels[self.cols * m:self.cols * (m + 1)]] for m in range(self.rows)]

        # roteer
        tegel_rot = [list(l) for l in list(zip(*tegel_ll))[::-1]]

        # platslaan
        self.tegels = [item for sublist in tegel_rot for item in sublist]

        # roteer elke tegel zelf
        self.tegels = [tegel.rotate(1) for tegel in self.tegels]
        self.rows, self.cols = self.cols, self.rows
        return(self)

    def roteerN(self, N):
        for i in range(N % 4):
            self.roteer()

    def is_rotatie_van(self, andere):
        return(any([self == andere.roteer() for i in range(4)]))

    def check_laatste(self):
        curtegel = len(self.tegels) - 1
        row = curtegel // self.cols
        col = curtegel % self.cols
        valid = True
        if row > 0:
            valid = self.tegels[curtegel].opdruk_int[0] == self.tegels[curtegel - self.cols].opdruk_int[2]
            # print('checking tegel {}, rows: {}=={}'.format(curtegel,
            #                                               self.tegels[curtegel].opdruk_int[0],
            #                                               self.tegels[curtegel - self.cols].opdruk_int[2]))
        if col > 0:
            valid &= self.tegels[curtegel].opdruk_int[3] == self.tegels[curtegel - 1].opdruk_int[1]
            # print('checking tegel {}, cols: {}=={}'.format(curtegel,
            #                                               self.tegels[curtegel].opdruk_int[3],
            #                                               self.tegels[curtegel - 1].opdruk_int[1]))
        # print('check valid = ' + str(valid))
        return valid

    def __str__(self):
        s = []
#        activerows = (len(self.tegels) - 1) / self.cols + 1
        for row in range(self.cols):
            s.append(tegels.horcat(self.tegels[row * self.cols : (row + 1) * self.cols]))
        return '\n'.join(s)

    def __eq__(self, other):
        if self.rows != other.rows:
            return False
        if self.cols != other.cols:
            return False
        return(self.tegels == other.tegels)


if __name__ == '__main__':
    veld = Speelveld(2, 2)
    veld2 = Speelveld(2, 2)
    veld3 = Speelveld(2, 2)
    veld4 = Speelveld(2, 2)
    setje = tegels.set4()
    setje = tegels.tegel_shuffle(setje, seed=1)
    for T in setje:
        veld.add_tegel(T)
        # print(veld)
        # veld.check_laatste()
        veld2.add_tegel(T.rotate(0))
    veld3.add_tegel(setje[1].rotate(1))
    veld3.add_tegel(setje[3].rotate(1))
    veld3.add_tegel(setje[0].rotate(1))
    veld3.add_tegel(setje[2].rotate(1))
    veld4.add_tegel(setje[0])
    veld4.add_tegel(setje[0])
    veld4.add_tegel(setje[1])
    veld4.add_tegel(setje[2])
    print(veld)
    print('------')
    print(veld2)
    print('veld == veld2:' + str(veld == veld2))
    print('------')
    print(veld3)
    print('veld == veld3:' + str(veld == veld3))
    veld.roteer()
    print('veld geroteerd:\n' + str(veld))
    veld.roteerN(3)
    print('veld == veld3:' + str(veld == veld3))
    print('veld is rotatie veld2:' + str(veld.is_rotatie_van(veld2)))
    print('veld is rotatie veld4:' + str(veld.is_rotatie_van(veld4)))
    print('veld:\n' + str(veld))
    print('veld2:\n' + str(veld2))
    print('veld4:\n' + str(veld4))

