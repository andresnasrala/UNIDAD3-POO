from claseManejaHelados import ManejaHelados
from claseManejaSabores import ManejaSabores


if __name__=='__main__': 

    manager_Sabores = ManejaSabores()
    manager_Helados = ManejaHelados()
    
    manager_Sabores.cargaSabores()
    
    gramos =float (input("Ingrese la cantidad de GRAMOS 100gr,150gr,250gr,500gr o 1000gr: "))
    if(gramos==100 or gramos==150 or gramos ==250 or gramos==500 or gramos==1000):
        precio = float(input("Ingrese el PRECIO del helado: "))
        cant_sabores = int(input("Ingrese la CANTIDAD de sabores: "))
        manager_Helados.RegistrarVenta(gramos,precio,cant_sabores,manager_Sabores)

    manager_Helados.ListarTop5Sabores()

