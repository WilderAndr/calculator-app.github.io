from app import suma, resta, multiplicacion, division

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 3) == 2

def test_multiplicacion():
    assert multiplicacion(3, 4) == 12

def test_division():
    assert division(10, 2) == 5
    assert division(5, 0) == "Error: División por cero"
