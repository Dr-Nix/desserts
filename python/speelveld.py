'''
Created on Dec 30, 2018

@author: boris
'''


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

    def set_connections(self):
        pass

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


if __name__ == '__main__':
    import tegels
    veld = Speelveld(2, 2)
    for T in tegels.set4(shuffle=True, seed=1):
        veld.add_tegel(T)
        # print(veld)
        veld.check_laatste()
    print(veld)
