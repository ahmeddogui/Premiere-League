class Managers:

    def __init__(self, __manager_id, __nom_manager, __prenom_manager, __equipe, __poste_de_manager):
        self.__manager_id = __manager_id,
        self.__nom_manager = __nom_manager
        self.__prenom_manager = __prenom_manager,
        self.__equipe = __equipe,
        self.__poste_de_manager = __poste_de_manager

    
    def setManagerId(self, manager_id) -> None:
        self.__manager_id = manager_id
    def getManagerId(self) -> int:
        return self.__manager_id    
    
    def setNomManager(self, nom_manager) -> None:
        self.__nom_manager = nom_manager
    def getNomManager(self,nom_manager) -> str:
        return self.__nom_manager
    
    def setPrenomManager(self, prenom_manager) -> None:
        self.__prenom_manager = prenom_manager
    def getPrenomManager(self) -> str:
        return self.__prenom_manager
    
    def setEquipe(self, equipe) -> None:
        self.__equipe = equipe
    def getEquipe(self) -> str:
        return self.__equipe
    
    def setPosteManager(self, poste_de_manager) -> None:
        self.__poste_de_manager = poste_de_manager
    def getPosteManager(self) -> str:
        return self.__poste_de_manager