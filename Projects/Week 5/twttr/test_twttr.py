from twttr import shorten

def test_shorten():
    assert shorten('hello') == 'hll'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('aeiou2,') == '2,'
