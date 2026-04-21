"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3

# aca lo hice a mano y despues busque lo de mark.parametrize y se ve q es más sencillo de escribir
# nos quedamos con las dos versiones porq hubo un progreso
# def test_add_suma_negativos():
#     """Ejemplo: -11 + -2 debe dar -13."""
#     assert add(-11, -2) == -13

# def test_add_suma_cero_y_positivo():
#     """Ejemplo: 0 + 2 debe dar 2."""
#     assert add(0, 2) == 2

# def test_add_suma_decimales():
#     """Ejemplo: 0 + 2 debe dar 2."""
#     assert add(0.1, 2.3) == 2.4

@pytest.mark.parametrize("a, b, expected", [
    (-1, -2, -3),                                                                                  
    (5,  0,  5),
    (1.5, 2.5, 4.0),                                                                               
])                                                                                                 
def test_add_casos(a, b, expected):
    assert add(a, b) == expected   


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Sumar dos números negativos
#   - Sumar un número positivo y uno negativo
#   - Sumar con cero
#   - Sumar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
#
# Ejemplo de test parametrizado:
#
# @pytest.mark.parametrize("a,b,expected", [
#     (..., ..., ...),
#     (..., ..., ...),
# ])
# def test_add_parametrizado(a, b, expected):
#     assert add(a, b) == expected
