class Calc:
    def __init__(self, a=0, b=0):
        self.X = a
        self.Y = b
        return

    def soma(self):

        r = self.X + self.Y
        return r

    def sub(self):
        r = self.X - self.Y
        return r

    def multiplicacao(self):
        r = self.X * self.Y
        return r

    def divisao(self):
        r = self.X / self.Y
        return r
