class TablaAsignacion:

    def __init__(self):
        self.tabla = ["T","R","W","A","G","M","Y","F","P","D","X","B", \
                      "N","J","Z","S","Q","V","H","L","C","K","E", ]
        
    def get_tabla(self):
        return self.tabla   
    
    def get_letra(self, posicion):
        try:
            return self.tabla[posicion]
        except IndexError:
            return "Esta fuera de rango"
        
    def get_longitud(self):
        return len(self.get_tabla())
    
    def is_letra_permitida(self, letra):
        return letra in self.get_tabla()
    
    def calcular_letra(self, DNI):
        posicion = int(DNI) % self.get_longitud()
        return self.get_letra(posicion)
    
    def __repr__(self) -> str:
        return "\n".join(self.get_tabla())
    
    

if __name__ == "__main__":

    import random

    tabla = TablaAsignacion()

    print("\n## TABLA ##\n")

    print(tabla)

    print("\n## ACCESO POR POSICION ##\n")

    print(tabla.get_letra(0))  
    print(tabla.get_letra(22)) 
    print(tabla.get_letra(30)) 
    print("\n## LETRAS NO PERMITIDAS ##\n")

    letras_no_permitidas = ["I", "Ñ", "O", "U"]
    for letra in letras_no_permitidas:
        print(f"Letra {letra}: {tabla.is_letra_permitida(letra)}")

    casos_test = [  
        "78484464T",
        "72376173A",
        "01817200Q",
        "95882054E",
        "63587725Q",
        "26861694V",
        "21616083Q",
        "26868974Y",
        "40135330P",
        "89044648X",
        "80117501Z",
        "34168723S",
        "76857238R",
        "66714505S",
        "66499420A",
    ]

    test = 15

    for num in range(1, test + 1):
        caso = ""
        for digito in range(1, 9):
            caracter_ascii = random.randrange(48, 57 + 1, 1)
            caso = caso + chr(caracter_ascii)       
        caso = caso + letras_no_permitidas[random.randrange(0, 3 + 1, 1)]
        casos_test = casos_test + [caso]

    print("\n## CASOS TEST ##\n")

    print(casos_test)

    for dni in casos_test:
        if tabla.calcular_letra(dni[:-1]) == dni[-1]:
            print(f"{dni} OK" ) 
        else:
            print(f"{dni} FAIL")