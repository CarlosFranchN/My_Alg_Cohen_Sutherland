a = [15,10]
b = [30,20]
c = [20,55]
d = [40,60]
e = [30,20]
f = [60,-10]
pontos = [a,b,c,d,e,f]
vetor_1 = [a,b]
vetor_2 = [c,d]
vetor_3 = [e,f]


def bits_Sutherland(ponto):
    bits = [0,0,0,0]
    if ponto[1] > 50:
        bits[0] = 1
    elif ponto[1] < 0:
        bits[1] = 1
        
    if  ponto[0] > 50:
        bits[2] = 1
    elif  ponto[0] < 0:
        bits[3] = 1
        
    return bits

def in_viewport(vetor):
    VIEWPORT:list = [0,0,0,0]
    saida = list(map(lambda ponto: True if ponto == VIEWPORT else False,vetor))
    return saida

def contido(vetor):
    in_viewport(vetor)
    if sum(saida) == 2:
        return "Contidos"
    elif sum(saida) == 1:
        return "Parcialmente Contidos"
        
    elif sum(saida) == 0:
        return "Não Contidos"
    

# for ponto in pontos:
#     print(bits_Sutherland(ponto))
vetor_1_bits = list(map(bits_Sutherland,vetor_1))
vetor_2_bits = list(map(bits_Sutherland,vetor_2))
vetor_3_bits = list(map(bits_Sutherland,vetor_3))
print()
print(in_viewport(vetor_1_bits))
print(in_viewport(vetor_2_bits))
print(in_viewport(vetor_3_bits))

