from employee import Employee

employee = Employee('Olexandr', 'Kozachenko', 20)


def test_email():
    assert employee.email == 'Olexandr.Kozachenko@email.com'


def test_fullname():
    assert employee.fullname == 'Olexandr Kozachenko'


def test_apply_raise():
    assert employee.pay * employee.raise_amt == 21
