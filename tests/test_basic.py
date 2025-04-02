from clearscale import how_much_bigger

def test_how_much_bigger():
    assert how_much_bigger("40ms", "100ns") == "400000x"
    assert how_much_bigger("1s", "1ms") == "1000x"
    assert how_much_bigger("1ms", "1ms") == "1x"
    assert how_much_bigger("0s", "1s") == "0x"
