import pygame
import calcule
import afisare
import buton

pygame.init()
    
class camp():
    def __init__(self, ID, op, x, y, width, height, nume):
        self.ID = ID
        self.op = op
        self.pozitie=(x, y)
        self.size=(width, height)
        self.nume = nume
    border=2
    info=0
    def draw(self, v, surface):
        pygame.draw.rect(surface, v[0].negru, (self.pozitie[0], self.pozitie[1], self.size[0], self.size[1]))
        pygame.draw.rect(surface, v[0].alb, (self.pozitie[0]+self.border, self.pozitie[1]+self.border, self.size[0]-2*self.border, self.size[1]-2*self.border))
    def drawtxt(self, v, surface):
        text = v[0].font.render(str(self.info), False, v[0].negru)
        surface.blit(text, (self.pozitie[0]+5, self.pozitie[1]+6))
    def drawnume(self, v, surface):
        text = v[0].font.render(str(self.nume), False, v[0].negru)
        surface.blit(text, (self.pozitie[0],self.pozitie[1]-20))

screen = pygame.display.set_mode((1100, 700))
class variables():
    WIDTH = 1100
    HEIGHT = 700
    albastru=(100,100,255)
    alb=(255, 255, 255)
    negru=(0, 0, 0)
    gri=(122, 122, 122)
    rosu=(255, 0, 0)
    show=(0, 0, 0)
    culoaretemp=(245, 245, 245)
    adaugare=True
    liscount=0
    sel=1
    stergere=False
    proces=False
    tip='LSI'
    surfacestanga =pygame.Surface((WIDTH/2, HEIGHT/1.5))
    surfacedreapta =pygame.Surface((WIDTH/2, HEIGHT/1.5))
    operatie="Inserare Inceput"
    campuri=[camp(1, operatie, 100, 100, 100, 30, "Informatie:"), camp(2, "Inserare Mijloc", 100, 200, 100, 30, "Dupa:"), camp(3, operatie, 350, 100, 100, 30, "RGB"),camp(4, operatie, 350, 150, 100, 30, ""), camp(5, operatie, 350, 200, 100, 30, "")]
    butoane=[buton.create(screen, gri, 50, HEIGHT-110, 120, 40, 0, "Inserare Inceput"), buton.create(screen, gri, 220, HEIGHT-110, 120, 40, 1, "Inserare Mijloc"),buton.create(screen, gri, 390, HEIGHT-110, 120, 40, 2, "Inserare Sfarsit"), buton.create(screen, gri, 560, HEIGHT-110, 120, 40, 3, "Stergere Inceput"), buton.create(screen, gri, 730, HEIGHT-110, 120, 40, 4, "Stergere Mijloc"), buton.create(screen, gri, 900, HEIGHT-110, 120, 40, 5, "Stergere Sfarsit"), buton.create(surfacedreapta, gri, 350, 300, 50, 50, 6, ""), buton.create(surfacedreapta, gri, 400, 300, 25, 50, 7, ""), buton.create(screen, gri, 50, HEIGHT-50, 120, 40, 8, "Distrugere"), buton.create(surfacedreapta, gri, 400, 300, 25, 50, 7, ""), buton.create(screen, gri, 220, HEIGHT-50, 120, 40, 9, "LSI")]
    selected=-1
    prim=-1
    clock = pygame.time.Clock()
    font = pygame.font.Font("freesansbold.ttf", 20)
    fontbutoane = pygame.font.Font("freesansbold.ttf", 15)
    fonttitlu=pygame.font.Font("freesansbold.ttf", 30)
    lista=[]
v=[variables()]

def main():
    while True:
        v[0].clock.tick(60)
        calcule.main(v)
        afisare.main(screen, v)

        

if __name__ == '__main__':
    main()