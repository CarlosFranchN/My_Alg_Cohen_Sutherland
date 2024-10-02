class vetor:
    def __init__(self,ponto1,ponto2):
        self.vetor = [ponto1,ponto2]
        self.bits = [0,0,0,0]
        
    def bits_Sutherland(self,ponto):
        if ponto[1] > 50:
            self.bits[0] = 1
        elif ponto[1] < 0:
            self.bits[1] = 1
            
        if  ponto[0] > 50:
            self.bits[2] = 1
        elif  ponto[0] < 0:
            self.bits[3] = 1
            
        