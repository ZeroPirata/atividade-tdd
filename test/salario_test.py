import pytest
from src.main import Funcionario, CalcularSalario


@pytest.fixture
def calc() -> CalcularSalario:
    return CalcularSalario()


def test_desenvolvedor_com_salario_maior_ou_igual_3000(calc: CalcularSalario):
    funcionario = Funcionario(
        "Gabriel Souza", "gabriel@example.com", "DESENVOLVEDOR", 3500
    )
    assert calc.calcular_salario(funcionario) == 2800


def test_desenvolvedor_com_salario_menor_que_3000(calc: CalcularSalario):
    funcionario = Funcionario("Maria", "maria@example.com", "DESENVOLVEDOR", 2500)
    assert calc.calcular_salario(funcionario) == 2250


def test_dba_com_salario_maior_ou_igual_2000(calc: CalcularSalario):
    funcionario = Funcionario("Lucas", "lucas@example.com", "DBA", 2500)
    assert calc.calcular_salario(funcionario) == 1875


def test_dba_com_salario_menor_que_2000(calc: CalcularSalario):
    funcionario = Funcionario("Rodolfo", "rodolfo@example.com", "DBA", 1500)
    assert calc.calcular_salario(funcionario) == 1275


def test_testador_com_salario_maior_ou_igual_2000(calc: CalcularSalario):
    funcionario = Funcionario("Pedro", "pedro@example.com", "TESTADOR", 2500)
    assert calc.calcular_salario(funcionario) == 1875


def test_testador_com_salario_menor_que_2000(calc: CalcularSalario):
    funcionario = Funcionario("Mara", "mara@example.com", "TESTADOR", 1500)
    assert calc.calcular_salario(funcionario) == 1275


def test_gerente_com_salario_maior_ou_igual_5000(calc: CalcularSalario):
    funcionario = Funcionario("Godofredo", "godofredo@example.com", "GERENTE", 6000)
    assert calc.calcular_salario(funcionario) == 4200


def test_gerente_com_salario_menor_que_5000(calc: CalcularSalario):
    funcionario = Funcionario("Jeremias", "jeremias@example.com", "GERENTE", 4000)
    assert calc.calcular_salario(funcionario) == 3200
