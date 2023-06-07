from claseLista import Lista
from claseInvestigador import Investigador
from claseDocenteInvestigador import DocenteInvestigador
from claseDocente import Docente
from clasePersonalApoyo import PersonalApoyo

def crear_agente():
    print("Seleccione el tipo de agente que desea crear:")
    print("1. Docente")
    print("2. Investigador")
    print("3. Docente Investigador")
    print("4. Personal de Apoyo")
    
    tipo_agente = int(input("Ingrese el número correspondiente al tipo de agente: "))
    
    cuil = input("Ingrese el CUIL del agente: ")
    nombre = input("Ingrese el nombre del agente: ")
    apellido = input("Ingrese el apellido del agente: ")
    sueldo_basico = float(input("Ingrese el sueldo básico del agente: "))
    antiguedad = int(input("Ingrese la antigüedad del agente: "))

    if tipo_agente == 1:
        carrera = input("Ingrese la carrera del docente: ")
        cargo = input("Ingrese el cargo del docente: ")
        catedra = input("Ingrese la cátedra del docente: ")
        docente = Docente(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
        return docente
    elif tipo_agente == 2:
        area_investigacion = input("Ingrese el área de investigación: ")
        tipo_investigacion = input("Ingrese el tipo de investigación: ")
        investigador = Investigador(cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
        return investigador
    elif tipo_agente == 3:
        carrera = input("Ingrese la carrera del docente investigador: ")
        cargo = input("Ingrese el cargo del docente investigador: ")
        catedra = input("Ingrese la cátedra del docente investigador: ")
        area_investigacion = input("Ingrese el área de investigación: ")
        tipo_investigacion = input("Ingrese el tipo de investigación: ")
        categoria_incentivos = input("Ingrese la categoría en el programa de incentivos de investigación: ")
        importe_extra = float(input("Ingrese el importe extra por docencia e investigación: "))
        docente_investigador = DocenteInvestigador(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria_incentivos, importe_extra)
        return docente_investigador
    elif tipo_agente == 4:
        categoria = input("Ingrese la categoría del personal de apoyo: ")
        personal_apoyo = PersonalApoyo(cuil, apellido, nombre, sueldo_basico, antiguedad, categoria)
        return personal_apoyo
    else:
        print("Opción no válida.")
        return None

def menu(lista_agentes: Lista):
    while True:
        print("1. Insertar a agentes a la colección")
        print("2. Agregar agentes a la colección")
        print("3. Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición")
        print("4. Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.")
        print("5. Dada un área de investigación, contar la cantidad de agentes que son docente_investigador, y la cantidad de investigadores que trabajen en ese área.")
        print("6. Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.")
        print("7. Almacenar los datos de todos los agentes en el archivo personal.json")
        print("8. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            agente = crear_agente()
            posicion = int(input("Ingrese la posición en la que desea insertar el agente: "))
            lista_agentes.agregar_agente_a_posicion(posicion, agente)
            print(f"Agente {agente.getNombre()} {agente.getApellido()} insertado en la posición {posicion}.")
        elif opcion == 2:
            agente = crear_agente()
            lista_agentes.agregar_agente(agente)
            print(f"Agente {agente.getNombre()} {agente.getApellido()} agregado a la colección.")
        elif opcion == 3:
            posicion = int(input("Ingrese la posición: "))
            agente = lista_agentes.mostrar_agente_por_posicion(posicion)
            print(agente.getApellido(), agente.getNombre(), agente.getCargo(), agente.getCatedra())
        elif opcion == 4:
            area_investigacion = input("Ingrese el área de investigación: ")
            docentes_investigadores = lista_agentes.generar_listado_docentes_investigadores_por_area(area_investigacion)
            for docente_investigador in docentes_investigadores:
                print(docente_investigador.getApellido(), docente_investigador.getNombre(), docente_investigador.getCargo(), docente_investigador.getCatedra())
        elif opcion == 5:
            categoria_investigacion = input("Ingrese la categoría de investigación: ")
            agentes_por_categoria = lista_agentes.generar_listado_agentes_por_categoria(categoria_investigacion)
            for agente in agentes_por_categoria:
                print(agente.getApellido(), agente.getNombre(), agente.getCargo(), agente.getCatedra())
        elif opcion == 6:
            listado = lista_agentes.recorrer_lista_e_generar_listado()
            for nombre, apellido, cargo, cátedra, sueldo in listado:
                print(f"{nombre} {apellido} - Cargo: {cargo} - Cátedra: {cátedra} - Sueldo: {sueldo}")
        elif opcion == 7:
            lista_agentes.almacenar_agentes_en_archivo()
        elif opcion == 8:
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    lista_agentes = Lista()
    menu(lista_agentes)