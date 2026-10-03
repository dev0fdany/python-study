from twttr import twttr
def main():
    test_noshort()
    test_short()
def test_noshort():
    assert twttr("cry") == "cry"
    assert twttr("gym") == "gym"
    assert twttr("fly") == "fly"


def test_short():
    assert twttr("twitter") == "twttr"
    assert twttr("cow") == "cw"
    assert twttr("please") == "pls"


if __name__ == "__main__":
    main()