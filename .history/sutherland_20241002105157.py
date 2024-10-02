class Vetor:
    def __init__(self, ponto1, ponto2):
        self.vetor = [ponto1, ponto2]
        self.bits_vetor = []
        self.definir_bits()

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
        saida = list(map(lambda ponto: True if ponto == VIEWPORT else False, self.bits_vetor))
        return saida

    def contido(self):
        saida = self.in_viewport()
        if sum(saida) == 2:
            return f"O vetor {self.vetor} está Contido"
        elif sum(saida) == 1:
            return f"O vetor {self.vetor} está Parcialmente Contido"

        elif sum(saida) == 0:
            return f" O vetor {self.vetor} está Não Contido"
        



# a = [15,10]
# b = [30,20]
# c = [20,55]
# d = [40,60]
# e = [30,20]
# f = [60,-10]
# pontos = [a,b,c,d,e,f]
# vetor_1 = Vetor(a,b)
# vetor_2 = Vetor(c,d)
# vetor_3 = Vetor(e,f)

# print(vetor_1)
# print(vetor_1.bits_vetor)
# print(vetor_1.vetor)
# print(vetor_1.in_viewport())
# print(vetor_1.contido())
a = []
b = []
print("Sabendo que a VIEWPORT tem o tamanho (50,50):")
print("Digite as coordenadas dos pontos do vetor: ")
a[0] = int(input("Digite a coordenada X do primeiro ponto: "))
a[1] = int(input("Digite a coordenada Y do primeiro ponto: "))
b[0] = int(input("Digite a coordenada X do segundo ponto: "))
b[1] = int(input("Digite a coordenada Y do segundo ponto: "))

vetor = Vetor(a,b)
print(vetor.vetor)
print(vetor.bits_vetor)
print(vetor.in_viewport())
print(vetor.contido())