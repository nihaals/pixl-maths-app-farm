from pma.classes import _generate_password_id


def test_password_id_text():
    assert _generate_password_id('test'), 'ppeqqQ=='
    assert _generate_password_id('testing'), 'ppeqqZ2loA=='


def test_password_id_number():
    assert _generate_password_id('12345'), 'Y2RqaWk='
    assert _generate_password_id('09876543210'), 'YmtvbGpsbWVoamA='


def test_password_id_alphanum():
    assert _generate_password_id('test1234'), 'ppeqqWVpbGY='
    assert _generate_password_id('1234test'), 'Y2RqaaicrKY='
    assert _generate_password_id('1234test1234'), 'Y2RqaaicrKZna2Nk'
    assert _generate_password_id('test1234test'), 'ppeqqWVpbGaqnqOk'
    assert _generate_password_id('1t2e3s4t'), 'Y6ZpmmeqbaY='


def test_password_id_chars():
    assert _generate_password_id('1+2=3'), 'Y2R0aA=='
