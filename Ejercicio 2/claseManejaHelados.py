from claseHelado import Helado 

class ManejaHelados(): 
    lista_helados = []

    def __init__(self): 
        self.__lista_helados = []

    def RegistrarVenta(self,gramos,precio,cant_sabores,manager_Sabores): 

        helado = Helado(gramos,precio)

        for i in range(0,cant_sabores):
            
            id=int(input("Ingrese el id del helado: "))
            sabor=manager_Sabores.getSabor(id)

            if sabor==None:
                print("Sabor inexistente.")
            else: 
                helado.Agregarsabor(sabor)
            
        self.__lista_helados.append(helado)
    
    def ListarTop5Sabores(self): 
        print(len(self.__lista_helados))
        diccionario={}
        max=float(0)
        nombre =''
        for helado in self.__lista_helados:
            dicciSaborPeso = helado.getDiccionario()
            for sabor in dicciSaborPeso:
                if sabor in diccionario:
                    diccionario[sabor] += dicciSaborPeso[sabor]
                else:
                    diccionario[sabor] = dicciSaborPeso[sabor]

        for i in range(2):
            for sabor in diccionario:
                if diccionario[sabor]>max: 
                    max = diccionario[sabor]
                    nombre=sabor
            print(nombre)
            del diccionario[nombre]

