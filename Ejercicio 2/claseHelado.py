class Helado(): 
    limite_sabores = 4 
    __gramos : float
    __precio : float 
    __sabores : list 

    def __init__(self,gramos,precio): 
        self.__gramos = gramos 
        self.__precio = precio
        self.__sabores =[]
    
    def Agregarsabor(self,sabor): 
        
        if len(self.__sabores)<self.limite_sabores: 
         self.__sabores.append(sabor)

        else: 
           print("Limite Alcanzado ") 

    def getDiccionario(self):
       dicciSaborPeso = {}
       pesoSabor =self.__gramos/len(self.__sabores)
       for i in range(len(self.__sabores)):
          if self.__sabores[i].getNombre() in dicciSaborPeso:
             dicciSaborPeso[self.__sabores[i].getNombre()] += pesoSabor
          else:
             dicciSaborPeso[self.__sabores[i].getNombre()] = pesoSabor
       return dicciSaborPeso
      
      


             
    