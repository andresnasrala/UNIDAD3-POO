from claseEmpleado import Empleado

class EmpleadoTemporal(Empleado): 
    __fecha_inicio : str 
    __fecha_fin : str 


    def __init__(self,dni,nombre,direccion,telefono,fecha_inicio,fecha_fin): 
        
        super().__init__(dni,nombre,direccion,telefono)
        self.__fecha_inicio = fecha_inicio 
        self.__fecha_fin = fecha_fin 