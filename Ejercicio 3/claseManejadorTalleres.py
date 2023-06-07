import os
import numpy as array
import csv
from claseTallerCapacitacion import TallerCapacitacion 
from datetime import datetime

class ManejadorTalleres:
    __cantidad = 0
    __dimension = 0 
    __incremento = 5

    def __init__(self, dimension, incremento = 5) -> None:
            self.__arreglo_talleres = array.empty (dimension, dtype=TallerCapacitacion)
            self.__cantidad = 0
            self.__dimension = dimension
    
    def AgregarTaller(self,objeto_taller): 
        
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo_talleres.resize(self.__dimension, refcheck=False)
        self.__arreglo_talleres[self.__cantidad] = objeto_taller
        self.__cantidad += 1

    def cargaTalleres(self): 
                    
        archivo=open(os.getcwd()+'/Assets/Talleres.csv','r')
        reader = csv.reader(archivo,delimiter=';')
        i=int(0)

        archivo.__next__()
        for fila in reader: 
            objeto_taller=TallerCapacitacion(fila[0],fila[1],fila[2],fila[3])
            self.AgregarTaller(objeto_taller)
        
        archivo.close()

    def mostrarTalleres(self):

        i=int(0)
        for i in range(len(self.__taller)):
             print(self.__arreglo_talleres[i].getDatosTaller())

    def BuscarId (self, i):
        return self.__arreglo_talleres[i]

    def darDeAlta(self,ManejadorInscripciones,ManejadorPersonas): 
        nombre = input ('Ingrese nombre de la persona: ')
        direccion = input ('Ingrese direcion: ')
        dni = input ('Ingrese DNI de la persona: ')
        print ('Elija el taller a inscribir: ')
        self.mostrarTalleres()
        i = int (input ('Ingrese id del taller elegido: '))
        busqueda_porId = self.BuscarId(i-1)

        if busqueda_porId.getVacante() > 0:
            Persona = ManejadorPersonas.registrarPersona(nombre, direccion,dni,busqueda_porId)
            inscripcion = ManejadorInscripciones.nuevaInscripcion(Persona, datetime.now().date(), busqueda_porId)
            busqueda_porId.AgregarInscripcion(inscripcion)
            print ('Persona inscripta con exito!')
            busqueda_porId.actualizarVacante()
            
        else: 
            print ('Error, no hay vacantes para el taller. Vuelva a intentarlo')
            os.system('pause')
            self.darAlta(ManejadorInscripciones,ManejadorPersonas)


    def getTalleres(self):
        return self.__arreglo_talleres

                