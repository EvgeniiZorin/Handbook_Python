import calc

def test_normal_case():
    assert calc.add(5,4) == 9, "incorrect sum!"

def test_another_case():
    assert calc.add(1,1) == 2, "incorrect sum!"
