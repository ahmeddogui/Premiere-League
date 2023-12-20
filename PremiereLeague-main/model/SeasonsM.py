class Seasons:

    def __init__(self, __season_id, __annee):
        self.__season_id = __season_id
        self.__annee = __annee

    def setSeasonId(self, season_id) -> None:
        self.__season_id = season_id
    def getSeasonId(self) -> int:
        return self.__season_id
    
    def setAnnee(self, annee) -> None:
        self.__annee = annee
    def getAnnee(self) -> int:
        return self.__annee