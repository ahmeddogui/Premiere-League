class Buts:

    def __init__(self, __but_id, __minute, __buteur, __passeur):
        self.__but_id = __but_id,
        self.__minute = __minute,
        self.__buteur = __buteur,
        self.__passeur = __passeur
    
    def setButId(self, but_id) -> None:
        self.__but_id = but_id
    def getButId(self) -> int:
        return self.__but_id

    def setMinute(self, minute) -> None:
        self.__minute = minute
    def getMinute(self) -> int:
        return self.__minute
    
    def setButeur(self, buteur) -> None:
        self.__buteur = buteur
    def getButeur(self) -> str:
        return self.__buteur
    
    def setPasseur(self, passeur) -> None:
        self.__passeur = passeur
    def getPasseur(self) -> str:
        return self.__passeur