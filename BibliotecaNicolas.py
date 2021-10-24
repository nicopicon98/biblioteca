from datetime import date


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.codigo = []
        self.biblioteca = []
        self.lista_letra = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.count = 0

    def hash_code(self):
        for i in self.lista_letra:
            for j in range(0, 10):
                for k in range(0, 10):
                    for v in range(0, 10):
                        self.codigo.append(f"{i}{j}{k}{v}")
        return self.codigo

    def guardarLibro(self, titulo, autor, anioo_public, genero):
        self.nuevotitulo = titulo
        self.nuevoautor = autor
        self.nuevoanioo_public = anioo_public
        self.nuevogenero = genero
        indexCode = len(self.biblioteca) - 1
        return self.biblioteca.append([self.hash_code()[indexCode+1], self.nuevotitulo, self.nuevoautor, self.nuevoanioo_public, self.nuevogenero])

    def grabar(self):
        archivo = open("archivo.txt", "w")
        for x in self.biblioteca:
            archivo.write("Id: {}".format(x[0]))
            archivo.write("\n")
            archivo.write("Titulo: {}".format(x[1]))
            archivo.write("\n")
            archivo.write("Autor: {}".format(x[2]))
            archivo.write("\n")
            archivo.write("fecha: {}".format(x[3]))
            archivo.write("\n")
            archivo.write("genero: {}".format(x[4]))
            archivo.write("\n")
            archivo.write("-----------------------")
            archivo.write("\n")
        archivo.close()

    def listar(self):
        for x in self.biblioteca:
            yield x

    def buscar(self, parBusq, elem):
      self.parBusq = int(parBusq)
      self.elem = elem
      if(self.parBusq == 1):
        self.checkBusquedaCodigo(self.parBusq, self.elem)
      if(self.parBusq == 2):
         self.checkBusqueda(self.parBusq, self.elem)
      if(self.parBusq == 3):
        self.checkBusqueda(self.parBusq, self.elem)
      if(self.parBusq == 4):
        self.checkBusqueda(self.parBusq, self.elem)
      if(self.parBusq == 5):
        self.checkBusqueda(self.parBusq, self.elem)

    def checkBusqueda(self, parBusq, elem):
      pocision = -1
      cont = 0
      for x in self.biblioteca:
          if not elem.lower() in x[parBusq - 1].lower():
              pocision +=1
          if elem.lower() in x[parBusq - 1].lower():
              pocision +=1
              cont +=1
              if cont > 0:
                #si coincide
                self.mostrarBusqueda(x[0],x[1],x[2],x[3],x[4])
      #si no coincide
      if cont == 0:
        par = self.parametroBusqueda(parBusq)
        print(f"No se encontraron coincidencias para {par} {elem}")

    def parametroBusqueda(self, parBusq):
        if parBusq == 2:
          return "el titulo"
        if parBusq == 3:
          return "el autor"
        if parBusq == 4:
          return "la fecha"
        if parBusq == 5:
          return "el genero"

    def checkBusquedaCodigo(self, parBusq, elem):
      pocision = -1
      cont = 0
      for x in self.biblioteca:
          if not elem.lower() == x[parBusq - 1].lower():
              pocision +=1
          if elem.lower() == x[parBusq - 1].lower():
              pocision +=1
              cont +=1
              break
      if cont == 1:
        x = self.biblioteca[pocision]
        self.mostrarBusqueda(x[0],x[1],x[2],x[3],x[4])
      elif cont == 0:
        print(f"No se encontraron coincidencias para el codigo {elem}")

    def mostrarBusqueda(self, x0, x1, x2, x3, x4):
      print(f"Codigo: {x0}, Titulo: {x1}, Autor: {x2}, Fecha: {x3}, Genero: {x4}")


