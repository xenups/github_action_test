def capital_case(x: str):
    return x.capitalize()


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
