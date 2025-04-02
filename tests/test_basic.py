from clearscale import how_much_bigger

def test_how_much_bigger():
    assert how_much_bigger("40ms", "100ns") == "400000x"
    assert how_much_bigger("1s", "1ms") == "1000x"
    assert how_much_bigger("1ms", "1ms") == "1x"
    assert how_much_bigger("0s", "1s") == "0x"

def test_data_units():
    assert how_much_bigger("1MB", "1kB") == "1000x"
    assert how_much_bigger("10kB", "10B") == "1000x"
    assert how_much_bigger("1GB", "1MB") == "1000x"

def test_fractional_result():
    assert how_much_bigger("1.2s", "1s") == "1.2x"
    assert how_much_bigger("3ms", "2ms") == "1.5x"
    assert how_much_bigger("1s", "300ms") == "3.33x"
    assert how_much_bigger("1s", "333ms", precision=1) == "3.0x"

def test_physical_units():
    assert how_much_bigger("1km", "1m") == "1000x"
    assert how_much_bigger("1kg", "500g") == "2x"
    assert how_much_bigger("1kWh", "3600J") == "1000x"
    assert how_much_bigger("2MB", "2000kB") == "1x"
