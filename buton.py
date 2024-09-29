import pygame
import calcule

def click(button, v):
    match button.id:
        case 0:
            v[0].operatie="Inserare Inceput"
            v[0].campuri[0].op=v[0].operatie
            v[0].campuri[2].op=v[0].operatie
            v[0].campuri[3].op=v[0].operatie
            v[0].campuri[4].op=v[0].operatie
        case 1:
            v[0].operatie="Inserare Mijloc"
            v[0].campuri[0].op=v[0].operatie
            v[0].campuri[1].op=v[0].operatie
            v[0].campuri[1].text="Inserare Sfarsit"
            v[0].campuri[2].op=v[0].operatie
            v[0].campuri[3].op=v[0].operatie
            v[0].campuri[4].op=v[0].operatie
        case 2:
            v[0].operatie="Inserare Sfarsit"
            v[0].campuri[0].op=v[0].operatie
            v[0].campuri[2].op=v[0].operatie
            v[0].campuri[3].op=v[0].operatie
            v[0].campuri[4].op=v[0].operatie
        case 3:
            if(len(v[0].lista)>0):
                calcule.stergereloc(v, 0)
        case 4:
            v[0].operatie="Stergere Mijloc"
        case 5:
            if(len(v[0].lista)>0):
                calcule.stergereloc(v, len(v[0].lista)-1)
                v[0].lista[len(v[0].lista)-1].succesor=False
        case 6:
            v[0].show=v[0].butoane[5].colour
            v[0].campuri[2].info=v[0].butoane[6].colour[0]
            v[0].campuri[3].info=v[0].butoane[6].colour[1]
            v[0].campuri[4].info=v[0].butoane[6].colour[2]
            v[0].sel=1
        case 7:
            v[0].show=v[0].butoane[6].colour
            v[0].campuri[2].info=v[0].butoane[7].colour[0]
            v[0].campuri[3].info=v[0].butoane[7].colour[1]
            v[0].campuri[4].info=v[0].butoane[7].colour[2]
            v[0].sel=2
        case 8:
            v[0].lista=[]
            v[0].liscount=0
        case 9:
            if v[0].tip=='LSI':
                v[0].tip='LDI'
                v[0].butoane[10].text='LDI'
                for i in range(len(v[0].lista)):
                    v[0].lista[i].liniepreddest=v[0].lista[v[0].lista[i].predecesor].liniepred
            else:
                v[0].tip='LSI'
                v[0].butoane[10].text='LSI'
            

class button():
    hover = True
    visible = True
    effectlock = False
    limit = False
    border = 3
    bordercolour = (0,0,0)
    def __init__(self, surface, colour, x, y, width, height, id, text):
        self.surface = surface
        self.colour = colour
        self.hovercolour = (colour[0]+30, colour[1]+30, colour[2]+30)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.id = id
        self.text = text
    def detect(self, mousepos):
        if self.x <= mousepos[0]  <= self.x + self.width and self.y <= mousepos[1] <= self.y + self.height and self.hover==True:
            return True
        else:
            return False
    def draw(self, mousepos):
        check = self.detect(mousepos)
        if self.visible and 0 <= self.border < self.width and self.border < self.height:
            pygame.draw.rect(self.surface, self.bordercolour, [self.x, self.y, self.width, self.height])
        if not check and self.visible and self.border >= 0:
            pygame.draw.rect(self.surface, self.colour, [self.x + self.border//2, self.y + self.border//2, self.width - self.border, self.height - self.border])
        elif check and self.visible and self.border >= 0:
            pygame.draw.rect(self.surface, self.hovercolour, [self.x + self.border//2, self.y + self.border//2, self.width - self.border, self.height - self.border])
    def drawtxt(self, v, surface):
        txt = v[0].fontbutoane.render(self.text, False, v[0].alb)
        surface.blit(txt, (self.x,self.y+10))
    def click(self, v, mousepos, mousepressed):
        check = self.detect(mousepos)
        if check and not self.effectlock and mousepressed[0] and not self.limit:
            self.limit = True
            
        elif check and not mousepressed[0] and self.limit:
            click(self, v)
            self.limit = False


def create(surface, colour, x, y, width, height, id, text):
    return button(surface, colour, x, y, width, height, id, text)