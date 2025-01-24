import pytest
from src.tabla_asignacion import TablaAsignacion
from src.dni import Dni

def test_letra_valida(dni, esperado):
    dni_obj = Dni(dni)
    assert dni_obj.check_letra() == esperado


def test_letra_invalida(dni, esperado):
    dni_obj = Dni(dni)
    assert dni_obj.check_letra() == esperado


def test_calculo_letra(dni_sin_letra, letra_esperada):
    dni_obj = Dni(dni_sin_letra + "X")  
    assert dni_obj.obtener_letra() == letra_esperada


def test_longitud_dni(dni, longitud_correcta):
    dni_obj = Dni(dni)
    assert dni_obj.check_longitud() == longitud_correcta


def test_numero_valido(dni, es_valido):
    dni_obj = Dni(dni)
    assert dni_obj.check_numero() == es_valido
