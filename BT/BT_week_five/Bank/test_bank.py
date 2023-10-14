from Bank import value


def test_value_hello():
    assert value("hello") == 0


def test_value_h():
    assert value("hi") == 20


def test_value_other():
    assert value("welcome") == 100
    assert value("goodbye") == 100


if __name__ == "__main__":
    test_value_hello()
    test_value_h()
    test_value_other()
    print("All tests passed!")
