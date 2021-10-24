from BibliotecaNicolas import Biblioteca

def agregarLibro():
    titulo = input("Ingrese el titulo: ")
    autor = input("Ingrese el autor: ")
    fecha = input("Ingrese la fecha: ")
    genero = input("Ingrese el genero:  ")
    newArray = [titulo, autor, fecha, genero]
    return newArray


def userInteraction():
    # Instancia
    library1 = Biblioteca("Biblioteca UTS")

    # Default Books
    sS = ["Harry Potter and the sorcere's stone",
          "J.K Rowling", "26-06-1997", "Fantasy Fiction"]
    cS = ["Harry Potter and the chamber of secrets",
          "J.K Rowling", "02-07-1998", "Fantasy Fiction"]
    pA = ["Harry Potter and prisoner of Azkaban",
          "J.K Rowling", "08-07-1999", "Fantasy Fiction"]
    gF = ["Harry Potter and the goblet of fire",
          "J.K Rowling", "08-07-2000", "Fantasy Fiction"]
    oF = ["Harry Potter and the order of the phoenix",
          "J.K Rowling", "21-06-2003", "Fantasy Fiction"]
    hP = ["Harry Potter and the half-blood prince",
          "J.K Rowling", "16-07-2005", "Fantasy Fiction"]
    dH = ["Harry Potter and the deathly hallows",
          "J.K Rowling", "21-07-2007", "Fantasy Fiction"]
    # Inserting Books
    library1.guardarLibro(sS[0], sS[1], sS[2], sS[3])
    library1.guardarLibro(cS[0], cS[1], cS[2], cS[3])
    library1.guardarLibro(pA[0], pA[1], pA[2], pA[3])
    library1.guardarLibro(gF[0], gF[1], gF[2], gF[3])
    library1.guardarLibro(oF[0], oF[1], oF[2], oF[3])
    library1.guardarLibro(hP[0], hP[1], hP[2], hP[3])
    library1.guardarLibro(dH[0], dH[1], dH[2], dH[3])

    # Interaction
    while True:
        print("""
           1) Adicionar
           2) Mostrar
           3) Guardar
           4) Buscar
           5) Salir
           """)
        opc = input("-Seleccione una opción:")
        if opc == "1":
            nuevoLibro = agregarLibro()
            library1.guardarLibro(nuevoLibro[0], nuevoLibro[1], nuevoLibro[2], nuevoLibro[3])
        elif opc == "2":
            result = library1.listar()
            for item in result:
                print(f"Codigo: {item[0]}, Titulo: {item[1]}, Autor: {item[2]}, Fecha: {item[3]}, Genero: {item[4]}")
        elif opc == "3":
            library1.grabar()
        elif opc == "4":
          while True:
            print("""
                  1) Codigo
                  2) Titulo
                  3) Autor
                  4) Año de publicacion
                  5) Genero
                  6) Volver al menu anterior
                  """)
            opc1 = input("Que parametro de busqueda desea?")
            if opc1 == "1":
              elem = input("Ingrese el codigo: ")
              library1.buscar(opc1,elem)
            if opc1 == "2":
              elem = input("Ingrese el titulo: ")
              library1.buscar(opc1,elem)
            if opc1 == "3":
              elem = input("Ingrese el autor: ")
              library1.buscar(opc1,elem)
            if opc1 == "4":
              elem = input("Ingrese el año de publicacion(dd-mm-aaaa): ")
              library1.buscar(opc1,elem)
            if opc1 == "5":
              elem = input("Ingrese el genero: ")
              library1.buscar(opc1,elem)
            if opc1 == "6":
              break

        elif opc == "5":
            break


userInteraction()
