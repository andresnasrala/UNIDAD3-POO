from claseEmpleadoTemporal import EmpleadoTemporal

class EmpleadoExterno(EmpleadoTemporal): 
    __tarea : str 
    __monto_viatico : float 
    __costo_obra : float 
    __monto_seguro : float 

    def __init__(self,dni,nombre,direccion,telefono,fecha_inicio,fecha_fin,tarea,monto_viatico,costo_obra,monto_seguro):
         
        super().__init__(dni,nombre,direccion,telefono,fecha_inicio,fecha_fin)
        self.__tarea = tarea 
        self.__monto_viatico = monto_viatico
        self.__costo_obra = costo_obra
        self.__monto_seguro = monto_seguro

