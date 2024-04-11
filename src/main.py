# Atividade Um
class CalcTriangulo:
    def __init__(self) -> None:
        pass

    def calc(self, a: int, b: int, c: int) -> str:
        if a <= 0 or b <= 0 or c <= 0:
            return "Não é um triângulo válido"
        elif a + b <= c or a + c <= b or b + c <= a:
            return "Não é um triângulo válido"
        elif a == b == c:
            return "Equilátero"
        elif a == b or a == c or b == c:
            return "Isósceles"
        return "Escaleno"


# Atividade Dois
class Email:
    def __init__(self, email_address):
        self.email_address = email_address


class Person:
    def __init__(self, nome: str, idade: int, emails: list = []):
        self.nome = nome
        self.idade = idade
        self.emails = emails

    @staticmethod
    def __nome_valid(nome: str) -> bool:
        if (
            not nome
            or len(nome.split()) < 2
            or not all(part.isalpha() for part in nome.split())
        ):
            return False
        return True

    @staticmethod
    def __idade_valida(idade: int) -> bool:
        if not (1 <= idade <= 200):
            return False
        return True

    @staticmethod
    def __email_valida(emails) -> bool:
        if not emails or not any(isinstance(email, Email) for email in emails):
            return False
        return True

    def __adicionar_email(self) -> bool:
        for email in self.emails:
            parts = email.email_address.split("@")
            if (
                len(parts) != 2
                or not all(part for part in parts)
                or "." not in parts[1]
            ):
                return False
        return True

    def isValidToInclude(self) -> list:
        if not self.__nome_valid(self.nome):
            return (
                "O nome deve ser composto por ao menos 2 partes e conter apenas letras"
            )

        if not self.__idade_valida(self.idade):
            return "A idade deve estar no intervalo [1, 200]"

        if not self.__email_valida(self.emails):
            return "O objeto Person deve ter pelo menos um objeto da classe Email associado"

        if not self.__adicionar_email():
            return "O nome da classe Email deve estar no formato '_____@____._____"

        return "É Válido"


# Atividade Três
class Funcionario:
    def __init__(self, nome: str, email: str, cargo: str, salario_base: float) -> None:
        self.nome = nome
        self.email = email
        self.cargo = cargo
        self.salario_base = salario_base


class CalcularSalario:
    def __init__(self) -> None:
        pass

    @staticmethod
    def calcular_desconto(
        cargo_salario: float, salario: float, desconto: list
    ) -> float:
        if salario >= cargo_salario:
            return salario * desconto[0]
        return salario * desconto[1]

    def calcular_salario(self, funcionario: Funcionario):
        salario_base = funcionario.salario_base
        if funcionario.cargo == "DESENVOLVEDOR":
            return self.calcular_desconto(3000, salario_base, [0.80, 0.90])
        elif funcionario.cargo == "DBA" or funcionario.cargo == "TESTADOR":
            return self.calcular_desconto(2000, salario_base, [0.75, 0.85])
        elif funcionario.cargo == "GERENTE":
            return self.calcular_desconto(5000, salario_base, [0.70, 0.80])
        else:
            raise ValueError("Cargo inválido")
