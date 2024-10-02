class vetor:
    def __init__(self, ponto1, ponto2):
        self.vetor = [ponto1, ponto2]
        self.bits_vetor = []

    def bits_Sutherland(self, ponto):
        bits = [0, 0, 0, 0]
        if ponto[1] > 50:
            bits[0] = 1
        elif ponto[1] < 0:
            bits[1] = 1

        if ponto[0] > 50:
            bits[2] = 1
        elif ponto[0] < 0:
            bits[3] = 1

        return bits

    def definir_bits(self):
        for ponto in self.vetor:
            self.bits_vetor.append(self.bits_Sutherland(ponto))

    def in_viewport(self):
        VIEWPORT: list = [0, 0, 0, 0]
        saida = list(map(lambda ponto: True if ponto == VIEWPORT else False, self.vetor))
        return saida

    def contido(self):
        saida = self.in_viewport()
        if sum(saida) == 2:
            return "Contidos"
        elif sum(saida) == 1:
            return "Parcialmente Contidos"

        elif sum(saida) == 0:
            return "Não Contidos"

vetor = Vetor()
a = [15,10]
b = [30,20]
c = [20,55]
d = [40,60]
e = [30,20]
f = [60,-10]
pontos = [a,b,c,d,e,f]
vetor_1 = vetor(a,b)
vetor_2 = [c,d]
vetor_3 = [e,f]

