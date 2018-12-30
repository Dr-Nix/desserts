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
        pass

    def __str__(self):
        s = []
#        activerows = (len(self.tegels) - 1) / self.cols + 1
        for row in range(self.cols):
            s.append(self.horcat(self.tegels[row * self.cols : (row + 1) * self.cols]))
        return '\n'.join(s)

    def horcat(self, tegs):
        splitlist = [t.blockstr().split('\n') for t in tegs]
        transposelist = list(map(list, zip(*splitlist)))
        return '\n'.join(map(''.join, transposelist))


if __name__ == '__main__':
    import tegels
    veld = Speelveld(2, 2)
    for T in tegels.set4():
        veld.add_tegel(T)
    print(veld)
