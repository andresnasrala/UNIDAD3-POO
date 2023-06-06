from claseEmpleadoPlanta import EmpleadoPlanta
from claseEmpleadoTemporalContratado import EmpleadoContratado
from claseEmpleadoTemporalExterno import EmpleadoExterno
from claseEmpleado import Empleado
import numpy as np 
import os 
import csv
class ManejadorEmpleado(): 
    __contratados : np 
    __planta : np 
    __externo : np 
    def __init__(self,dimension_contratados,dimension_planta,dimensión_externo):

        self.__contratados=np.empty(dimension_contratados,dtype=EmpleadoContratado)
        self.__planta = np.empty(dimension_planta,dtype=EmpleadoPlanta)
        self.__externo = np.empty(dimensión_externo,dtype=EmpleadoExterno)
    
    def cargarEmpleados(self): 

#-----------------------------------------------------------------------------------------------------------------------------------------

        archivo_contratados = open(os.getcwd()+'/Assets/contratados.csv')
        reader_contratados = csv.reader(archivo_contratados,delimiter=';')

        i = int(0)
        archivo_contratados.__next__()


        for fila in reader_contratados:

            empleado_contratado=EmpleadoContratado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])
            self.__contratados[i]=empleado_contratado

            i+=1
        
        archivo_contratados.close()

#-----------------------------------------------------------------------------------------------------------------------------------------------

        archivo_externos =open(os.getcwd()+'/Assets/externos.csv','r')
        reader_externos=csv.reader(archivo_externos,delimiter=';')

        i = int(0)
        archivo_externos.__next__()
        for fila in reader_externos:

            empleado_externo=EmpleadoExterno(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9])
            self.__externo[i]=empleado_externo
            i+=1

        archivo_externos.close()





        archivo_planta = open(os.getcwd()+'/Assets/planta.csv','r')
        reader_planta = csv.reader(archivo_planta,delimiter=';')

#-------------------------------------------------------------------------------------------------------------------------------

        i=int(0)
        archivo_planta.__next__()
        for fila in reader_planta:

            empleado_planta=EmpleadoPlanta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.__planta[i]=empleado_planta
            i+=1
        archivo_planta.close()


        
if __name__=='__main__': 

    manager = ManejadorEmpleado(4,4,4)
    manager.cargarEmpleados()
