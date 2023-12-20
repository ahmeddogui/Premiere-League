from controller.EquipesC import Equipes

#br = Brands()

liste_equipes = Equipes.visualiserEq()

print(liste_equipes)

listeEq = []

print("##################################")

for eq in liste_equipes:

    ideq = eq.getEquipeId()
    nom_equipe = eq.getNomDeEquipe()
    manager = eq.getManager()
    joueurs = eq.getJoueurs()



    print(ideq, nom_equipe, manager, joueurs)

    listeEq.append((ideq, nom_equipe, manager, joueurs)) # [], {}, (a,b)

print("**********************************")

print(listeEq)
#%%
