import random
from szomszed import Szomszed
class Palya():
    def __init__(self,meret,akna):
        self.meret = meret
        self.akna = akna
        self.tabla =  self.general()
    def general(self):
        lerakott = set()
        self.palya = []
        for i in range(self.meret[0]):
            self.palya.append([])
            for j in range(self.meret[1]):
                self.palya[i].append(0)
        while len(lerakott) < self.akna:
            sor = random.randrange(0,self.meret[0])
            oszlop = random.randrange(0,self.meret[1])
            pont = sor, oszlop
            if pont in lerakott:
                continue
            lerakott.add(pont)
            self.palya[sor][oszlop] = -1

        for i in lerakott:
            szomszed = Szomszed((i[0],i[1]),self.meret).szomszed
            for j,k in szomszed:
                if self.palya[j][k] >=0:
                    self.palya[j][k] += 1
        return self.palya
