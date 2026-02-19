'''#assert:user defined exception.not testing
import sys
try:
    age=int(input("enter age to check eligible vote:"))
    assert age>=18,"not eligible to vote"
    print("eligible to vote")
except:
    print("error reason:",sys.exc_info()[0])
    print("error reason:",sys.exc_info()[1])'''


def inc(x):
    return x + 1
def test_answer():
    assert inc(3) == 14


def add(a, b):
    return a + b
def test_add():
    assert add(2, 3) == 5
