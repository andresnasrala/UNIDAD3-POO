class Empleado():
    __dni : str 
    __nombre : str 
    __direccion : str 
    __telefono : str 

    def __init__(self,dni,nombre,direccion,telefono): 
        
        self.__dni = dni 
        self.__nombre = nombre 
        self.__direccion = direccion 
        self.__telefono = telefono 
    
    def getNombre(self): 
        return self.__nombre
    
    def getDNI(self): 
        return self.__dni 
    
