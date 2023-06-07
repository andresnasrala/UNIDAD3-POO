class Persona():
    __nombre : str 
    __direccion : str 
    __dni : str 

    def __init__(self,nombre,direccion,dni):
        self.__nombre = nombre 
        self.__direccion = direccion 
        self.__dni = dni 

    def getNombre(self): 
        self.__nombre 

    def getDireccion(self): 
        self.__direccion

    def getDNI(self):
        self.__dni 

    def getPersona(self): 
        return "Nombre: "+self.__nombre+" "+"DNI: "+self.__dni+ "Direccion: "+self.__direccion
