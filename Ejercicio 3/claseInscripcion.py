class Inscripcion(): 
    __fechaInscripcion : str 
    __pago : bool
    __persona : object
    __taller : str 

    def __init__(self,fechaInscripcion,persona,taller,pago=False)->None: 
        self.__fechaInscripcion = fechaInscripcion
        self.__pago = pago
        self.__persona = persona 
        self.__taller = taller 

    def getFecha (self):
        return self.__fechaInscripcion

    def getPago (self):
        return self.__pago
    
    def setPago (self):
        self.__pago = True

    def getPersona (self):
        return self.__persona

    def getTaller (self):
        return self.__taller

