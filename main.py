import pygame
import random
width, height = 1000,1000
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("First Game")

#def variables
fps = 60
black=(0,0,0)
green=(0,255,255)
white=(255, 255, 255)

taille_case=20

w, h = 50, 50
grille = [[0 for x in range(w)] for y in range(h)]
voisin = [[0 for x in range(w)] for y in range(h)]

# aléatoire
for i in range(0, w):
    for j in range(0, h):
        if (random.random() >= 0.7):
            grille[i][j] = 1

def regle(grille,w,h):
    for i in range(0,w):
        for j in range(0, h):
            #if vivant
            if (grille[i][j] == 1):
                if (voisin[i][j] <= 1):
                    grille[i][j] = 0
                if (voisin[i][j] > 3):
                    grille[i][j] = 0

            #if mort
            else:
                if (voisin[i][j] == 3):
                    grille[i][j] = 1


def compte_voisin(grille,voisin,w,h):
    for i in range(0,w):
        for j in range(0, h):
            #encroix --------------------------
            # v_nord
            if (j>=1):
                if (grille[i][j-1] == 1):
                    voisin[i][j] += 1
            # v_sud
            if (j<=48):
                if (grille[i][j+1] == 1):
                    voisin[i][j] += 1
            # v_ouest
            if (i>=1):
                if (grille[i-1][j] == 1):
                    voisin[i][j] += 1
            # v_est
            if (i<=48):
                if (grille[i+1][j] == 1):
                    voisin[i][j] += 1

            #diag -----------------------------
            # v_nord_ouest
            if (j>=1) and (i>=1):
                if (grille[i-1][j-1] == 1):
                    voisin[i][j] += 1
            # v_nord_est
            if (j>=1) and (i<=48):
                if (grille[i+1][j-1] == 1):
                    voisin[i][j] += 1
            # v_sud_ouest
            if (j<=48) and (i>=1):
                if (grille[i-1][j+1] == 1):
                    voisin[i][j] += 1
            # v_sud_est
            if (j<=48) and (i<=48):
                if (grille[i+1][j+1] == 1):
                    voisin[i][j] += 1


def reset_voisin(voisin):
    for i in range(0, w):
        for j in range(0, h):
            voisin[i][j]=0

def remplie(grille,w,h):
    for i in range(0,w):
        for j in range(0, h):
            if (grille[i][j] == 1):
                pygame.draw.rect(win, green, pygame.Rect(taille_case*i, taille_case*j, taille_case, taille_case))
            #else:
                #pygame.draw.rect(win, white, pygame.Rect(20 * i, 20 * j, 20, 20))

#dessine quadrillage
def quadrille():
    for i in range(0,w+1):
        for j in range(0,h+1):
            pygame.draw.rect(win, black, pygame.Rect(0, 0, taille_case*i, taille_case*j), 2)

def draw_window():
    win.fill(white)
    quadrille()
    remplie(grille, w, h)
    compte_voisin(grille, voisin, w, h)
    regle(grille,w,h)
    reset_voisin(voisin)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    loop = True
    initial = True
    draw_window()
    while initial:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                initial = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x1=pos[0]//taille_case
                y1=pos[1]//taille_case
                grille[x1][y1] = 1
                pygame.draw.rect(win, green, pygame.Rect(0, 0, taille_case * x1, taille_case * y1), 2)
                remplie(grille, w, h)
                pygame.display.update()
                print("Click") #LAS
    while loop:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()