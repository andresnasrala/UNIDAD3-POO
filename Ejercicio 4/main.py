from claseManejadorEmpleado import ManejadorEmpleado
if __name__=='__main__': 

    empleados_contratados=int(input("Ingrese la cantidad de empleados contratados: "))
    empleados_planta=int(input("Ingrese la cantidad de empleados de planta: "))
    empleados_externos=int(input("Ingrese la cantidad de empleados externos: "))
    manager = ManejadorEmpleado(empleados_contratados,empleados_planta,empleados_externos)
    manager.cargarEmpleados()