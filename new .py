from tkinter import N


def hello():
    print("hello")
def goodbye():
    print("bye bye")
def sqared():
    N*N
def test_positive():
    assert sqared(2)==4
def test_negative():
    assert sqared(-3)==9
    def test_0():
        assert sqared(0)==0
