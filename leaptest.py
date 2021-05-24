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


def leap(year):
    #year = input("Input the year you want to check: ")
    print(year)
    if(int(year)% 4 == 0):
        if(int(year)%100 ==0):
            if(int(year)% 400 == 0):
                return 'This is a leap year'
            else: 
                return 'not a leap year'
        else: 
            return 'This is a leap year'
    else: 
        return 'not a leap year'