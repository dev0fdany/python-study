from plates import is_valid

def main():
    test_size()
    test_alphanum()
    test_digit()
    test_alpha()
    test_num()
def test_size():
    assert is_valid("A") == False
    assert is_valid("TOOBIGG") == False

def test_alphanum():
    assert is_valid("CS50") == True
    assert is_valid("PY03") == False

def test_digit():
    assert is_valid("50CS") == False
    assert is_valid("03PY") == False

def test_alpha():
    assert is_valid("Hello") == True
    assert is_valid("Python") == True

def test_num():
    assert is_valid("50") == False
    assert is_valid("3000") == False

if __name__ == "__main__":
    main()