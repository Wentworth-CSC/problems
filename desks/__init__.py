import check50
from re import escape


@check50.check()
def exists():
    """desks.py exists"""
    check50.exists("desks.py")

@check50.check(exists)
def test_one():
    """desks accepts 20, 21, 22"""
    check50.run("python3 coke.py").stdin("20").stdin("21").stdin("22").stdout("32").exit()

@check50.check(exists)
def test_two():
    """desks accepts 1, 1, 1"""
    check50.run("python3 coke.py").stdin("1").stdin("1").stdin("1").stdout("3").exit()

@check50.check(exists)
def test_three():
    """desks accepts 26, 20, 16"""
    check50.run("python3 coke.py").stdin("26", prompt=True).stdin("20", prompt=True).stdin("16", prompt=True).stdout("31").exit()

@check50.check(exists)
def test_four():
    """desks accepts 25, 21, 23"""
    check50.run("python3 coke.py").stdin("25", prompt=True).stdin("21", prompt=True).stdin("23", prompt=True).stdout("26").exit()

@check50.check(exists)
def test_five():
    """desks accepts 17, 19, 18"""
    check50.run("python3 coke.py").stdin("17", prompt=True).stdin("19", prompt=True).stdin("18", prompt=True).stdout("28").exit()


