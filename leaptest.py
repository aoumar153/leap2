import unittest 

def test_pal():
    s = 2000
    assert leap(s) == 'This is a leap year'
def test_p():
    s = 20001
    assert leap(s) == 'not a leap year'
def test_p():
    s = '2340'
    assert leap(s) == 'error'
