from claseSabor import Sabor
import os 
import csv 
class ManejaSabores(): 
    _lista_sabores = []

    def __init__(self): 
        self.__lista_sabores = []

    def cargaSabores(self): 
        
        archivo = open(os.getcwd()+'/Assets/sabores.csv')
        reader = csv.reader(archivo,delimiter=';')

        for fila in reader: 
            
            objeto_sabores=Sabor(int(fila[0]),fila[1],fila[2])
            self.__lista_sabores.append(objeto_sabores)
    
    def getSabor(self,idBuscado): 
        sabor = None
        i = 0 
        N = len(self.__lista_sabores)
        while i < N and self.__lista_sabores[i].getID() != idBuscado:
            i += 1
        
        if i<len(self.__lista_sabores):
            sabor = self.__lista_sabores[i]

        return sabor
        
        
        