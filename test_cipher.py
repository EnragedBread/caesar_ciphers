import cipher

def test_encode_a_single_word():
    assert cipher.encode('braeden', 3) == 'eudhghq'

def test_decode_a_single_word():
    assert cipher.decode('eudhghq', 3)

def test_encode_a_single_wrapping_word():
    assert cipher.encode('zoo', 3) == 'crr'

def test_encode_a_single_wrapping_word():
    assert cipher.encode('zoo', 64) == 'laa'

def test_encode_a_phrase():
    assert cipher.encode('hello world!', 3) == 'khoor zruog!'