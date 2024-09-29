import pygame

def ecraninc(screen, v):
    mouse = pygame.mouse.get_pos()
    screen.fill(v[0].albastru)
    if(v[0].sel==1):
        v[0].butoane[6].colour=v[0].show
        v[0].butoane[6].hovercolour=v[0].show
    else:
        v[0].butoane[7].colour=v[0].show
        v[0].butoane[7].hovercolour=v[0].show
    for i in range(6) :
        v[0].butoane[i].draw(mouse)
        v[0].butoane[i].drawtxt(v, screen)
    if v[0].operatie=="Inserare Inceput" or v[0].operatie=="Inserare Mijloc" or v[0].operatie=="Inserare Sfarsit":
        v[0].butoane[6].draw(mouse)
        v[0].butoane[6].drawtxt(v, screen)
        v[0].butoane[7].draw(mouse)
        v[0].butoane[7].drawtxt(v, screen)
    v[0].butoane[8].draw(mouse)
    v[0].butoane[8].drawtxt(v, screen)
    v[0].butoane[10].draw(mouse)
    v[0].butoane[10].drawtxt(v, screen)

def suprafstanga(screen, v):
    screen.blit(v[0].surfacestanga, (0,100))
    v[0].surfacestanga.fill((v[0].alb))
    for i in range(v[0].liscount):
        v[0].lista[i].draw(v, v[0].surfacestanga)
        v[0].lista[i].drawtxt(v, v[0].surfacestanga)
    for i in range(v[0].liscount):
        v[0].lista[i].point(v, v[0].surfacestanga)

def suprafdreapta(screen, v):
    screen.blit(v[0].surfacedreapta, (v[0].WIDTH/2,100))
    v[0].surfacedreapta.fill(v[0].culoaretemp)
    for i in range(len(v[0].campuri)):
        if v[0].campuri[i].op==v[0].operatie:
            v[0].campuri[i].draw(v, v[0].surfacedreapta)
            v[0].campuri[i].drawtxt(v, v[0].surfacedreapta)
            v[0].campuri[i].drawnume(v, v[0].surfacedreapta)
    text = v[0].fonttitlu.render(str(v[0].operatie), False, v[0].negru)
    v[0].surfacedreapta.blit(text, (v[0].WIDTH/7+10,20))

def ecransf():
    pygame.display.update()

def main(screen, v):
    ecraninc(screen, v)
    suprafstanga(screen, v)
    suprafdreapta(screen, v)
    ecransf()
    