from src.main import Person, Email

def test_valid_person():
    person = Person("Gabriel Souza", 23, [Email("gabriel@example.com")])
    assert person.isValidToInclude() == "É Válido"


def test_invalid_name():
    person = Person("GabrielSouza", 22, [Email("gabriel@example.com")])
    assert person.isValidToInclude() == "O nome deve ser composto por ao menos 2 partes e conter apenas letras"


def test_invalid_age():
    person = Person("Gabriel Souza", 999, [Email("gabriel@example.com")])
    assert person.isValidToInclude() == "A idade deve estar no intervalo [1, 200]"


def test_no_email():
    person = Person("Gabriel Souza", 30)
    assert person.isValidToInclude() == "O objeto Person deve ter pelo menos um objeto da classe Email associado"


def test_invalid_email_format():
    person = Person("Gabriel Souza", 30, [Email("email_invalido")])
    assert person.isValidToInclude() == "O nome da classe Email deve estar no formato '_____@____._____"
