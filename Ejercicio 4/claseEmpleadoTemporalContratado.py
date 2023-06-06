from claseEmpleadoTemporal import EmpleadoTemporal

class EmpleadoContratado(EmpleadoTemporal):

    __cantidad_horas : float 
    __valor_hora : float 

    def __init__(self,dni,nombre,direccion,telefono,fecha_inicio,fecha_fin,cantidad_horas,valor_hora): 
        
        super().__init__(dni,nombre,direccion,telefono,fecha_inicio,fecha_fin)
        self.__cantidad_horas = cantidad_horas 
        self.__valor_hora = valor_hora 