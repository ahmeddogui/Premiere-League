import sys
sys.path.insert(0, 'C:/Users/ahmed/OneDrive/Bureau/AHMED/PremiereLeague-main')
from dao.EquipesDAO import *
import model
from model import EquipesM

class Equipes:

    @staticmethod
    def visualiserEq():

        try:

            eDAO = EquipesDAO()

            eqs: list[EquipesM.Equipes] = eDAO.trouverTout()

            if eqs==None :
                return "ERROR"

            return eqs

        except Exception as e:
            print(f'Erreur_EquipessC.visualiserEq() ::: {e}')

        return None

    @staticmethod
    def visualiserUnEq(idEQ):

        try:

            eqDAO = EquipesDAO()

            eq: EquipesM.Equipes = eqDAO.trouverUn(idEQ)

            if eq==None :
                return "ERROR"

            return eq

        except Exception as e:
            print(f'Erreur_EquipesC.visualiserUnEq() ::: {e}')

        return None


    @staticmethod
    def ajouterUnEq(equipeID, nomEquipe, manager, joueurs):

        try:

            eqDAO = EquipesDAO()

            objEQ = EquipesM.Equipes()

            objEQ.setEquipeId(equipeID)
            objEQ.setNomDeEquipe(nomEquipe)
            objEQ.setManager(manager)
            objEQ.setJoueurs(joueurs)


            eq: int = eqDAO.insererUn(objEQ)

            if eq==0:
                return "ERROR"

            return "AJOUT Eq AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_EquipesC.ajouterUnEq() ::: {e}')

        return None

    @staticmethod
    def modifierUnEq(equipeID, nomEquipe, manager, joueurs):
        '''
        Modifie un body part.
        @param idBP: ID du body part.
        @param nameBP: Nouveau nom du body part.
        @return: Statut de la modification du body part.
        '''
        try:

            eqDAO = EquipesDAO()
            objEQ = EquipesM.Equipes()

            # objEQ.setEquipeId(equipeID)
            objEQ.setNomDeEquipe(nomEquipe)
            objEQ.setManager(manager)
            objEQ.setJoueurs(joueurs)

            eq: int = eqDAO.modifierUn(equipeID, objEQ)

            if eq==0 :
                return "ERROR"

            return "MODIFICATION DE EQ AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_EquipesC.modifierUnEq() ::: {e}')

        return None

    @staticmethod
    def supprimerUnEq(equipeID):

        try:

            eqDAO = EquipesDAO()

            eq: int = eqDAO.supprimerUn(equipeID)

            if eq==0 :
                return "ERROR"

            return "SUPPRESSION EQ AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_EquipesC.supprimerUnEQ() ::: {e}')

        return None
    
    @staticmethod
    def search_Equipes_by_name(keyword) -> list[Equipes]|str:
        """
        Rechercher des equipes par nom.
        @param keyword: Mot-clé de recherche.
        
        """
        try:

            equDAO = EquipesDAO()

            listEq: list[model.EquipesM.Equipes] = equDAO.searchPleinText(keyword)

            if listEq == None:
                return "ERROR"

            return listEq

        except Exception as e:

            print(f"Erreur_EquipesC.search_Equipes_by_name() ::: {e}")

        return None