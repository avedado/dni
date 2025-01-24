from src.tabla_asignacion import TablaAsignacion

class Dni:

    def __init__(self, cadena = ""):
        self.dni = cadena
        self.numero_sano = False
        self.letra_sana = False
        self.tabla = TablaAsignacion()
    
    def set_dni(self, cadena):
        self.dni = cadena

    def get_dni(self):
        return self.dni   
    
        
    def set_numero_sano(self, valor):
        self.numero_sano = valor

    def get_numero_sano(self):
        return self.numero_sano

    def set_letra_sana(self, valor):
        self.letra_sana = valor

    def get_letra_sana(self):
        return self.letra_sana

    def check_CIF(self):
        return self.check_dni() and self.check_letra()

    def check_dni(self):
        self.set_numero_sano(self.check_longitud() and self.check_numero())
        return self.get_numero_sano()

    def check_letra(self):
        if self.get_numero_sano():
            self.set_letra_sana(
                self.get_parte_alfabetica_dni().isupper()
                and not self.get_parte_alfabetica_dni().isdigit()
                and self.check_letra_valida()
            )
            return self.get_letra_sana()
        else:
            return False

    def obtener_letra(self):
        if self.get_numero_sano():
            return self.tabla.calcular_letra(self.get_parte_numerica_dni())
        else:
            return None

    def check_longitud(self):
        return len(self.get_dni()) == 9

    def check_numero(self):
        return self.dni[:-1].isdigit()

    def check_letra_valida(self):
        if self.get_numero_sano():
            return self.get_parte_alfabetica_dni() == self.obtener_letra()
        else:
            return False

    def get_parte_alfabetica_dni(self):
        return self.dni[-1]

    def get_parte_numerica_dni(self):
        if self.get_numero_sano():
            return self.dni[:-1]
        else:
            return False


if __name__ == "__main__":

    import random

    casosTest = []
    numero_casos = 25

    for dni in range(1, numero_casos + 1):
        caso = ""
        for digito in range(1, 9):
            caracter_ascii = random.randrange(48, 58 + 1, 1)
            caso = caso + chr(caracter_ascii)
        caso = caso + chr(random.randrange(65, 90 + 1, 1))
        casos_test = casos_test + [caso]

    print("\n## CASOS TEST ALEATORIOS ##\n")

    print(casos_test)

    for test_string in casos_test:
        dni = Dni(test_string)
        print(dni.get_dni())
        dni.check_CIF()
    
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

    print("\n #### CASOS OK #### \n")

    for test_string in casos_test:
        dni = Dni(test_string)
        print(dni.get_dni())
        dni.check_CIF()
        