import check50
import re

@check50.check()
def exists():
    """sphere.py exists"""
    check50.exists("sphere.py")

@check50.check(exists)
def test1():
    """input of 1 yields output of 4.188790204"""
    output = check50.run("python3 sphere.py").stdin("1").stdout("4.188790204").exit()

@check50.check(exists)
def test14():
    """input of 15 yields output of 14137.1669385"""
    output = check50.run("python3 sphere.py").stdin("15").stdout("14137.1669385").exit()
@check50.check(exists)

def test50():
    """input of a hidden value yieldsthe correct output"""
    output = check50.run("python3 sphere.py").stdin("25").stdout("65449.8469375").exit()
