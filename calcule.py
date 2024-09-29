import pygame
import math
def insidest(v, n):
    if (n[0]>0) and (n[0]<v[0].WIDTH/2)and (n[1]>100) and (n[1]<v[0].HEIGHT/1.5+100):
        return True
    else: 
        return False
def insidedr(v, n):
    if (n[0]>v[0].WIDTH/2) and (n[0]<v[0].WIDTH)and (n[1]>100) and (n[1]<v[0].WIDTH/1.5+100):
        return True
    else: 
        return False
def insidemouse(mouse,n):
    if (mouse[0]>=n[0]) and (mouse[0]<=n[0]+n[2]) and (mouse[1]>=n[1]) and (mouse[1]<=n[1]+n[3]):
        return True
    else: 
        return False
class lis():
    def __init__(self, id, x, y, size, info):
        self.id = id
        self.x = x
        self.y = y
        self.origin = (x, y)
        self.size = size
        self.info = info
        self.valoare=(x-(size/2),y-(size/2), self.size, self.size)
        self.linieorigine=(self.x+self.size, self.y-8)
        self.liniedest=[self.x+self.size, self.y-8]
        self.dest=(self.x-self.size//2, self.y-8)
        self.liniepred=[self.x+self.size, self.y+8]
        self.liniepreddest=[self.x-self.size//2, self.y+8]
        self.liniepredorigine=[self.x-self.size//2, self.y+8]
    succesor=False
    predecesor=False
    culoare=(180, 180, 180)
    proces=False
    
    succuloare=(0,0,0)
    border=(0,0,0)
    def draw(self, v, surface):
        pygame.draw.rect(surface, self.border, self.valoare)
        pygame.draw.rect(surface, self.culoare, (self.valoare[0]+1, self.valoare[1]+1, self.valoare[2]-2, self.valoare[3]-2))
        pygame.draw.rect(surface, self.border, (self.x+self.size/2, self.y-self.size/2, self.size/2, self.size))
        pygame.draw.rect(surface, self.succuloare, (self.x+self.size/2+1, self.y-self.size/2+1, self.size/2-2, self.size-2))
    def drawtxt(self, v, surface):
        text = v[0].font.render(str(self.info), False, v[0].alb)
        surface.blit(text, (self.x-(self.size/2)+3,self.y-(self.size/2)+15))
    def point(self, v, surface):
        #print("[", self.id, ",", len(v[0].lista)-2, "]")
        if(self.id<=(len(v[0].lista)-2)):
            pygame.draw.line(surface, self.succuloare, self.linieorigine, self.liniedest, 3)
        if(self.id>0 and v[0].tip=='LDI'):
            pygame.draw.line(surface, self.succuloare, self.liniepredorigine, self.liniepreddest, 3)
    def detect(self, v, mousepos):
        if self.valoare[0] <= mousepos[0]  <= self.valoare[0] + self.valoare[2]<=v[0].WIDTH/1.5 and self.valoare[1]+100 <= mousepos[1] <= self.valoare[1] + self.valoare[3]+100<=v[0].HEIGHT/2+100:
            return True
        else:
            return False
    def click(self, v, mouse, mousepos):
        check=self.detect(v, mousepos)
        if check and mouse[0]:
            return True
        elif check and not mouse[0]:
            return False



def creareloc(v, nr):
    i=len(v[0].lista)
    v[0].lista.append(0)
    while(i>nr):
        v[0].lista[i-1].id=v[0].lista[i-1].id+1
        v[0].lista[i-1].succesor+=1
        v[0].lista[i-1].predecesor+=1
        v[0].lista[i]=v[0].lista[i-1]
        i=i-1
def stergereloc(v, nr):
    i=nr
    while(i<len(v[0].lista)-1):
        v[0].lista[i+1].id=v[0].lista[i+1].id-1
        v[0].lista[i]=v[0].lista[i+1]
        v[0].lista[i].succesor-=1
        v[0].lista[i].predecesor-=1
        i=i+1
    v[0].lista.pop()
    v[0].liscount=v[0].liscount-1
    
def crearelis(v, mouse, nr):
    v[0].lista[nr]=lis(nr, mouse[0],mouse[1]-100, 50, v[0].campuri[0].info)
    v[0].lista[nr].culoare=v[0].butoane[6].colour
    v[0].lista[nr].succuloare=v[0].butoane[7].colour
    v[0].adaugare=False
    v[0].liscount=v[0].liscount+1
def inserareinc(v, mouse, mouse_presses):
    if(mouse_presses[0] and v[0].adaugare and insidest(v, mouse)):
        creareloc(v, 0)
        crearelis(v, mouse, 0)
        if len(v[0].lista)>1:
            v[0].lista[0].succesor=1
            v[0].lista[1].predecesor=0
            if v[0].tip=="LDI":
                v[0].lista[1].proces=True
        v[0].proces=True
        v[0].lista[0].proces=True

        
    if((not mouse_presses[0]) and (not v[0].adaugare)):
        v[0].adaugare=True
def inseraresf(v, mouse, mouse_presses):
    if(mouse_presses[0] and v[0].adaugare and insidest(v, mouse)):
        creareloc(v, len(v[0].lista))
        crearelis(v, mouse, len(v[0].lista)-1)
        v[0].proces=True
        v[0].lista[len(v[0].lista)-2].succesor=len(v[0].lista)-1
        v[0].lista[len(v[0].lista)-1].predecesor=len(v[0].lista)-2
        v[0].lista[len(v[0].lista)-2].proces=True
        if v[0].tip=="LDI":
            v[0].lista[len(v[0].lista)-1].proces=True
    if((not mouse_presses[0]) and (not v[0].adaugare)):
        v[0].adaugare=True
def inseraremij(v, mouse, mouse_presses):
    if(mouse_presses[0] and v[0].adaugare and insidest(v, mouse)):
        for i in range(len(v[0].lista)):
            if v[0].lista[i].info==v[0].campuri[1].info:
                creareloc(v, i+1)
                crearelis(v, mouse, i+1)
                v[0].lista[i].succesor=i+1
                v[0].lista[i+1].succesor=i+2
                v[0].lista[i+1].predecesor=i
                v[0].proces=True
                v[0].lista[i].proces=True
                v[0].lista[i+1].proces=True
                if v[0].tip=="LDI":
                    v[0].lista[i+2].proces=True
                if v[0].lista[i+1].id<len(v[0].lista)-1:
                    v[0].lista[i+1].succesor=v[0].lista[i+1].id+1
                break
        
    if((not mouse_presses[0]) and (not v[0].adaugare)):
        v[0].adaugare=True
def stergeremij(v, mouse, mouse_presses):
    for i in range(len(v[0].lista)-1):
        if v[0].lista[i].click(v, mouse_presses,mouse) and v[0].adaugare:        
            stergereloc(v, i)
            v[0].lista[i-1].proces=True
            if v[0].tip=="LDI":
                v[0].lista[i].proces=True
            if not(i==len(v[0].lista)-1):
                v[0].lista[i+1].proces=True
            else:
                v[0].lista[i].succesor=False
            v[0].proces=True
            v[0].adaugare=False
    if len(v[0].lista)>0:
        if v[0].lista[len(v[0].lista)-1].click(v, mouse_presses,mouse) and v[0].adaugare:
                stergereloc(v, len(v[0].lista)-1)
                v[0].adaugare=False
    if((not mouse_presses[0]) and (not v[0].adaugare)):
        v[0].adaugare=True
def calcst(v, mouse, mouse_presses):
    
    if v[0].proces:
        tmp=0
        i=len(v[0].lista)-1
        while i>=0:
            if v[0].lista[i].succesor and v[0].lista[i].proces:
                
                if (math.floor(v[0].lista[i].liniedest[0])!= math.floor(v[0].lista[v[0].lista[i].succesor].dest[0])) or (math.floor(v[0].lista[i].liniedest[1])!= math.floor(v[0].lista[v[0].lista[i].succesor].dest[1])):
                    if v[0].lista[v[0].lista[i].succesor].dest[0]>v[0].lista[i].liniedest[0]:
                        v[0].lista[i].liniedest[0]+=1
                    elif v[0].lista[v[0].lista[i].succesor].dest[0]<v[0].lista[i].liniedest[0]:
                        v[0].lista[i].liniedest[0]-=1
                    if v[0].lista[v[0].lista[i].succesor].dest[1]>v[0].lista[i].liniedest[1]:
                        v[0].lista[i].liniedest[1]+=1
                    elif v[0].lista[v[0].lista[i].succesor].dest[1]<v[0].lista[i].liniedest[1]:
                        v[0].lista[i].liniedest[1]-=1
                    tmp=1
                    break
            i-=1
        i=len(v[0].lista)-1
        if tmp==0 and v[0].tip=="LDI":
            while i>=0:
                if (v[0].lista[i].predecesor+1) and v[0].lista[i].proces:
                    
                    if (math.floor(v[0].lista[i].liniepreddest[0])!= math.floor(v[0].lista[v[0].lista[i].predecesor].liniepred[0])) or (math.floor(v[0].lista[i].liniepreddest[1])!= math.floor(v[0].lista[v[0].lista[i].predecesor].liniepred[1])):
                        if v[0].lista[v[0].lista[i].predecesor].liniepred[0]>v[0].lista[i].liniepreddest[0]:
                            v[0].lista[i].liniepreddest[0]+=1
                        elif v[0].lista[v[0].lista[i].predecesor].liniepred[0]<v[0].lista[i].liniepreddest[0]:
                            v[0].lista[i].liniepreddest[0]-=1
                        if v[0].lista[v[0].lista[i].predecesor].liniepred[1]>v[0].lista[i].liniepreddest[1]:
                            v[0].lista[i].liniepreddest[1]+=1
                        elif v[0].lista[v[0].lista[i].predecesor].liniepred[1]<v[0].lista[i].liniepreddest[1]:
                            v[0].lista[i].liniepreddest[1]-=1
                        tmp=1
                        break
                    else:
                        v[0].lista[i].proces=False
                else:
                    v[0].lista[i].proces=False
                i-=1
        if tmp==0:
            v[0].proces=False
    else:
        match v[0].operatie:
            case "Inserare Inceput":
                inserareinc(v, mouse, mouse_presses)
            case "Inserare Sfarsit":
                inseraresf(v, mouse, mouse_presses)
            case "Inserare Mijloc":
                inseraremij(v, mouse, mouse_presses)
            case "Stergere Mijloc":
                stergeremij(v, mouse, mouse_presses)
        


def calcdr(v, mouse, mouse_presses):
    temp=1
    v[0].show=(v[0].campuri[2].info, v[0].campuri[3].info, v[0].campuri[4].info)
    if(mouse_presses[0] and v[0].adaugare and insidedr(v, (mouse))):
        for i in range(len(v[0].campuri)):
            if(insidemouse(mouse, (v[0].campuri[i].pozitie[0]+v[0].WIDTH/2, v[0].campuri[i].pozitie[1]+100, v[0].campuri[i].size[0], v[0].campuri[i].size[1]))) and v[0].campuri[i].op==v[0].operatie:
                if not(v[0].selected== -1):
                    v[0].campuri[v[0].selected].border=2
                v[0].selected=i
                v[0].campuri[i].border=4
                temp=0
        if(temp==1):
            v[0].campuri[v[0].selected].border=2
            v[0].selected=-1
        v[0].adaugare=False

def calcmij(v, mouse, mouse_presses):
    for i in range(3):
        v[0].butoane[i].click(v, mouse, mouse_presses)
    if not(v[0].proces):
        v[0].butoane[3].click(v, mouse, mouse_presses)
        v[0].butoane[4].click(v, mouse, mouse_presses)
        v[0].butoane[5].click(v, mouse, mouse_presses)
        v[0].butoane[7].click(v, mouse, mouse_presses)
        v[0].butoane[8].click(v, mouse, mouse_presses)
        v[0].butoane[10].click(v, mouse, mouse_presses)
    v[0].butoane[6].click(v, (mouse[0]-v[0].WIDTH/2, mouse[1]-100), mouse_presses)
    v[0].butoane[9].click(v, (mouse[0]-v[0].WIDTH/2, mouse[1]-100), mouse_presses)

def scrie(v, nr):
    if(nr==-1):
        v[0].campuri[v[0].selected].info=v[0].campuri[v[0].selected].info//10
    elif v[0].selected==2 or v[0].selected==3 or v[0].selected==4:
        v[0].campuri[v[0].selected].info=min(v[0].campuri[v[0].selected].info*10+nr,255)
    elif not(v[0].selected==-1) and not(v[0].campuri[v[0].selected].info//1000>0):
        v[0].campuri[v[0].selected].info=v[0].campuri[v[0].selected].info*10+nr
    
    
        
    
def switchnum(v, event):
    match event.key:
        case pygame.K_0:
            scrie(v, 0)
        case pygame.K_1:
            
            scrie(v, 1)
        case pygame.K_2:
            scrie(v, 2)
        case pygame.K_3:
            scrie(v, 3)
        case pygame.K_4:
            scrie(v, 4)
        case pygame.K_5:
            scrie(v, 5)
        case pygame.K_6:
            scrie(v, 6)
        case pygame.K_7:
            scrie(v, 7)
        case pygame.K_8:
            scrie(v, 8)
        case pygame.K_9:
            scrie(v, 9)
        case pygame.K_BACKSPACE:
            scrie(v, -1)
        


def pyg(v):
    mouse = pygame.mouse.get_pos()
    mouse_presses = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            switchnum(v, event)
    
    calcst(v, mouse, mouse_presses)
    calcdr(v, mouse, mouse_presses)
    calcmij(v, mouse, mouse_presses)
    

def main(v):
    pyg(v)