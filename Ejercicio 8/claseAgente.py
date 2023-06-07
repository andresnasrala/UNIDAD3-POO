class Agente:
    __cuil : str 
    __apellido : str 
    __nombre : str 
    __sueldo_basico : float 
    __antiguedad : str 
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo_basico = sueldo_basico
        self.__antiguedad = antiguedad
   
    def getCuil(self):
        return self.__cuil
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getSueldo(self):
        return self.__sueldo_basico
    
    def getAntiguedad(self):
        return self.__antiguedad   
    
    def __str__(self):
        return f"{self.__apellido}, {self.__nombre}"