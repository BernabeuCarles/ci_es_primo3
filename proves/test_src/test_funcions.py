"""  
Este módulo realiza análisis de datos sobre registros de ventas.  
Incluye funciones para leer datos, procesar estadísticas  
y generar informes.  
""" 

from src.funcions import es_primo

def test_es_primo_numero_primo():
    assert es_primo(2) == True

def test_es_primo_negativo():
    assert es_primo(-10) == False

def test_es_primo_numero_primo_mayor_2():
    assert es_primo(29) == True
    