class Facultad():
    __codigo : str 
    __nombre : str 
    __direccion : str 
    __localidad : str 
    __telefono : str 
    __Carrera : list

    def __init__(self,codigo,nombre,direccion,localidad,telefono): 
        
        self.__codigo = codigo 
        self.__nombre = nombre 
        self.__direccion = direccion
        self.__localidad = localidad 
        self.__telefono = telefono 
        self.__Carrera = []
        
    def AddCarrera(self,codigo,nombre,fecha_inicio,duracion,titulo):
        from claseCarrera import Carrera
        objeto_carrera=Carrera(codigo,nombre,fecha_inicio,duracion,titulo)
        self.__Carrera.append(objeto_carrera)


    def getCodigo(self): 
        return self.__codigo
    

    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getLocalidad(self):
        return self.__localidad
    
    def getTelefono(self):
        return self.__telefono
    
    def getCarrera(self):
        for i in range(len(self.__Carrera)):
            print(self.__Carrera[i].getCarrera())
            