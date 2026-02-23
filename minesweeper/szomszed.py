class Szomszed():
    def __init__(self,pont,meret):
        self.pont = pont
        self.meret = meret
        self.szomszed = self.szomszedok()
    def szomszedok(self):
        self.szomszed = []
        if self.pont[0] > 0 and self.pont[1] > 0:#bal-fent
            self.szomszed.append([self.pont[0]-1 , self.pont[1]-1])
        if self.pont[0] > 0: # fent
            self.szomszed.append([self.pont[0]-1,self.pont[1]]) 
        if self.pont[0] > 0 and self.pont[1] < self.meret[1]-1:#jobb-fent
            self.szomszed.append([self.pont[0]-1,self.pont[1]+1])
        if self.pont[1] < self.meret[1]-1:#bal
            self.szomszed.append([self.pont[0],self.pont[1]+1])
        if self.pont[1] > 0: #jobb
            self.szomszed.append([self.pont[0],self.pont[1]-1])
        if self.pont[0] < self.meret[0]-1 and self.pont[1] > 0: #bal-lent
            self.szomszed.append([self.pont[0]+1,self.pont[1]-1])
        if self.pont[0] < self.meret[0]-1: #lent
            self.szomszed.append([self.pont[0]+1,self.pont[1]])
        if self.pont[1] < self.meret[1]-1 and self.pont[0] < self.meret[0]-1:  #jobb-lent
            self.szomszed.append([self.pont[0]+1,self.pont[1]+1])
        return self.szomszed
