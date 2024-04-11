import pytest
from src.main import CalcTriangulo


@pytest.fixture
def calc() -> CalcTriangulo:
    return CalcTriangulo()


# Triângulo escaleno válido
def test_triangulo_escaleno_valido(calc: CalcTriangulo):
    assert calc.calc(3, 4, 5) == "Escaleno"


# Triângulo isósceles válido
def test_triangulo_isosceles_valido(calc: CalcTriangulo):
    assert calc.calc(5, 5, 3) == "Isósceles"


# Triângulo equilatero válido
def test_triangulo_equilatero_valido(calc: CalcTriangulo):
    assert calc.calc(5, 5, 5) == "Equilátero"


# Pelo menos 3 casos de teste (CTs) para isósceles válido contendo a permutação dos mesmos valores
@pytest.mark.parametrize("a, b, c", [(5, 5, 4), (5, 4, 5), (4, 5, 5)])
def test_triangulo_isosceles_valido_permutacao(calc: CalcTriangulo, a, b, c):
    assert calc.calc(a, b, c) == "Isósceles"


# Um valor zero
def test_um_valor_zero(calc: CalcTriangulo):
    assert calc.calc(0, 3, 5) == "Não é um triângulo válido"


# Um valor negativo
def test_um_valor_negativo(calc: CalcTriangulo):
    assert calc.calc(-3, 4, 5) == "Não é um triângulo válido"


# A soma de 2 lados é igual ao teceiro lado
def test_soma_dois_lados_igual_terceiro(calc: CalcTriangulo):
    assert calc.calc(3, 3, 6) == "Não é um triângulo válido"


# Para o item acima, um CT para cada permutação de valores
@pytest.mark.parametrize("a, b, c", [(2, 2, 4), (2, 4, 2), (4, 2, 2)])
def test_soma_dois_lados_igual_terceiro_permutacao(calc: CalcTriangulo, a, b, c):
    assert calc.calc(a, b, c)


# CT em que a soma de 2 lados é menor que o terceiro lado
def test_soma_dois_lados_menor_terceiro(calc: CalcTriangulo):
    assert calc.calc(1, 2, 4) == "Não é um triângulo válido"


# Para o item acima, um CT para cada permutação de valores
@pytest.mark.parametrize("a, b, c", [(2, 2, 4), (2, 4, 2), (4, 2, 2)])
def test_soma_dois_lados_menor_terceiro_permutacao(calc: CalcTriangulo, a, b, c):
    assert calc.calc(a, b, c) == "Não é um triângulo válido"


# Um CT para os três valores iguais a zero
def test_todos_valores_zero(calc: CalcTriangulo):
    assert calc.calc(0, 0, 0) == "Não é um triângulo válido"
