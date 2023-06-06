from claseCarrera import Carrera 
from claseFacultad import Facultad
import csv  
import os 
class ManejaFacultades():
    __lista = []


    def __init__(self):
        self.__lista = []


    def Carga(self):
        try: 
            archivo = open(os.getcwd()+'/Assets/Facultades.csv','r',encoding='utf-8')
            reader = csv.reader(archivo,delimiter=',')
            i = int(0)
            codigo_facultad=None

            for fila in reader: 
            
               if codigo_facultad!=fila[0]: 
                objeto_facultad = Facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
                self.__lista.append(objeto_facultad)
               if codigo_facultad==fila[0]: 
                   objeto_facultad.AddCarrera(fila[1].fila[2],fila[3],fila[4])


        except Exception as error:
            print("Error al cargar el archivo:", str(error))

    def mostrar(self):


        for i in range (len(self.__lista)):

            print(self.__lista[i].getNombre())
            print(self.__lista[i].getCarrera())



if __name__=='__main__':

    manager=ManejaFacultades()
    manager.Carga()
    manager.mostrar()

