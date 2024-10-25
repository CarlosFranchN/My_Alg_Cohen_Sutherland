class Vetor:
    def __init__(self, ponto1, ponto2):
        self.vetor = [ponto1, ponto2]
        self.vetor_viewport = [ponto1, ponto2]
        self.bits_vetor = []
        self.bit_value = []
        self.definir_bits()
        self.definir_bit_value()
        self.xMin,self.xMax,self.yMin,self.yMax = 0 , 50 , 0 , 50
        self.INSIDE = 0  # 0000
        self.LEFT = 1    # 0001
        self.RIGHT = 2   # 0010
        self.BOTTOM = 4  # 0100
        self.TOP = 8     # 1000
    def definir_bit_value(self):

        for array in self.bits_vetor:
            string = "".join(map(str,array))
            self.bit_value.append(int(string,2))

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
    def compute_code(self,ponto):

        code = self.INSIDE
        x = ponto[0]
        y = ponto[1]
        if x < self.xMin:
            code |= self.LEFT
        elif x>self.xMax:
            code |= self.RIGHT

        if y < self.yMin:
            code |= self.BOTTOM
        elif y > self.yMax:
            code |= self.TOP

        return code

    def clip(self):
        x1,y1 = self.vetor[0][0],self.vetor[0][1]
        x2,y2 = self.vetor[1][0],self.vetor[1][1]
        code1 = self.compute_code(self.vetor[0])
        code2 = self.compute_code(self.vetor[1])
        flag = False

        while True:
            if code1 == 0 and code2 == 0:
                flag = True
                break
            elif (code1 & code2) != 0:
                break
            else:
                code_out = code1 if code1 != 0 else code2

                if code_out & self.TOP:
                    x = x1 + (x2 - x1) * (self.yMax - y1) / (y2 - y1)
                    y = self.yMax
                elif code_out & self.BOTTOM:
                    x = x1 + (x2 - x1) * (self.yMin - y1) / (y2 - y1)
                    y = self.yMin
                elif code_out & self.RIGHT:  # à direita
                    y = y1 + (y2 - y1) * (self.xMax - x1) / (x2 - x1)
                    x = self.xMax
                elif code_out & self.LEFT:  # à esquerda
                    y = y1 + (y2 - y1) * (self.xMin - x1) / (x2 - x1)
                    x = self.xMin

                if code_out == code1:
                    self.vetor_viewport[0] = [x,y]
                    code1 = self.compute_code([x,y])
                else:
                    self.vetor_viewport[1] = [x,y]
                    code2 = self.compute_code([x,y])

            if flag:
                print(f"Linha dentro da janela: ({x1}, {y1}) até ({x2}, {y2})")
            else:
                print("Linha fora da janela")
                    


        
    def in_viewport(self):
        VIEWPORT: list = [0, 0, 0, 0]
        saida = list(
            map(lambda ponto: True if ponto == VIEWPORT else False, self.bits_vetor)
        )
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
# vetor_1 = Vetor(a,b)
# vetor_2 = Vetor(c,d)
# vetor_3 = Vetor(e,f)

# vetores = [vetor_1,vetor_2,vetor_3]
# # Exemplo =>
# for vetor in vetores:
#     print(vetor.vetor)
#     print(vetor.bits_vetor)
#     print(vetor.bit_value)
#     vetor.clip()
#     print(vetor.vetor_viewport)
#     print(vetor.contido())
#     print()
