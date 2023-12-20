class Joueurs:

    def __init__(self, __joueur_id, __nom_joueur, __premon_joueur, __position, __nombre_de_but, __nombre_de_passes_d, __distance_parcurue):
        self.__joueur_id = __joueur_id
        self.__nom_joueur = __nom_joueur
        self.__premon_joueur = __premon_joueur
        self.__position = __position
        self.__nombre_de_but = __nombre_de_but,
        self.__nombre_de_passes_d = __nombre_de_passes_d
        self.__distance_parcurue = __distance_parcurue

    def setJoueurId(self, joueur_id) -> None:
        self.__joueur_id = joueur_id
    def getJoueurId(self) -> int:
        return self.__joueur_id

    def setNom(self, nom_joueur) -> None:
        self.__nom_joueur = nom_joueur
    def getNom(self) -> str:
        return self.__nom_joueur

    def setPrenom(self, premon_joueur) -> None:
        self.__premon_joueur = premon_joueur
    def getPrenom(self) -> str:
        return self.__premon_joueur

    def setPosition(self, position) -> None:
        self.__position = position
    def getPosition(self) -> str:
        return self.__position
    
    def setNombreDeBut(self, nombre_de_but) -> None:
        self.__nombre_de_but = nombre_de_but
    def getNombreDeBut(self) -> int:
        return self.__nombre_de_but
    
    def setNombreDePassesD(self, nombre_de_passes_d) -> None:
        self.__nombre_de_passes_d = nombre_de_passes_d
    def getNombreDePassesD(self) -> int:
        return self.__nombre_de_passes_d
    
    def setDistanceParcurue(self, distance_parcurue) -> None:
        self.__distance_parcurue = distance_parcurue
    def getDistanceParcurue(self) -> int:
        return self.__distance_parcurue
    