a = [15,10]
b = [30,20]
c = [20,55]
d = [40,60]
e = [30,20]
f = [60,-10]

vetor_1 = [a,b]
vetor_2 = [c,d]
vetor_3 = [e,f]

VIEWPORT:tuple = (50,50)

def bits_Sutherland(vetor):
    bits = [0,0,0,0]
    if vetor[0][1] > 50 or vetor[1][1] > 50:
        bits[0] = 1
    elif vetor[0][1] < 0 or vetor[1][1] < 0:
        bits[1] = 1
        
    if vetor[0][0] > 50 or vetor[1][0] > 50:
        bits[2] = 1
    elif vetor[0][0] < 0 or vetor[1][0] < 0:
        bits[3] = 1
        
    return bits



bits_vetor1 = bits_Sutherland(vetor_1)
bits_vetor2 = bits_Sutherland(vetor_2)
bits_vetor3 = bits_Sutherland(vetor_3)

print(bit)