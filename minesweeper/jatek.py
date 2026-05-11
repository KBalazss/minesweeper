import pygame
from szomszed import Szomszed
from palya import Palya
import time
class  Jatek():
    def __init__(self, palya, Ablak_meret,Palya_meret,aknak,cella):
        self.palya = palya
        self.Ablak_meret = Ablak_meret
        self.Palya_meret = Palya_meret
        self.aknak = aknak
        self.cella = cella
        self.volt = []
        self.ures = [[ 0 for i in range(Palya_meret[1])]for j in range(Palya_meret[0])]
        self.vesztett = False
        self.starttime = time.time()
        self.current_time = time.time() - self.starttime
        self.button_rect = pygame.Rect(
            self.Ablak_meret[0]-250,
            self.Ablak_meret[1] - 70,
            180,
            50
        )

    def fut(self):
        self.ablak = pygame.display.set_mode(self.Ablak_meret)
        pygame.init()
        fut = True
        while fut:
            if self.vesztett or self.nyertel_e():
                self.current_time = self.current_time
            else:
                self.current_time = time.time() - self.starttime
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    if not self.vesztett or not self.nyertel_e():
                        with open("save.txt", "w") as s:
                            for sor in self.palya:
                                s.write(" ".join(map(str, sor)) + "\n")

                        with open("cover.txt", "w") as g:
                            for sor in self.ures:
                                g.write(" ".join(map(str, sor)) + "\n")
                        g.close()
                        s.close()
                    fut = False


                if (event.type == pygame.MOUSEBUTTONDOWN):
                    self.poz = self.eger_poz()
                    if self.button_rect.collidepoint(event.pos):
                        self.palya = Palya(self.Palya_meret,self.aknak).tabla
                        self.volt = []
                        self.ures = [[ 0 for i in range(self.Palya_meret[1])]for j in range(self.Palya_meret[0])]
                    if self.poz[0] < self.Palya_meret[0] and self.poz[1] < self.Palya_meret[1]:
                        if event.button == 1 and self.ures[self.poz[0]][self.poz[1]] == 0:
                            self.ures[self.poz[0]][self.poz[1]] =1
                            
                            self.felfed(self.poz)
                            
                            if self.palya[self.poz[0]][self.poz[1]] == -1:
                                self.vesztett = True
                        if event.button == 3:
                            if self.ures[self.poz[0]][self.poz[1]] ==0:
                                self.ures[self.poz[0]][self.poz[1]] = -1
                            elif self.ures[self.poz[0]][self.poz[1]] ==-1:
                                self.ures[self.poz[0]][self.poz[1]] = 0
                                    
            self.kirajz()
            pygame.display.update()
        pygame.quit()
    
    def kirajz(self):
        ablak = self.ablak
        ablak.fill("black")
        betu= pygame.font.SysFont('Arial',20)
        ido_betu = pygame.font.SysFont('Arial',40)
        vege_betu = pygame.font.SysFont('Arial',70)
        
        
        #ido_kiir
        f = open('best_time.txt','r')
        best = f.readline()
        ido = ido_betu.render(f'Idő: {round(self.current_time)}',1,'white')
        ablak.blit(ido, (0,self.Ablak_meret[1] - ido.get_height()))
        best_ido = ido_betu.render(f'legjobb idő: {best}',1,'white')
        ablak.blit(best_ido, (0,self.Ablak_meret[1] - ido.get_height()*2))

        pygame.draw.rect(ablak, 'blue',self.button_rect)
        text = betu.render("Uj jatek", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.button_rect.center)
        ablak.blit(text, text_rect)
        if self.vesztett == True:
            szo = vege_betu.render('Vesztettél!',1,'white')
            ablak.blit(szo,(self.Ablak_meret[0]/2-szo.get_width()/2,self.Ablak_meret[0]/2))
            return

        if self.nyertel_e() == True:
            if int(best) > round(self.current_time) or int(best) == 0:
                f = open('best_time.txt','w')
                f.write(str(round(self.current_time)))
            szo = vege_betu.render('Nyertél!',1,'white')
            ablak.blit(szo,(self.Ablak_meret[0]/2-szo.get_width()/2,self.Ablak_meret[0]/2))
            f.close()
            return

        #kockak kirajzolasa
        
        meretszel = self.Ablak_meret[0]//self.cella
        for i, sor in enumerate(self.palya):
            hosz = meretszel*i
            for j,ertek in enumerate(sor): 
                szel = meretszel*j
                fedett = self.ures[i][j]

                if fedett == 0:
                    pygame.draw.rect(ablak, 'lightgrey',(szel,hosz,meretszel, meretszel))
                    pygame.draw.rect(ablak, 'black',(szel,hosz,meretszel, meretszel),2)
                    continue
                elif fedett == -1:
                    pygame.draw.rect(ablak, 'green',(szel,hosz,meretszel, meretszel))
                    pygame.draw.rect(ablak, 'black',(szel,hosz,meretszel, meretszel),2)     
                    continue
                else:
                    
                    pygame.draw.rect(ablak, 'darkgrey',(szel,hosz,meretszel, meretszel))
                    pygame.draw.rect(ablak, 'black',(szel,hosz,meretszel, meretszel),2)
                    #kockak ertekenek kiirasa
                    szo = betu.render(str(ertek),1,'black')
                    if ertek > 0:
                        ablak.blit(szo,(szel + (meretszel/2 - szo.get_width()/2) ,hosz + (meretszel/2 - szo.get_width()/2)))
        
    def eger_poz(self):
        poz = pygame.mouse.get_pos()
        cella = int(poz[1]//(self.Ablak_meret[0]//self.cella)),int(poz[0]//(self.Ablak_meret[0]//self.cella))
        return cella
    def felfed(self,p):
        self.volt.append(p)
        if self.palya[p[0]][p[1]] == 0:
            szomszed = Szomszed((p[0],p[1]),self.Palya_meret).szomszed
            for i in szomszed:
                if i in self.volt or self.ures[i[0]][i[1]] == -1:
                    continue
                else:
                    self.volt.append(i)
                    self.felfed(i)
                    self.ures[i[0]][i[1]] = 1
                    #felfedett += 1
                
    def nyertel_e(self):
        felfedett =0
        for i in range(self.Palya_meret[0]):
            for j in range(self.Palya_meret[1]):
                if self.ures[i][j] == 1:
                    felfedett += 1
        if felfedett == self.Palya_meret[0]*self.Palya_meret[1]-self.aknak:
            return True
        return False