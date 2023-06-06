class Carrera():
    __fecha_inicio ="13/03/2024"
    __codigo : str 
    __nombre : str 
    __duracion : str 
    __titulo : str 



    def __init__(self,codigo,nombre,duracion,titulo):

        self.__codigo = codigo 
        self.__nombre = nombre 
        self.__duracion = duracion 
        self.__titulo = titulo 

    def getCodigo(self):
        return self.__codigo 
    
    def getNombre (self):
        return self.__nombre 
    
    def getFechaInicio(self):
        return self.__fecha_inicio
    
    def getDuracion(self):
        return(self.__duracion)
    
    def getTitulo(self):
        return(self.__titulo)
    
    def getCarrera(self): 
        return self.__codigo +" "+self.__nombre+" "+self.__fecha_inicio+" "+self.__duracion+" "+self.__titulo