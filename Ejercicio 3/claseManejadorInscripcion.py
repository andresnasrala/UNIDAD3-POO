import numpy as array
from inscripcion import Inscripcion

class manejadorInscripcion:
    __cantidad = 0
    __dimension = 0 
    __incremento = 5

    def __init__(self, dimension, incremento = 5) -> None:
            self.__insc = array.empty (dimension, dtype=Inscripcion)
            self.__cantidad = 0
            self.__dimension = dimension

    def agregarInscripcion (self, i):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__insc.resize(self.__dimension, refcheck=False)
        self.__insc[self.__cantidad] = i
        self.__cantidad += 1

    def nuevaInscripcion(self, persona,fecha,taller,pago=False):
        Inscripto= Inscripcion (fecha, persona, taller, pago)
        self.agregarInscripcion (Inscripcion)
        return Inscripcion

    def verificarInscripcto(self, dni):
        valorRetorno=None
        bandera=False
        indice=0
        while (indice < len(self.__insc) and not bandera):
            p = self.__insc[indice].getPersona()
            if (dni == p.getDni()):
                valorRetorno = self.__insc[indice]
                bandera = True
            else:
                indice+=1
        return valorRetorno

    def consultarInscripcion(self, dni):
        i = self.verificarInscripcto(dni)
        if i != None:
            t = i.getTaller()
            print (f'dni: {dni} esta inscripto en el taller: {t.getNombreTaller()}, adeuda: {t.getMonto()}')
        else: print ('La persona no está inscripta')

    def registrarPago (self, dni):
        i = self.verificarInscripcto(dni)
        if i != None:
            i.setPago()
            print ('se realizó el pago')
            print (i.getPago())
        else: print ('La persona no está inscripta')