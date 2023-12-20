import sys
sys.path.insert(0, 'C:/Users/ahmed/OneDrive/Bureau/AHMED/PremiereLeague-main')
from dao.SeasonsDAO import *
from model import SeasonsM

class Seasons:

    @staticmethod
    def visualiserSeason():

        try:

            seasonDAO = SeasonsDAO()

            seasons: list[SeasonsM.Seasons] = seasonDAO.trouverTout()

            if seasons==None :
                return "ERROR"

            return seasons

        except Exception as e:
            print(f'Erreur_SeasonsC.visualiserSeason() ::: {e}')

        return None

    @staticmethod
    def visualiserUnSeason(idSeason):

        try:

            seasonDAO = SeasonsDAO()

            season: SeasonsM.Seasons = seasonDAO.trouverUn(idSeason)

            if season==None :
                return "ERROR"

            return season

        except Exception as e:
            print(f'Erreur_SeasonC.visualiserUnSeason() ::: {e}')

        return None


    @staticmethod
    def ajouterUnSeason(idSeason, annee):

        try:

            seasonDAO = SeasonsDAO()

            objSeason = SeasonsM.Seasons()

            objSeason.setSeasonId(idSeason)
            objSeason.setAnnee(annee)


            season: int = seasonDAO.insererUn(objSeason)

            if season==0:
                return "ERROR"

            return "AJOUT Season AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_SeasonsC.ajouterUnSeason() ::: {e}')

        return None

    @staticmethod
    def modifierUnSeason(idSeason, annee):

        try:

            seasonDAO = SeasonsDAO()
            objSeason = SeasonsM.Seasons()

            # objJ.setJoueurId(idJ)
            objSeason.setSeasonId(idSeason)
            objSeason.setAnnee(annee)

            season: int = seasonDAO.modifierUn(idSeason, objSeason)

            if season==0 :
                return "ERROR"

            return "MODIFICATION DE Season AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_SeasonC.modifierUnSeason() ::: {e}')

        return None

    @staticmethod
    def supprimerUnJ(idSeason):

        try:

            seasonDAO = SeasonsDAO()

            season: int = seasonDAO.supprimerUn(idSeason)

            if season==0 :
                return "ERROR"

            return "SUPPRESSION Season AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_SeasonsC.supprimerUnSeason() ::: {e}')

        return None