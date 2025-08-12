from bank import greeting

def test_hello():
    assert greeting('hello') == '$0'
    assert greeting('Hello') == '$0'
    assert greeting('HeLlO') == '$0'

def test_h():
    assert greeting('hi') == '$20'
    assert greeting('Hi') == '$20'
    assert greeting('Hella') == '$20'

def test_anything_else():
    assert greeting('Yo') == '$100'
    assert greeting('What?') == '$100'
    assert greeting('My man') == '$100'
