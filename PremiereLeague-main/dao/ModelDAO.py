import sys
sys.path.insert(0, 'C:/Users/ahmed/OneDrive/Bureau/AHMED/PremiereLeague-main')
from abc import ABC, abstractmethod
from ConnectionDAO import ConnexionBD

class modeleDAO(ABC):
    connect_objet = ConnexionBD().getConnexion() 

    # insert

    @abstractmethod
    def insererUn(self, objIns) -> int:
        pass

    @abstractmethod
    def insererToutList(self, objIns) -> int:
        pass 

    #select
    @abstractmethod
    def trouverUn(self, cleTrouv) -> int:
        pass

    @abstractmethod
    def trouverTout(self) -> int:
        pass 

    @abstractmethod
    def trouverToutParUn(self, cleTrouv) -> list:
        pass

    @abstractmethod
    def trouverToutParUnLike(self, cleTrouv)->list:
        pass

    #update

    @abstractmethod
    def modifierUn(slef, cleAnc, objModif) -> int:
        pass

    #delete

    @abstractmethod
    def supprimerUn(self, cleSup) -> int:
        pass