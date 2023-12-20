import sys
sys.path.insert(0, 'C:/Users/ahmed/OneDrive/Bureau/AHMED/PremiereLeague-main')
from dao import ButsDAO
from model import ButsM

class Buits:

    @staticmethod
    def visualiserButs():
        '''
        Visualise tous les buts.
        @retrun: Liste de buts ou message d'erreur
        '''

        try:

            bDAO = ButsDAO()

            bs: list[ButsM.Buts] = bDAO.trouverTout()

            if bs == None:
                return "ERROR"
            
            return bs
        
        except Exception as e:
            print(f"Erreur_ButsC.visualiserButs() ::: {e}")

        return None
    

    @staticmethod
    def visualiserUnBut(idB):

        try:

            bDAO = ButsDAO()

            b: ButsM.Buts = bDAO.trouverUn(idB)

            if b == None:
                return "ERROR"
            
            return b
        
        except Exception as e:
            print(f"Erreur_ButsC.visualiserUnBut() ::: {e}")

        return None
    
    @staticmethod
    def ajouterUnBut(idB, minuteB, buteurB, passeurB):

        try:

            bDAO = ButsDAO()

            objB = ButsM.Buts()

            objB.setButId(idB)
            objB.setMinute(minuteB)
            objB.setButeur(buteurB)
            objB.setPasseur(passeurB)

            b: int = bDAO.insererUn(objB)

            if b==0:
                return "ERROR"

            return "AJOUT BP AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_ButsC.ajouterUnBut() ::: {e}')

        return None
    

    @staticmethod
    def modifierUnBut(idB, minuteB, buteurB, passeurB):

        try:

            bDAO = ButsDAO()
            objB = ButsM.Buts()

            # objB.setButId(idB)
            objB.setMinute(minuteB)
            objB.setButeur(buteurB)
            objB.setPasseur(passeurB)

            b: int = bDAO.modifierUn(idB, objB)

            if b==0 :
                return "ERROR"

            return "MODIFICATION Dut B AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_ButsC.modifierUnBut() ::: {e}')

        return None
    
    @staticmethod
    def supprimerUnBP(idB):
        '''
        Supprime un body part.
        @param idBP: ID du body part.
        @return: Statut de la suppression du body part.
        '''
        try:

            bDAO = ButsDAO()

            b : int = bDAO.supprimerUn(idB)

            if b==0 :
                return "ERROR"

            return "SUPPRESSION But AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_Buts.supprimerUnBut() ::: {e}')

        return None