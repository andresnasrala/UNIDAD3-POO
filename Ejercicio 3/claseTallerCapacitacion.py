class TallerCapacitacion():
    __idTaller : int 
    __nombre : str 
    __vacantes : int 
    __montoinscripto : int 
    __inscripcion : object
    
    def __init__(self,idTaller,nombre,vacantes,montoinscripto,inscripcion=None)->None:
        self.__idTaller = idTaller
        self.__nombre = nombre 
        self.__vacantes = vacantes 
        self.__montoinscripto = montoinscripto
        self.__inscripcion = inscripcion


    def getDatosTaller(self): 
        return self.__idTaller + " "+self.__nombre+ " vacantes:  "+self.__vacantes +" Monto de Inscripción "+self.__montoinscripto
    
    def setAgregarInscripcion(self,inscripcion): 
        self.__inscripcion = inscripcion
    
    def getNombreTaller(self): 
        return self.__nombre
    
    def getIdTaller(self): 
        return self.__idTaller
    
    def setActualizarVacante(self): 
        self.__vacantes-=1
    
    def getVacante(self): 
        return self.__vacantes

    def getMonto(self): 
        return self.__montoinscripto
    
    def getInscripcion(self): 
        return self.__inscripcion