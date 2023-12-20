class Equipes:

    def __init__(self, __equipe_id, __nom_de_equipe, __manager, __joueurs):
        self.__equipe_id = __equipe_id,
        self.__nom_de_equipe = __nom_de_equipe,
        self.__manager = __manager,
        self.__joueurs = __joueurs

    def setEquipeId(self, equipe_id) -> None:
        self.__equipe_id = equipe_id

    def getEquipeId(self) -> int:
        return self.__equipe_id
    
    def setNomDeEquipe(self, nom_de_equipe) -> None:
        self.__nom_de_equipe = nom_de_equipe
    
    def getNomDeEquipe(self,nom_de_equipe) -> str:
        return self.__nom_de_equipe
    
    def setManager(self, manager) -> None:
        self.__manager = manager

    def getManager(self) -> str:
        return self.__manager
    
    def setJoueurs(self, joueurs) -> None:
        self.__joueurs = joueurs

    def getJoueurs(self) -> str:
        return self.__joueurs


