class Sabor(): 
    __idSabor: int 
    __ingredientes : str 
    __nombreSabor: str 

    def __init__(self,idSabor,ingredientes,nombreSabor): 
        self.__idSabor=idSabor
        self.__ingredientes = ingredientes
        self.__nombreSabor = nombreSabor

    def getID(self):
        return self.__idSabor
    
    def getNombre(self): 
        return self.__nombreSabor
    