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

VIEWPORT:tuple = (50,50)

def bits_Sutherland(ponto):
    bits = [0,0,0,0]
    if ponto[1] > 50:
        bits[0] = 1
    elif ponto[1] < 0:
        bits[1] = 1
        
    if  ponto[] > 50:
        bits[2] = 1
    elif  ponto[1] < 0:
        bits[3] = 1
        
    return bits

for ponto in pontos:
    print(bits_Sutherland(ponto))


