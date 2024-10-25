# a = [15,10]
# b = [30,20]
# c = [20,55]
# d = [40,60]
# e = [30,20]
# f = [60,-10]
# pontos = [a,b,c,d,e,f]
# vetor_1 = [a,b]
# vetor_2 = [c,d]
# vetor_3 = [e,f]


# def bits_Sutherland(ponto):
#     bits = [0,0,0,0]
#     if ponto[1] > 50:
#         bits[0] = 1
#     elif ponto[1] < 0:
#         bits[1] = 1

#     if  ponto[0] > 50:
#         bits[2] = 1
#     elif  ponto[0] < 0:
#         bits[3] = 1

#     return bits

# def in_viewport(vetor):
#     VIEWPORT:list = [0,0,0,0]
#     saida = list(map(lambda ponto: True if ponto == VIEWPORT else False,vetor))
#     return saida

# def contido(vetor):
#     saida = in_viewport(vetor)
#     if sum(saida) == 2:
#         return "Contidos"
#     elif sum(saida) == 1:
#         return "Parcialmente Contidos"

#     elif sum(saida) == 0:
#         return "Não Contidos"


# # for ponto in pontos:
# #     print(bits_Sutherland(ponto))
# vetor_1_bits = list(map(bits_Sutherland,vetor_1))
# vetor_2_bits = list(map(bits_Sutherland,vetor_2))
# vetor_3_bits = list(map(bits_Sutherland,vetor_3))
# print()
# # print(contido(vetor_1_bits))
# # print(contido(vetor_2_bits))
# # print(contido(vetor_3_bits))

# print(f"O vetor 1 está  {contido(vetor_1_bits)}")
# print(f"O vetor 2 está {contido(vetor_2_bits)}")
# print(f"O vetor 3 está {contido(vetor_3_bits)}")


# a = 10
# print(bin(a))
# Definir códigos de regiões
INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000

# Definir limites da janela de recorte
xmin, ymin, xmax, ymax = 0, 0, 100, 100


# Função para calcular o código de um ponto
def compute_code(x, y):
    code = INSIDE
    if x < xmin:  # à esquerda
        code |= LEFT
    elif x > xmax:  # à direita
        code |= RIGHT
    if y < ymin:  # abaixo
        code |= BOTTOM
    elif y > ymax:  # acima
        code |= TOP
    return code


# Função de recorte Cohen-Sutherland
def cohen_sutherland_clip(x1, y1, x2, y2):
    # Calcular o código dos pontos
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        # Caso trivial: ambos os pontos estão dentro
        if code1 == 0 and code2 == 0:
            accept = True
            break
        # Caso trivial: ambos os pontos estão fora da mesma região
        elif (code1 & code2) != 0:
            break
        # Caso complicado: recortar a linha
        else:
            # Seleciona um dos pontos fora da janela
            code_out = code1 if code1 != 0 else code2

            # Encontrar o ponto de interseção com a borda
            if code_out & TOP:  # acima
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOTTOM:  # abaixo
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & RIGHT:  # à direita
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            elif code_out & LEFT:  # à esquerda
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            # Atualiza o ponto fora da janela e recalcula o código
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        print(f"Linha dentro da janela: ({x1}, {y1}) até ({x2}, {y2})")
    else:
        print("Linha fora da janela")


# Exemplo de uso
x1, y1 = 10, 70
x2, y2 = 120, 80
cohen_sutherland_clip(x1, y1, x2, y2)
