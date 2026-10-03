from bank import greeting

def main():
    test_hello()
    test_h()
    test_no_h()

def test_hello():
    assert greeting("Hello dude") == "$0"
    assert greeting("Hello bro") == "$0"
    assert greeting("Hello ??") == "$0"
def test_h():
    assert greeting("Hi dude") == "$20"
    assert greeting("Hi bro") == "$20"
    assert greeting("Hi ??") == "$20"
def test_no_h():
    assert greeting("What's up?") == "$100"
    assert greeting("What's good?") == "$100"
    assert greeting("What's the matter?") == "$100"

if __name__ == "__main__":
    main()
