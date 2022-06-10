
"""
Création d'un jeu d'échec
créateur: Dekeister Clément
"""
#crée un damier vide
def création_damier():
    t=[[" " for i in range(8)]for j in range(8)]
    return t  

#affiche le damier
def affiche_damier(t):
    for j in range(8):
        print(j,t[j])

liste_des_pieces=["♙","♖","♘","♗","♕","♔","♟","♜","♞","♝","♛","♚"]
liste_des_pieces_blanche=["♖","♘","♗","♕","♔","♗","♘","♖","♙"]
liste_des_pieces_noire=["♜","♞","♝","♛","♚","♝","♞","♜","♟"]


#place les pions au début de la partie
def damier_debut(t):
    for j in range(8):
        t[0][j]=liste_des_pieces_noire[j]
        t[1][j]="♟"
        t[7][j]=liste_des_pieces_blanche[j]
        t[6][j]="♙"
    affiche_damier(t)
    return t
    
#detecte quel pièce est sur la case selectionné
def quelle_piece(t,x,y):
    if t[x][y] == " ":
        return None
    elif t[x][y] == "♜" or t[x][y] == "♖":
        t=deplacement_tour(t,x,y)
    elif t[x][y] == "♞" or t[x][y] == "♘":
        t=deplacement_cavalier(t,x,y)
    elif t[x][y] == "♝" or t[x][y] == "♗":
        t=deplacement_fou(t,x,y)
    elif t[x][y] == "♛" or t[x][y] == "♕":
        t=deplacement_dame(t,x,y)
    elif t[x][y] == "♚" or t[x][y] == "♔":
        t=deplacement_roi(t,x,y)
    elif t[x][y] == "♟" or t[x][y] == "♙":
        t=deplacement_pion(t,x,y)
    return t
#renvoie true si une case est libre
def est_libre(t,x,y):
    if t[x][y]==" ":
        return True
    else:
         return False

"""Création des fonctions de déplacement des différentes pièces"""
"""certaines sont chaotiques mais toute fonctionnent et normalement tte les conditions sont respectées"""
#vérifie et déplace le roi si il le peut
def deplacement_roi(t,x,y):
    x1=int(input("sur quelle case souhaitez-vous bouger? x: "))
    y1=int(input("y:" ))
    if x1 == x and y1 == y:
        print("vous êtes déjà sur cette case")
        return deplacement_roi(t,x,y)
    elif x1 > x-2 and x1 < x+2 :
        if y1 > y-2 and y1 < y+2 :
            if t[x][y] in liste_des_pieces_blanche and t[x1][y1] in liste_des_pieces_blanche :
                print("vous ne pouvez pas prendre votre pièce")
                return deplacement_roi(t,x,y)
            elif t[x][y] in liste_des_pieces_noire and t[x1][y1] in liste_des_pieces_noire :
                print("vous ne pouvez pas prendre votre pièce")
                return deplacement_roi(t,x,y)
            else:
                t[x1][y1]=t[x][y]
                t[x][y]=" "         
    else :
        print("tu ne peux pas te déplacer sur cette case choisi en une autre")
        deplacement_roi(t,x,y)
    affiche_damier(t)

#vérifie et déplace un pion si il le peut
def deplacement_pion(t,x,y):
    x1=int(input("sur quelle case souhaitez-vous bouger? x: "))
    y1=int(input("y:" ))
    #pion blanc
    if t[x][y] in liste_des_pieces_blanche:
        if y1==y and (x1==x-1 or x1==x-2) :
            if x==6 :
                if est_libre(t,x1,y1):
                    t[x1][y1]=t[x][y]
                    t[x][y]= " "
                else:
                    print("cette case est prise veuillez changer")
                    deplacement_pion(t,x,y)
            elif x1 == x-1 :
                if est_libre(t,x1,y1):
                    t[x1][y1]=t[x][y]
                    t[x][y]= " "
                    print(t[x1][y1])
                else:
                    print("cette case est prise veuillez changer")
                    deplacement_pion(t,x,y)
            else :
                print("cette case est prise veuillez changer")
                deplacement_pion(t,x,y)
        elif (y1==y-1 or y1==y+1) and x1==x-1:
            if est_libre(t,x1,y1):
                print("tu ne peux pas te déplacer sur cette case")
                deplacement_pion(t,x,y)
            else:
                if t[x1][y1] in liste_des_pieces_noire :
                    t[x1][y1]=t[x][y]
                    t[x][y]= " "
                else:
                    affiche_damier(t)  
                    print("cette case est prise veuillez changer")
        else:
            print("Vous ne pouvez pas vous déplacer à cet endroit")
            deplacement_pion(t,x,y)
    #pion noir
    else:
        if y1==y and (x1==x+1 or x1==x+2) :
            if x==1 :
                if est_libre(t,x1,y1):
                    t[x1][y1]=t[x][y]
                    t[x][y]= " "
                else:
                    print("cette case est prise veuillez changer")
                    deplacement_pion(t,x,y)
            elif x1==x+1:
                if est_libre(t,x1,y1):
                    t[x1][y1]=t[x][y]
                    t[x][y]= " "
                else:
                    print("cette case est prise veuillez changer")
                    deplacement_pion(t,x,y)
            else:
                print("tu ne peux pas te déplacer sur cette case")
                deplacement_pion(t,x,y)

        elif (y1==y-1 or y1==y+1) and x1==x+1:
            if est_libre(t,x1,y1):
                print("tu ne peux pas te déplacer sur cette case")
                deplacement_pion(t,x,y)
            else:
                if t[x1][y1] in liste_des_pieces_blanche :
                    t[x1][y1]=t[x][y]
                    t[x][y]= " "
                else:
                    print("vous essayez de prendre votre propre pièce")
                    deplacement_pion(t,x,y)
        else:
            print("vous ne pouvez pas aller ici")
            deplacement_pion(t,x,y)
    return t 

#vérifie et déplace une tour si elle le peut
def deplacement_tour(t,x,y):
    x1=int(input("sur quelle case souhaitez-vous bouger? x: "))
    y1=int(input("y:" ))
    if x==x1 and y==y1:
        print('vous êtes déjà sur cette case')
        return deplacement_tour(t,x,y)
    elif t[x1][y1] in liste_des_pieces_blanche and t[x][y] in liste_des_pieces_blanche :
        print("vous ne pouvez pas prendre votre pièce")
        return deplacement_tour(t,x,y)
    elif t[x1][y1] in liste_des_pieces_noire and t[x][y] in liste_des_pieces_noire :
        print("vous ne pouvez pas prendre votre pièce")
        return deplacement_tour(t,x,y)
    #axe  horizontal
    if x==x1 and y1>-1 and y1<8 :
        pos_y=y
        if  y>y1 :
            pos_y=pos_y-1
            if pos_y == y1 :
                t[x1][y1]=t[x][y]
                t[x][y]=" "
                return
            while pos_y != y1:
                if not est_libre(t,x,pos_y):
                    print("vous ne pouvez pas vous deplacer ici")
                    return deplacement_tour(t,x,y)
                pos_y=pos_y-1  
            t[x][y1]=t[x][y]
            t[x][y]=" "
        else:
            pos_y=pos_y+1
            if pos_y == y1 :
                t[x1][y1]=t[x][y]
                t[x][y]=" "
                return
            while pos_y != y1:
                if not est_libre(t,x,pos_y):
                    print("vous ne pouvez pas vous deplacer ici")
                    return deplacement_tour(t,x,y)
                pos_y=pos_y+1  
            t[x][y1]=t[x][y]
            t[x][y]=" "
    #axe vertical
    elif y==y1 and x1>-1 and x1<8:
        pos_x=x
        if  x>x1 : 
            pos_x=pos_x-1 
            if pos_x == x1:
                
                t[x1][y1]=t[x][y]
                print(t[x1][y1])
                t[x][y]=" "
                return
            while pos_x != x1:
                if not est_libre(t,pos_x,y):
                    print("vous ne pouvez pas vous deplacer ici")
                    return deplacement_tour(t,x,y)
                pos_x=pos_x-1 
            print(t[x][y]) 
            t[x1][y1]=t[x][y]
            t[x][y]=" "
        else:
            pos_x=pos_x+1 
            if pos_x == x1:
                t[x1][y]=t[x][y]
                t[x][y]=" "
                return
            while pos_x != x1:
                if not est_libre(t,pos_x,y):
                    print("vous ne pouvez pas vous deplacer ici")
                    return deplacement_tour(t,x,y)
                pos_x=pos_x+1 
            t[x1][y]=t[x][y]
            t[x][y]=" "
    #en cas de mauvais déplacement
    else:
        print("vous ne pouvez pas vous déplacer ici")
        return deplacement_tour(t,x,y)

#toujours pareil mais pour le fou
def deplacement_fou(t,x,y):
    x1=int(input("sur quelle case souhaitez-vous bouger? x: "))
    y1=int(input("y:" ))
    if not( y1<8 and y1>-1 and x1<8 and x1>-1):
        print("les coordonnées ne sont pas valides")
        deplacement_fou(t,x,y)
    pos_x=x
    pos_y=y
    if x1>x :
        res_x=1
    else:
        res_x=-1
    if y1>y:
        res_y=1
    else:
        res_y=-1
    pos_x,pos_y=pos_x+res_x,pos_y+res_y
    while not( pos_x == x1 and pos_y == y1 ):
        if est_libre(t,pos_x,pos_y):
            pos_x,pos_y=pos_x+res_x,pos_y+res_y
        else:
            print("nop")
            deplacement_fou(t,x,y)
        if not( pos_y<8 and pos_y>-1 and pos_x<8 and pos_x>-1) :
                print("vous ne pouvez pas vous déplacer à cet endroit")
                deplacement_fou(t,x,y)
    if est_libre(t,x1,y1):
        t[x1][y1]=t[x][y]
        t[x][y]=" "
    else:
        if (t[x][y]=="♝" and (t[x1][y1] in liste_des_pieces_blanche)) or ( t[x][y]=="♗" and (t[x1][y1] in liste_des_pieces_noire) ):
            t[x1][y1]=t[x][y]
            t[x][y]=" "
        else:
            print("vous ne pouvez pas vous déplacer à cet endroit")
            deplacement_fou(t,x,y)

#deplacement cavalier  
def deplacement_cavalier(t,x,y):
    x1=int(input("sur quelle case souhaitez-vous bouger? x: "))
    y1=int(input("y:" ))
    couleur=0
    #vérification que les pions sont dans l'échéquier
    if not(x1>-1 or x1<8 or y1>-1 or y1<8):
        print("vous êtes en dehors de l'échequier changez de coordonées")
        return deplacement_cavalier(t,x,y)
    #si cavalier noir couleur=0 ,couleur=1 autrement
    if t[x1][y1] in liste_des_pieces_blanche:
        couleur=1
    #je vérifie toutes les coordonées manuellement comme il y en a que 8
    if x1==x+2:
        if y1==y-1 or y1==y+1:
            res=True
        else:
            res=False
    elif x1==x+1:
        if y1==y-2 or y1==y+2:
            res=True
        else:
            res=False
    elif x1==x-1:
        if y1==y-2 or y1==y+2:
            res=True
        else:
            res=False
    elif x1==x-2:
        if y1==y-1 or y1==y+1:
            res=True
        else:
            res=False
    else :
        res=False
    if res :
        #vérification qu'il ne prends une piece de la même couleur
        if (t[x][y] =="♘" and couleur == 1) or (t[x][y]=="♞" and couleur == 0 ) :
            print("vous ne pouvez pas prendre votre propre pièce")
            return deplacement_cavalier(t,x,y)
        else:
            #déplacement de la pièce
            t[x1][y1]=t[x][y]
            t[x][y]=" "
    #tout les autres deplacements sont faux
    else:
        print("vous ne pouvez pas vous déplacer ici")
        return deplacement_cavalier(t,x,y)

#le meilleur pour la fin
def deplacement_dame(t,x,y):
    x1=int(input("sur quelle case souhaitez-vous bouger? x: "))
    y1=int(input("y:" ))
    #j'ai littéralement recopié les fonction tour et fou car il fallait que les 
    #fonctions renvoient un booléen sauf que quand j'essayé de modifié tour et fou
    #pour qu'elles fassent les 2 je les cassait donc j'ai préféré les refaire spécialement
    # pr la dame de toute façon le programme ne consomme pas tellement comparé a la 
    #puissance d'un ordi voilà c'est tout
    part1=deplacement_dame_part1(t,x,y,x1,y1)
    part2=deplacement_dame_part2(t,x,y,x1,y1)
    if part1 or part2 :
        t[x1][y1]=t[x][y]
        t[x][y]=" "
    else:
        print("vous ne pouvez pas vous déplacer ici ")
        return deplacement_dame(t,x,y)

#deplacement dame 1 pareil que le fou
def deplacement_dame_part1(t,x,y,x1,y1):
    if not( y1<8 and y1>-1 and x1<8 and x1>-1):
        return False
    pos_x=x
    pos_y=y
    if x1>x :
        res_x=1
    else:
        res_x=-1
    if y1>y:
        res_y=1
    else:
        res_y=-1
    pos_x,pos_y=pos_x+res_x,pos_y+res_y
    while not( pos_x == x1 and pos_y == y1 ) :
        if est_libre(t,pos_x,pos_y):
            pos_x,pos_y=pos_x+res_x,pos_y+res_y
        else:
            return False
        if not( pos_y<8 and pos_y>-1 and pos_x<8 and pos_x>-1) :
                return False
    if est_libre(t,x1,y1):
        return True
    else:
        if (t[x][y]=="♛" and (t[x1][y1] in liste_des_pieces_blanche)) or ( t[x][y]=="♕" and (t[x1][y1] in liste_des_pieces_noire) ):
            return True
        else:
            return False

#déplacement dame 2 pareil que la tour
def deplacement_dame_part2(t,x,y,x1,y1):
    if x==x1 and y==y1:
        return False
    elif t[x1][y1] in liste_des_pieces_blanche and t[x][y] in liste_des_pieces_blanche :
        return False
    elif t[x1][y1] in liste_des_pieces_noire and t[x][y] in liste_des_pieces_noire :
        return False
    #axe  horizontal
    if x==x1 and y1>-1 and y1<8 :
        pos_y=y
        if  y>y1 :
            pos_y=pos_y-1
            if pos_y == y1 :
                return False
            while pos_y != y1:
                if not est_libre(t,x,pos_y):
                    return False
                pos_y=pos_y-1  
            return True
        else:
            pos_y=pos_y+1
            if pos_y == y1 :
                return True
            while pos_y != y1:
                if not est_libre(t,x,pos_y):
                    return False
                pos_y=pos_y+1  
            return True
    #axe vertical
    elif y==y1 and x1>-1 and x1<8:
        pos_x=x
        if  x>x1 : 
            pos_x=pos_x-1 
            if pos_x == x1:
                return True
            while pos_x != x1:
                if not est_libre(t,pos_x,y):
                    return False
                pos_x=pos_x-1 
            print(t[x][y]) 
            return True
        else:
            pos_x=pos_x+1 
            if pos_x == x1:
                return True
            while pos_x != x1:
                if not est_libre(t,pos_x,y):
                    return False
                pos_x=pos_x+1 
            return True
    #en cas de mauvais déplacement
    else:
        return False

#gere les tours enfin pas la pièce tour ,les tours endin vous avez compris
def deroulement_du_jeu(t):
    #tant que jeu = True signifie que les 2 rois sont tjrs en vie
    jeu=True
    tour=0
    while jeu:
        if tour%2==0:
            print("tour n°",tour,"au joueur 1 de jouer")
            x=int(input("quelle pièce souhaitez-vous bouger? x: "))
            y=int(input("y:" ))
            #verifie que la pièce qu il veut bouger existe et qu'elle est a lui
            if t[x][y] in liste_des_pieces_blanche:
                tour=tour+1
                t=quelle_piece(t,x,y)
                affiche_damier(t)
            else:
                print("ces coordonées ne sont pas disponible")

        else:
            print("tour n°",tour,"au joueur 2 de jouer")
            x=int(input("quelle pièce souhaitez-vous bouger? x: "))
            y=int(input("y:" ))
            #verifie que la pièce qu il veut bouger existe et qu'elle est a lui
            if t[x][y] in liste_des_pieces_noire:
                tour=tour+1
                quelle_piece(t,x,y)
                affiche_damier(t)
            else:
                print("ces coordonnées ne sont pas disponibles")
                affiche_damier(t)
        if ("♔" not in liste_des_pieces_blanche) or ("♚" not in liste_des_pieces_noire) :
                jeu=False
    if "♔" not in liste_des_pieces_blanche :
        print("Félicitation joueur 2 tu as gagné")
    else:
        print("Félicitation joueur 1 tu as gagné")
    


if __name__ == "__main__":
    t=création_damier()
    damier_debut(t)
    deroulement_du_jeu(t)
    #/!\ partie test fonction déplacement /!\ 
    #t[3][7]="♕"
    #t[4][3]="♛"
    #affiche_damier(t)
    #deplacement_dame(t,4,3)
    #affiche_damier(t)
    #print(t[3][2])