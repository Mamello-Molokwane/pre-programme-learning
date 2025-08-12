from fuel import convert, gauge
import pytest

def test_convert():
    assert convert('3/5') == 60
    assert convert('5/5') == 100
    with pytest.raises(ValueError):
        convert('10/5')
    with pytest.raises(ValueError):
        convert('-5/5')
    with pytest.raises(ZeroDivisionError):
        convert('5/0')
    with pytest.raises(ValueError):
        convert('String')


def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(60) == '60%'
