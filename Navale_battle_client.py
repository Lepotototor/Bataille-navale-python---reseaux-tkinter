# Script machine Client
# Envoi de message vers le serveur serveurSimple.py

import socket
import pickle
from random import randint
from copy import deepcopy
from tkinter import *
from tkinter.messagebox import showinfo
from time import time, sleep



def regles():

    #   arguments:
    #   ----------
    #       aucun
    #   renvoie:
    #   --------
    #       rien, elle affiche les règles du jeu
    #   préconditions:
    #   --------------
    #       aucune

    #----fenetre principale----

    interface_regles = Tk()
    interface_regles.title("Règles - Bataille Navale")

    interface_regles['bg'] = "#F0EBCA"

    #---Création des items du canevas et de leurs identifiants----
    label_regles1 = Label(interface_regles, text="Règles", bg="#F0EBCA", fg="#786c58", justify="center", wraplength="1000", font=("Arial",15))
    label_regles1.grid(row = 0, column = 0, padx = 15, pady =10)

    label_regles2 = Label(interface_regles, text="Commencer une partie de bataille navale :", bg="#F0EBCA", fg="#786c58", justify="center", wraplength="1000", font=("Arial",15))
    label_regles2.grid(row = 2, column = 0, padx = 15, pady =10)

    label_regles3 = Label(interface_regles, text="Au début du jeu, chaque joueur place à sa guise tous les bateaux sur sa grille de façon stratégique. Le but étant de compliquer au maximum la tache de son adversaire, c’est-à-dire détruire tous vos navires. Bien entendu, le joueur ne voit pas la grille de son adversaire.", bg="#F0EBCA", fg="#786c58", justify="center", wraplength="1000", font=("Arial",15))
    label_regles3.grid(row = 4, column = 0, padx = 15, pady =10)

    label_regles4 = Label(interface_regles, text="Une fois tous les bateaux en jeu, la partie peut commencer.. Un à un, les joueurs se tire dessus pour détruire les navires ennemis.", bg="#F0EBCA", fg="#786c58", justify="center", wraplength="1000", font=("Arial",15))
    label_regles4.grid(row = 6, column = 0, padx = 15, pady =10)

    label_regles5 = Label(interface_regles, text="Si un joueur tire sur un navire ennemi, le jeu le signale en disant « touché ». Il peut jouer plusieurs fois de suite tant qu'il touche un bateau de l'adversaire.", bg="#F0EBCA", fg="#786c58", justify="center", wraplength="1000", font=("Arial",15))
    label_regles5.grid(row = 8, column = 0, padx = 15, pady =10)

    label_regles6 = Label(interface_regles, text="Si le joueur ne touche pas de navire, le jeu le signale en disant « A l'eau » .", bg="#F0EBCA", fg="#786c58", justify="center", wraplength="1000", font=("Arial",15))
    label_regles6.grid(row = 10, column = 0, padx = 15, pady =10)

    label_regles7 = Label(interface_regles, text="Si le navire est entièrement touché le jeu le signale en disant « touché coulé ».", bg="#F0EBCA", fg="#786c58", justify="center", wraplength="1000", font=("Arial",15))
    label_regles7.grid(row = 12, column = 0, padx = 15, pady =10)

    label_regles8 = Label(interface_regles, text="Les cases bleues foncées et rouges servent à se souvenir des tirs ratés et les tirs touchés. Ces pions se placent sur la grille du dessous qui correspond aux bateaux de l'adversaire, la grille du dessus correspond à ses propes bateaux, les tirs et l'état des bateaux y paraissent.", bg="#F0EBCA", fg="#786c58", justify="center", wraplength="1000", font=("Arial",15))
    label_regles8.grid(row = 14, column = 0, padx = 15, pady =10)

    label_regles9 = Label(interface_regles, text="Comment gagner une partie de bataille navale:", bg="#F0EBCA", fg="#786c58", justify="center", wraplength="1000", font=("Arial",15))
    label_regles9.grid(row = 16, column = 0, padx = 15, pady =10)

    label_regles10 = Label(interface_regles, text="Une partie de bataille navale se termine lorsque l’un des joueurs n’a plus de navires.", bg="#F0EBCA", fg="#786c58", justify="center", wraplength="1000", font=("Arial",15))
    label_regles10.grid(row = 18, column = 0, padx = 15, pady =10)

    label_regles11 = Label(interface_regles, text="Astuces pour gagner à la bataille navale:", bg="#F0EBCA", fg="#786c58", justify="center", wraplength="1000", font=("Arial",15))
    label_regles11.grid(row = 20, column = 0, padx = 15, pady =10)

    label_regles12 = Label(interface_regles, text="Pour gagner plus rapidement, vous pouvez jouer vos tirs en croix, étant donné que le plus petit navire fait deux cases alors vous ne pourrez éviter aucun autre bateau sur votre chemin. Cette méthode est infaillible car elle est purement logique.", bg="#F0EBCA", fg="#786c58", justify="center", wraplength="1000", font=("Arial",15))
    label_regles12.grid(row = 22, column = 0, padx = 15, pady =10)
    return interface_regles

        
def defaite():

    #   arguments:
    #   ----------
    #       aucun
    #   renvoie:
    #   --------
    #       rien, elle affiche la défaite du joueur
    #   préconditions:
    #   --------------
    #       aucune

    #----fenetre principale----

    interface_defaite = Tk()
    interface_defaite.title("DEFAITE")

    interface_defaite.geometry("290x80")
    interface_defaite.resizable(width=False, height=False)
    
    texte="DEFAITE"

    texte_defaite = Label(interface_defaite, text=texte, fg="white", font=("Cooper Black",50), bg="#4f4f4f")
    texte_defaite.place(x=0, y=0)

    interface_defaite.mainloop()

def victoire():

    #   arguments:
    #   ----------
    #       aucun
    #   renvoie:
    #   --------
    #       rien, elle affiche la victoire du joueur
    #   préconditions:
    #   --------------
    #       aucune

    #----fenetre principale----

    interface_victoire = Tk()
    interface_victoire.title("VICTOIRE")

    #interdire la modification de la taille de la fenetre
    interface_victoire.geometry("320x80")
    interface_victoire.resizable(width=False, height=False)

    texte="VICTOIRE"

    texte_victoire = Label(interface_victoire, text=texte, fg="white", font=("Cooper Black",50), bg="#4f4f4f")
    texte_victoire.place(x=0, y=0)



    interface_victoire.mainloop()

def creation_grilles():

    #   arguments:
    #   ----------
    #       aucun
    #   renvoie:
    #   --------
    #       trois listes (grille_joueur_bateaux, grille_joueur_bateaux_ennemis, grille_adversaire_bateaux) : type list
    #   préconditions:
    #   --------------
    #       aucune

    #On créer les listes de listes qui serviront de grille de jeu
    grille_joueur_bateaux = [
        [" ~" for v in range(10)] for ligne in range(10)]
    grille_joueur_bateaux_ennemis = [
        [" ~" for v in range(10)] for ligne in range(10)]
    grille_adversaire_bateaux = [
        [" ~" for v in range(10)] for ligne in range(10)]

    return grille_joueur_bateaux, grille_joueur_bateaux_ennemis, grille_adversaire_bateaux


def affichage_grilles(grille_joueur_bateaux, grille_joueur_bateaux_ennemis):

    #   arguments:
    #   ----------
    #       deux listes (grille_joueur_bateaux, grille_joueur_bateaux_ennemis)
    #   renvoie:
    #   --------
    #       rien, cette fonction affiche les grilles des bateaux du joueur et des bateaux ennemis
    #   préconditions:
    #   --------------
    #       les deux listes rentrées en arguments doivent avoir été créée précédemment et contenir l'état actuel du jeu, elles doivent être composée de dix listes contenznt dix informations chacune

    #Fonction qui n'est pas utlisée dans le programme, elle n'est utile de l'utiliser que dans la console

    #Fonction qui va boucler sur les deux grilles d'un joueur pour les afficher
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print("Grille personnelle")
    print('  ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    for j in range(10):
        ligne = " " + str(j)
        for i in range(10):
            ligne += str(grille_joueur_bateaux[j][i])
        print(ligne)

    print('\n')
    print("Grille adversaire")
    print('  ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    for j in range(10):
        ligne = " " + str(j)
        for i in range(10):
            ligne += str(grille_joueur_bateaux_ennemis[j][i])
        print(ligne)


def tir(choix_case, grille_adversaire_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi, serveur):

    #   arguments:
    #   ----------
    #       trois listes (grille_adversaire_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi)
    #       choix_case : type str
    #       serveur : type class
    #   renvoie:
    #   --------
    #       dans le cas où le joueur touche un bateau ennemi qui n'a pas été touché : un booléen (True), trois listes (grille_ennemi_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi)
    #       dans le cas où le joueur touche un bateau ennemi qui a été touché : un str ("erreur"), trois listes (grille_ennemi_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi)
    #       dans le cas où le joueur tire dans l'eau : un booléen (False), trois listes (grille_ennemi_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi)
    #       dans le cas où le joueur tire dans une case d'eau où il a déjà tiré : un str ("erreur"), trois listes (grille_ennemi_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi)
    #   préconditions:
    #   --------------
    #       les trois listes rentrées en arguments doivent avoir été créée précédemment et contenir l'état actuel du jeu, elles doivent être composée de dix listes contenant dix informations chacune
    #       choix_case doit être de type str

    #On vérifie que les coordonnées soient bonnes
    if len(choix_case)!=2:
        return "erreur", grille_adversaire_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi

    serveur.send(choix_case.encode())

    for i in range(len(grille_adversaire_bateaux)):
        # On cycle sur tout le tableau des bateaux ennemis jusqu'à trouver la case des coordonnées
        for a in range(len(grille_adversaire_bateaux[i])):
            if choix_case == str(a)+str(i):

                if grille_adversaire_bateaux[i][a] == " o":
                    grille_adversaire_bateaux[i][a] = " Ø"
                    grille_joueur_bateaux_ennemis[i][a] = " Ø"

                    for u in range(len(bateaux_vivants_ennemi)):
                        # On cycle dans le tableau des bateaux vivants de l'ennemi
                        # pour pouvoir enlever celui qui a été abattu
                        for o in range(len(bateaux_vivants_ennemi[u])):
                            if bateaux_vivants_ennemi[u][o] == str(a)+str(i):
                                del bateaux_vivants_ennemi[u][o]
                                break

                    return True, grille_adversaire_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi

                elif grille_adversaire_bateaux[i][a] == " Ø":
                    print("Cette partie du bâteau a déja été attaquée")
                    return "erreur", grille_adversaire_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi

                elif grille_adversaire_bateaux[i][a] == " ☼":
                    print("Vous avez déja attaqué sur cette case")
                    return "erreur", grille_adversaire_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi

                elif grille_adversaire_bateaux[i][a] == " ~":
                    grille_adversaire_bateaux[i][a] = " ☼"
                    grille_joueur_bateaux_ennemis[i][a] = " ☼"
                    return False, grille_adversaire_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi

def tir_adversaire(choix_case, grille_adversaire_bateaux, bateaux_vivants_joueur):

    #   arguments:
    #   ----------
    #       deux listes (ggrille_adversaire_bateaux, bateaux_vivants_joueur)
    #       choix_case : type str
    #       serveur : type class
    #   renvoie:
    #   --------
    #       dans le cas où le joueur touche un bateau ennemi qui n'a pas été touché : un booléen (True), deux listes (ggrille_adversaire_bateaux, bateaux_vivants_joueur)
    #       dans le cas où le joueur touche un bateau ennemi qui a été touché : un str ("erreur"), deux listes (ggrille_adversaire_bateaux, bateaux_vivants_joueur)
    #       dans le cas où le joueur tire dans l'eau : un booléen (False), deux listes (ggrille_adversaire_bateaux, bateaux_vivants_joueur)
    #       dans le cas où le joueur tire dans une case d'eau où il a déjà tiré : un str ("erreur"), deux listes (ggrille_adversaire_bateaux, bateaux_vivants_joueur)
    #   préconditions:
    #   --------------
    #       les trois listes rentrées en arguments doivent avoir été créée précédemment et contenir l'état actuel du jeu, elles doivent être composée de dix listes contenant dix informations chacune
    #       choix_case doit être de type str

    #On vérifie que les coordonnées soient bonnes
    if len(choix_case)!=2:
        return "erreur", grille_adversaire_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_joueur

    for i in range(len(grille_adversaire_bateaux)):
        # On cycle sur tout le tableau des bateaux ennemis jusqu'à trouver la case des coordonnées
        for a in range(len(grille_adversaire_bateaux[i])):
            if choix_case == str(a)+str(i):

                if grille_adversaire_bateaux[i][a] == " o":
                    grille_adversaire_bateaux[i][a] = " Ø"

                    for u in range(len(bateaux_vivants_joueur)):
                        # On cycle dans le tableau des bateaux vivants de l'ennemi
                        # pour pouvoir enlever celui qui a été abattu
                        for o in range(len(bateaux_vivants_joueur[u])):
                            if bateaux_vivants_joueur[u][o] == str(a)+str(i):
                                del bateaux_vivants_joueur[u][o]
                                break

                    return True, grille_adversaire_bateaux, bateaux_vivants_joueur

                elif grille_adversaire_bateaux[i][a] == " Ø":
                    print("Cette partie du bâteau a déja été attaquée")
                    return "erreur", grille_adversaire_bateaux, bateaux_vivants_joueur

                elif grille_adversaire_bateaux[i][a] == " ☼":
                    print("Vous avez déja attaqué sur cette case")
                    return "erreur", grille_adversaire_bateaux, bateaux_vivants_joueur

                elif grille_adversaire_bateaux[i][a] == " ~":
                    grille_adversaire_bateaux[i][a] = " ☼"
                    return False, grille_adversaire_bateaux, bateaux_vivants_joueur


def implantation_bateaux_dans_grille(coordonnees_bateaux, grille_joueur_bateaux):

    #   arguments:
    #   ----------
    #       deux listes (coordonnees_bateaux, grille_joueur_bateaux)
    #       serveur : type class
    #   renvoie:
    #   --------
    #       rien, cette fonction modifie la liste grille_joueur_bateaux en y ajoutant aux bons endroits les places où se situent des bateaux
    #   préconditions:
    #   --------------
    #       coordonnees_bateaux doit contenir les coordonnées de 5 bateaux pour respecter les règles du jeu
    #       grille_joueur_bateaux doit avoir été créée précédemment et ne doit contenir que dix listes de dix caractères "~"

    #placer les bateaux en fonction de leurs coordonnées (11,12,13...)
    for i in coordonnees_bateaux:
        #On va aux coordonnées de chaque point de bateau pour y définir un emplacement de bateau
        temp = str(i)
        colonne = temp[0]
        ligne = temp[1]
        grille_joueur_bateaux[int(ligne)][int(colonne)] = ' O'


def coordonnees(grille_joueur_bateaux, grille_joueur_bateaux_ennemis, fenetre):

    #   arguments:
    #   ----------
    #       deux listes (grille_joueur_bateaux, grille_joueur_bateaux_ennemis)
    #       serveur : type class
    #   renvoie:
    #   --------
    #       trois listes (grille_joueur_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_joueur)
    #   préconditions:
    #   --------------
    #       les deux listes rentrées en arguments doivent avoir été créée précédemment et contenir l'état actuel du jeu, elles doivent être composée de dix listes contenant dix informations chacune

    #choix place bateaux joueur

    #On affiche une grille pour aider le joueur à se situer pour poser ses bateaux
    affichage_grilles(grille_joueur_bateaux, grille_joueur_bateaux_ennemis)

    print(f"Choix des positions de vos bateaux (position: '01' -> le 0 correspond à l'horizontal et le 1 à la vertical):")
    porte_avions = verification_grille(grille_joueur_bateaux, "Donnez les coordonnées du porte avion (longueur : 5), des cases alignées. (type : 01 02 03 04 05) : ", 5)
    affichage_grilles(grille_joueur_bateaux, grille_joueur_bateaux_ennemis)
    croiseur = verification_grille(grille_joueur_bateaux, "Donnez les coordonnées du croiseur (longueur : 4), des cases alignées. (type : 21 22 23 24 ) : ", 4)
    affichage_grilles(grille_joueur_bateaux, grille_joueur_bateaux_ennemis)

    premier_contre_tp = verification_grille(grille_joueur_bateaux, "Donnez les coordonnées du premier contre-torpilleurs (longueur : 3), des cases alignées. (type : 41 42 43) : ", 3)
    affichage_grilles(grille_joueur_bateaux, grille_joueur_bateaux_ennemis)

    deuxieme_contre_tp = verification_grille(grille_joueur_bateaux, "Donnez les coordonnées du deuxieme contre-torpilleurs (longueur : 3), des cases alignées. (type : 61 62 63) : ", 3)
    affichage_grilles(grille_joueur_bateaux, grille_joueur_bateaux_ennemis)

    torpilleur = verification_grille(grille_joueur_bateaux, "Donnez les coordonnées du torpilleur (longueur : 2), des cases alignées. (type : 81 82) : ", 2)
    affichage_grilles(grille_joueur_bateaux, grille_joueur_bateaux_ennemis)

    bateaux_vivants_joueur = [porte_avions, croiseur, premier_contre_tp, deuxieme_contre_tp, torpilleur]


    affichage_grilles(grille_joueur_bateaux, grille_joueur_bateaux_ennemis)
    input("Voici votre grille de jeu (touche 'Entrée' pour passer)")

    return grille_joueur_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_joueur


def verification_grille(grille_joueur_bateaux, nb_case, bateau):

    #   arguments:
    #   ----------
    #       une listes (grille_joueur_bateaux)
    #       un str (txt)
    #       un int (nb_case)
    #   renvoie:
    #   --------
    #       bateau : type list

    complet = True

    if len(bateau) < nb_case:
        showinfo("Erreur", "Il n'y a pas assez de parcelles de bateau")
        aligne = False
        troue = True
    elif len(bateau) > nb_case:
        showinfo("Erreur", "Il y a trop de parcelles de bateau")
        aligne = False
        troue = True
    else:
        abs = bateau[0][0]
        ord = bateau[0][1]
        aligne = True
        for i in bateau:
             if (i[0]!=abs) and (i[1]!=ord) and (aligne):
                 showinfo("Erreur", "Les morceaux ne sont pas alignés")
                 aligne = False
                 troue = True
    if aligne:
        ligne = True
        for i in bateau:
            if i[0]!=abs:
                ligne = False
        if ligne:
            k = 1
        else:
            k = 0

        if int(bateau[0][k]) < int(bateau[1][k]):
             troue = False
             for i in range(len(bateau)-1):
                 if int(bateau[i][k]) + 1 != int(bateau[i+1][k]):
                     troue = True
                     showinfo("Erreur", "Il y a un trou dans votre bateau")
                     break
        else:
             troue = False
             for i in range(len(bateau)-1):
                 if int(bateau[i][k]) - 1 != int(bateau[i+1][k]):
                     troue = True
                     showinfo("Erreur", "Il y a un trou dans votre bateau")
                     break
    return not troue

def ajout_coordonne(event):
    global grille_joueur_bateaux, identifiant_vers_case_bateaux, coordonnees_bateaux, iden_bateaux, bateaux_places

    if bateaux_places < 5:
        (iden,) = plateau_bateaux.find_closest(event.x, event.y)
        (col, lig) = identifiant_vers_case_bateaux[iden - 1]
        identifiant_case = str(identifiant_vers_case_bateaux[iden-1][0]) + str(identifiant_vers_case_bateaux[iden-1][1])

        if grille_joueur_bateaux[lig][col] == " v":
            grille_joueur_bateaux[lig][col] = " ~"
            plateau_bateaux.itemconfig(iden, fill = "#7BB2F9")
            del coordonnees_bateaux[coordonnees_bateaux.index(identifiant_case)]
            del iden_bateaux[iden_bateaux.index(iden)]
        elif grille_joueur_bateaux[lig][col] == " o":
            showinfo("Erreur", "Il y a déja une parcelle de bateau")
        else:
            grille_joueur_bateaux[lig][col] = " v"
            plateau_bateaux.itemconfig(iden, fill = 'pink')
            coordonnees_bateaux.append(identifiant_case)
            iden_bateaux.append(iden)

def valider_coordonne(event=""):
    global infos_bateaux, coordonnees_bateaux, iden_bateaux, bateaux_vivants_joueur, grille_joueur_bateaux, bateaux_places, fenetre, etiquette_joueur, bouton_valider, serveur
    if bateaux_places < 5:
        if verification_grille(grille_joueur_bateaux, infos_bateaux[bateaux_places][1], coordonnees_bateaux):
            bateaux_vivants_joueur.append(deepcopy(coordonnees_bateaux))
            bateaux_places += 1

            for coordonne in coordonnees_bateaux:
                grille_joueur_bateaux[int(coordonne[1])][int(coordonne[0])] = " o"
            for i in range(10):
                for j in range(10):
                    if grille_joueur_bateaux[i][j] == " o":
                        txt = plateau_bateaux.create_text(17+j*35, 22+i*35, fill="#141519", text = "", font=('Helvetica', 25, 'bold'))
                        plateau_bateaux.itemconfig(txt, text="o")

            etiquette_joueur.destroy()
            if bateaux_places == 5:
                bouton_valider.destroy()
                plateaux_jeux(fenetre)
            else:
                etiquette_joueur = Label(fenetre, text=infos_bateaux[bateaux_places][0], bg="#4f4f4f", fg="white", justify="center", wraplength="300", font=("Arial",15))
                etiquette_joueur.grid(row = 2, column = 0, columnspan = 3, padx = 15, pady =10)
        else:
            for coordonne in coordonnees_bateaux:
                grille_joueur_bateaux[int(coordonne[1])][int(coordonne[0])] = " ~"
        coordonnees_bateaux = []
        for iden in iden_bateaux:
            plateau_bateaux.itemconfig(iden, fill = "#7BB2F9")

#LES DEUX FONCTIONS SUIVANTES SERVENT POUR JOUER CONTRE UN ORDINATEUR, CELUI CI N'ETANT PAS SUFFISAMMENT AU POINT, ON UTILISE PAS CES FONCTIONS

def coordonnees_adversaire(grille_adversaire_bateaux):

    #   arguments:
    #   ----------
    #       une listes (grille_adversaire_bateaux)
    #   renvoie:
    #   --------
    #       grille_adversaire_bateaux, bateaux_vivants_ennemi : type list

    porte_avions = verification_adversaire(grille_adversaire_bateaux, 5)
    croiseur = verification_adversaire(grille_adversaire_bateaux, 4)
    premier_contre_tp = verification_adversaire(grille_adversaire_bateaux, 3)   #On definit chaque bateau
    deuxieme_contre_tp = verification_adversaire(grille_adversaire_bateaux, 3)
    torpilleur = verification_adversaire(grille_adversaire_bateaux, 2)

    bateaux_vivants_ennemi = [porte_avions, croiseur, premier_contre_tp, deuxieme_contre_tp, torpilleur]    #on definit la liste de bateaux de l'ennmi
    return grille_adversaire_bateaux, bateaux_vivants_ennemi

def verification_adversaire(grille_adversaire_bateaux, nb_cases):

    #   arguments:
    #   ----------
    #       une listes (grille_adversaire_bateaux)
    #       un int : nb_cases
    #   renvoie:
    #   --------
    #       bateau : type list

    direction = randint(0, 1)       #On choisit aleatoirement la direction du bateau
    case_depart = str(randint(0, 9)) + str(randint(0, 9))      #Et on pren un point aleatoire sur le plan
    bateau = [case_depart]                  #On definit le premier emplacement du bateau
    case_depart = list(case_depart)
    if int(case_depart[direction]) + nb_cases < 10:
        sens = 1
    else:               #On verifit si il y a assez de place pour aller dans le sens sinon on va en sens inverse
        sens = -1
    for i in range(1, nb_cases):
        case_depart[direction] = str(int(case_depart[direction]) + sens)
        case = case_depart[0] + case_depart[1]      #Donc on definit un nouvel emplacement dans le sens et la direction definit
        bateau.append(case)                         #pour que le bateau soit bien aligné

    implantation_bateaux_dans_grille(bateau, grille_adversaire_bateaux)
    return bateau

def tour_joueur(event):

    #   arguments:
    #   ----------
    #       event
    #   renvoie:
    #   --------
    #       rien, elle utilise des variables globales

    global game, grille_joueur_bateaux, grille_joueur_bateaux_ennemis, grille_adversaire_bateaux, bateaux_vivants_ennemi, serveur

    if game:
        (iden,) = plateau_bateaux_ennnemis.find_closest(event.x, event.y)
        (col, lig) = identifiant_vers_case_bateaux_ennemis[iden - 1]
        if grille_joueur_bateaux_ennemis[lig][col] != ' ~':
            showinfo("Erreur", "Vous avez déja attaqué sur cette case")
        else:
            choix_case = str(col) + str(lig)
            txt = plateau_bateaux_ennnemis.create_text(17+col*35, 22+lig*35, fill="#141519", text = "", font=('Helvetica', 25, 'bold'))

            resultat, grille_adversaire_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi = tir(
                choix_case, grille_adversaire_bateaux, grille_joueur_bateaux_ennemis, bateaux_vivants_ennemi, serveur)


            if resultat:
                restant_partie_bateaux = 0
                for a in bateaux_vivants_ennemi:
                    restant_partie_bateaux += len(a)
                plateau_bateaux_ennnemis.itemconfig(iden, fill = '#D12C2C')
                showinfo("Info", f"Touché !! \n\nIl reste {restant_partie_bateaux} parties de bateaux à toucher")

            elif resultat == False:
                plateau_bateaux_ennnemis.itemconfig(iden, fill = '#005DDC')
                showinfo("Info", "A l'eau !!")


            #On regarde si il y a un toucher-coulé
            for i in range(len(bateaux_vivants_ennemi)):
                if bateaux_vivants_ennemi[i] == []:
                    del bateaux_vivants_ennemi[i]
                    restant_bateaux = len(bateaux_vivants_ennemi)
                    showinfo("Info", f"Touché-coulé, il reste {restant_bateaux} bateaux à couler")
                    break

            #On vérifie que la partie n'est pas gagnée par le joueur
            if bateaux_vivants_ennemi == []:
                game = False
                victoire()

        if not resultat:
            tour_adversaire()


def tour_adversaire():

    #   arguments:
    #   ----------
    #       aucun
    #   renvoie:
    #   --------
    #       rien, elle utilise des variables globales

    global game, grille_joueur_bateaux, grille_joueur_bateaux_ennemis, grille_adversaire_bateaux, bateaux_vivants_joueur, plateau_bateaux, case_vers_identifiant_bateaux_ennemis, identifiant_vers_case_bateaux_ennemis, serveur

    if game:
        resultat = True
        while resultat == True:
            resultat = "erreur"
            while resultat == "erreur":
                choix_case = serveur.recv(25000).decode()
                resultat, grille_joueur_bateaux, bateaux_vivants_joueur = tir_adversaire(
                    choix_case, grille_joueur_bateaux, bateaux_vivants_joueur)
                (iden,) = plateau_bateaux.find_closest(17+int(choix_case[0])*35, 22+int(choix_case[1])*35)
                txt = plateau_bateaux.create_text(17+int(choix_case[0])*35, 22+int(choix_case[1])*35, fill="#141519", text = "", font=('Helvetica', 25, 'bold'))

            if resultat:
                restant_partie_bateaux = 0
                for a in bateaux_vivants_joueur:
                    restant_partie_bateaux += len(a)
                plateau_bateaux.itemconfig(iden, fill = '#D12C2C')
                plateau_bateaux.itemconfig(txt, fill='#D12C2C', text="/")
                showinfo("Info", f"Vous avez été touché !! \n\nIl vous reste {restant_partie_bateaux} parties de bateaux en vie")

            elif resultat == False:
                plateau_bateaux.itemconfig(iden, fill = '#005DDC')
                showinfo("Info", "Le joueur adverse a tiré dans l'eau !!")


            #On regarde si il y a un toucher-coulé
            for i in range(len(bateaux_vivants_joueur)):
                if bateaux_vivants_joueur[i] == []:
                    del bateaux_vivants_joueur[i]
                    restant_bateaux = len(bateaux_vivants_joueur)
                    showinfo("Info", f"Touché-coulé, il reste {restant_bateaux} bateaux en vie")
                    break


            #On vérifie que la partie n'est pas gagnée par le joueur
            if bateaux_vivants_joueur == []:
                game = False
                defaite()



def interface_jeu():

    #   arguments:
    #   ----------
    #       aucun
    #   renvoie:
    #   --------
    #       widgets :  fenetre, plateau_bateaux, plateau_bateaux_ennnemis
    #       tableaux de correspondance entre les items du canevas plateau et leurs identifiants : case_vers_identifiant, identifiant_vers_case


    #----fenetre principale----
    fenetre = Tk()
    fenetre.title("Bataille navale")
    fenetre.call('wm','iconphoto',fenetre._w,PhotoImage(file="image_fenetre.png"))
    #construire la fenetre à 100 pixels du cote gauche de l'ecran et 150 pixels du cote haut
    fenetre.geometry("385x750+100+150")
    #interdire la modification de la taille de la fenetre
    fenetre.resizable(width=False, height=False)
    fenetre['bg'] = "#4f4f4f"

    #----Canevas----
    #il faut diriger les entrées claviers vers le canevas qui n'a pas le focus par défaut
    #voir http://tkinter.fdex.eu/doc/focus.html#focus
    plateau_bateaux = Canvas(fenetre, width = COTE_CASE * 10, height = COTE_CASE * 10, bg = '#15DEA5', takefocus = 1)
    plateau_bateaux.grid(row = 1, column = 0, columnspan = 3, padx =15, pady = 10)

    #---Création des items du canevas et de leurs identifiants----
    case_vers_identifiant_bateaux = [ [0 for j in range(10)] for i in range(10) ]
    identifiant_vers_case_bateaux = [ (0,0) for k in range(100) ]

    boole=False
    for lig in range(10):
        for col in range(10):
            (x, y) = (col * COTE_CASE, lig * COTE_CASE)
            iden_bateaux = plateau_bateaux.create_rectangle(x, y , x + COTE_CASE, y + COTE_CASE,
                                            outline = COULEUR_BORD_CASE,
                                            fill= COULEUR_CASE[0], width=2)

            identifiant_vers_case_bateaux[iden_bateaux - 1] = (col, lig)
            case_vers_identifiant_bateaux[lig][col] = iden_bateaux

    # renvoie des widgets et des tableaux de correspondance items graphiques <-> identifiants
    return fenetre, plateau_bateaux, case_vers_identifiant_bateaux, identifiant_vers_case_bateaux

def plateaux_jeux(fenetre):
    #   arguments:
    #   ----------
    #       la fenetre principal
    #   renvoie:
    #   --------
    #       widgets :  plateaux_bateaux, plateau_bateaux_ennnemis
    #       tableaux de correspondance entre les items du canevas plateau et leurs identifiants : case_vers_identifiant, identifiant_vers_case

    #On cree le widget pour representer la grille ou l'on va attaquer
    global plateau_bateaux_ennnemis, case_vers_identifiant_bateaux_ennemis, identifiant_vers_case_bateaux_ennemis, serveur, bateaux_vivants_joueur, grille_joueur_bateaux, bateaux_vivants_ennemi, grille_adversaire_bateaux
    plateau_bateaux_ennnemis = Canvas(fenetre, width = COTE_CASE * 10, height = COTE_CASE * 10, bg = '#15DEA5', takefocus = 1, cursor="tcross")
    plateau_bateaux_ennnemis.grid(row = 2, column = 0, columnspan = 3, padx = 15, pady =10)

    #---Création des items du canevas et de leurs identifiants----
    case_vers_identifiant_bateaux_ennemis = [ [0 for j in range(10)] for i in range(10) ]
    identifiant_vers_case_bateaux_ennemis = [ (0,0) for k in range(100) ]

    serveur.send("c'est bon".encode())
    bateaux_vivants_ennemi, grille_adversaire_bateaux = envoi_recu_donnees(serveur, bateaux_vivants_joueur, grille_joueur_bateaux)

    boole=False
    for lig in range(10):
        for col in range(10):
            (x, y) = (col * COTE_CASE, lig * COTE_CASE)
            iden_bateaux_ennemis = plateau_bateaux_ennnemis.create_rectangle(x, y , x + COTE_CASE, y + COTE_CASE,
                                            outline = COULEUR_BORD_CASE,
                                            fill= COULEUR_CASE[0], width=2)

            identifiant_vers_case_bateaux_ennemis[iden_bateaux_ennemis - 1] = (col, lig)
            case_vers_identifiant_bateaux_ennemis[lig][col] = iden_bateaux_ennemis
    showinfo("Info", "La fenêtre supérieur correpond à votre grille, les bateaux sont représentées par des ronds noirs. \nSi ce rond devient un ron barré rouge, vous avez été touché, si une case devient bleu foncé, l'adversaire a tiré dans l'eau.\nLa fenêtre inférieur correspond à celle de l'ennemi, il suffit de cliquer sur la case où vous voulez tirer,\nSi vous touchez, la case devient rouge, et si vous ne touchez pas, elle devient bleue.")

    fenetre.update()
    plateau_bateaux_ennnemis.bind('<ButtonPress-1>', tour_joueur)

    premier_joueur=serveur.recv(25000)
    premier_joueur=premier_joueur.decode()

    if int(premier_joueur):
        showinfo('Info', "l'adversaire commence à jouer.")
        tour_adversaire()
    else:
        showinfo('Info', "vous commencer à jouer.")

def envoi_recu_donnees(serveur, bateaux_vivants_joueur, grille_joueur_bateaux):
    #On recuper les variables correspondant aux caracteristiques de l'adversaire
    donnees = serveur.recv(250000)
    bateaux_vivants_ennemi=pickle.loads(donnees)
    donnees = serveur.recv(250000)
    grille_adversaire_bateaux=pickle.loads(donnees)

    sleep(0.3)

    donnees=pickle.dumps(bateaux_vivants_joueur)
    serveur.send(donnees)
    donnees=pickle.dumps(grille_joueur_bateaux)
    serveur.send(donnees)

    return bateaux_vivants_ennemi, grille_adversaire_bateaux

def valider_input(event=""):
    global hote
    hote = entry_input.get()
    fenetre_input.destroy()

# _____________________________________________________________________________________________________________________________
#|                                                                                                                             |
#|                                                  PROGRAMME PRINCIPAL                                                        |
#|_____________________________________________________________________________________________________________________________|
# Constantes du programme

#Couleurs
COULEUR_CASE = ["#7BB2F9","green", "#3E61EA"]
COULEUR_BORD_CASE ="#887234"
COULEUR_BOUTON = "#3E61EA"
COULEUR_JOUEUR = {'JOUEUR_1' : 'Bleu', 'JOUEUR_2' : 'Vert'}

#Coté d'une case en pixels
COTE_CASE = 35

#On connecte à l'autre ordinateur
hote = ""      # Adresse IP du serveur

fenetre_input = Tk()
fenetre_input.title("Connexion")
fenetre_input.geometry("320x150")
fenetre_input['bg'] = "#F0EBCA"

entry_input = Entry(fenetre_input, text="Adresse IP", fg="#786c58", justify="center", bg="#F0EBCA", font=("Arial",19))
entry_input.grid(row = 0, column = 0, padx = 15, pady =10)

bouton_valider = Button(fenetre_input, text='Valider', anchor='center', command=valider_input, bg="#e7d5b8", fg="#786c58")
bouton_valider.grid(row=1, column=0, padx=15, pady=10)

fenetre_input.bind('<Return>', valider_input)

fenetre_input.mainloop()


port = 50000        # Port du serveur
# Déclaration de la connexion réseau
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.connect((hote, port))


game = True

#########
#tkinter#
#########

fenetre, plateau_bateaux, case_vers_identifiant_bateaux, identifiant_vers_case_bateaux = interface_jeu()

grille_joueur_bateaux, grille_joueur_bateaux_ennemis, grille_adversaire_bateaux = creation_grilles()

infos_bateaux = [("Donnez les coordonnées du porte avion (longueur : 5), des cases alignées", 5),
                 ("Donnez les coordonnées du croiseur (longueur : 4), des cases alignées", 4),
                 ("Donnez les coordonnées du premier contre-torpilleur (longueur : 3), des cases alignées", 3),
                 ("Donnez les coordonnées du deuxième contre-torpilleur (longueur : 3), des cases alignées", 3),
                 ("Donnez les coordonnées du torpilleur (longueur : 2), des cases alignées", 2)]
coordonnees_bateaux = []
iden_bateaux = []
bateaux_vivants_joueur = []
bateaux_places = 0

etiquette_joueur = Label(fenetre, text=infos_bateaux[bateaux_places][0], bg="#4f4f4f", fg="white", justify="center", wraplength="300", font=("Arial",15))
etiquette_joueur.grid(row = 2, column = 0, columnspan = 3, padx = 15, pady =10)

bouton_valider = Button(fenetre, text='Valider', command=valider_coordonne, bg="#6f6f6f", fg="white")
bouton_valider.grid(row = 3, column = 0, columnspan = 3, padx = 15, pady =10)

plateau_bateaux.bind('<ButtonPress-1>', ajout_coordonne)
fenetre.bind('<Return>', valider_coordonne)
fenetre.bind('<space>', valider_coordonne)

plateau_bateaux_ennnemis, case_vers_identifiant_bateaux_ennemis, identifiant_vers_case_bateaux_ennemis, bateaux_vivants_ennemi, grille_adversaire_bateaux = Canvas(), "", "", "", ""

#on presente les label_regles
interface_regles=regles()

#On rentre dans la partie même où les joueurs s'attaquent chacun leur tour

    
interface_regles.mainloop()
fenetre.mainloop()

serveur.close()
socket.close()
