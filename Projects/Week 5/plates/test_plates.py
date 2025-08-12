from plates import is_valid

def test_punctuation():
    assert is_valid('H-Ell') == False
    assert is_valid('hi,') == False

def test_two_letters():
    assert is_valid('h1') == False

def test_length():
    assert is_valid('OUTATIME') == False
    assert is_valid('H') == False
    assert is_valid('Valid') == True


def test_number_placement():
    assert is_valid('EXTO88') == True
    assert is_valid('50hello') == False
    assert is_valid('CS50PS') == False


def test_0_placement():
    assert is_valid('CS05') == False
    assert is_valid('Hell01') == False
