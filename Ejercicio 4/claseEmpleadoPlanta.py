from claseEmpleado import Empleado

class EmpleadoPlanta(Empleado): 

    __sueldo_basico : float 
    __antiguedad : str 

    def __init__(self,dni,nombre,direccion,telefono,sueldo_basico,antiguedad): 
        
        super().__init__(dni,nombre,direccion,telefono)
        self.__sueldo_basico = sueldo_basico 
        self.__antiguedad = antiguedad 
