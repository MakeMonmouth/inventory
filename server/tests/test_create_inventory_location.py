# A dummy function to ensure github actions is working
def inc(x):
    return x + 1

def test_positive():
    assert inc(3) == 4

def test_negative():
    assert inc(3) == 5
