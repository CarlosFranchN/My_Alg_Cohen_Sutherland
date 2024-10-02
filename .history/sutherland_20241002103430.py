class vetor:
    def __init__(self,ponto1,ponto2):
        self.vetor = [ponto1,ponto2]
        self.bits_vetor =  []
        
    def bits_Sutherland(self,ponto):
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
    
    def definir_bits(self):
         