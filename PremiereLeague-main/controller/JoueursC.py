import sys
sys.path.insert(0, 'C:/Users/ahmed/OneDrive/Bureau/AHMED/PremiereLeague-main')
from dao.JoueursDAO import *
import model
from model import JoueursM

class Joueurs:

    @staticmethod
    def visualiserJoueur():

        try:

            jDAO = JoueursDAO()

            js: list[JoueursM.Joueurs] = jDAO.trouverTout()

            if js==None :
                return "ERROR"

            return js

        except Exception as e:
            print(f'Erreur_JoueursC.visualiserJ() ::: {e}')

        return None

    @staticmethod
    def visualiserUnJ(idJ):

        try:

            jDAO = JoueursDAO()

            j: JoueursM.Joueurs = jDAO.trouverUn(idJ)

            if j==None :
                return "ERROR"

            return j

        except Exception as e:
            print(f'Erreur_JoueursC.visualiserUnJ() ::: {e}')

        return None


    @staticmethod
    def ajouterUnJ(idJ, nomJoueur, premonJoueur, position, nombreDeBut, nombreDePassesD, distanceParcurue):

        try:

            jDAO = JoueursDAO()

            objJ = JoueursM.Joueurs()

            objJ.setJoueurId(idJ)
            objJ.setNom(nomJoueur)
            objJ.setPrenom(premonJoueur)
            objJ.setPosition(position)
            objJ.setNombreDeBut(nombreDeBut)
            objJ.setNombreDePassesD(nombreDePassesD)
            objJ.setDistanceParcurue(distanceParcurue)


            j: int = jDAO.insererUn(objJ)

            if j==0:
                return "ERROR"

            return "AJOUT J AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_JoueursC.ajouterUnJ() ::: {e}')

        return None

    @staticmethod
    def modifierUnJ(idJ, nomJoueur, premonJoueur, position, nombreDeBut, nombreDePassesD, distanceParcurue):

        try:

            jDAO = JoueursDAO()
            objJ = JoueursM.Joueurs()

            # objJ.setJoueurId(idJ)
            objJ.setNom(nomJoueur)
            objJ.setPrenom(premonJoueur)
            objJ.setPosition(position)
            objJ.setNombreDeBut(nombreDeBut)
            objJ.setNombreDePassesD(nombreDePassesD)
            objJ.setDistanceParcurue(distanceParcurue)

            eq: int = jDAO.modifierUn(idJ, objJ)

            if eq==0 :
                return "ERROR"

            return "MODIFICATION DE EQ AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_JoueursC.modifierUnJ() ::: {e}')

        return None

    @staticmethod
    def supprimerUnJ(idJ):

        try:

            jDAO = JoueursDAO()

            j: int = jDAO.supprimerUn(idJ)

            if j==0 :
                return "ERROR"

            return "SUPPRESSION J AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_JoueursC.supprimerUnJ() ::: {e}')

        return None
    
    @staticmethod
    def search_Joueurs_by_name(keyword) -> list[Joueurs]|str:
        """
        Rechercher des joueurs par nom.
        @param keyword: Mot-clé de recherche.
       
        """
        try:

            jouDAO = JoueursDAO()

            listJo: list[model.JoueursM.Joueurs] = jouDAO.searchPleinText(keyword)

            if listJo == None:
                return "ERROR"

            return listJo

        except Exception as e:

            print(f"Erreur_JoeuursC.search_Joueurs_by_name() ::: {e}")

        return None