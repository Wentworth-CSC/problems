import check50
import re

@check50.check()
def exists():
    """einstein.py exists"""
    check50.exists("circle.py")

@check50.check(exists)
def test1():
    """input of 1 yields output of 90000000000000000"""
    output = check50.run("python3 circle.py").stdin("1", prompt=False).stdout("3.14159").exit()

@check50.check(exists)
def test14():
    """input of 10 yields output of 314.15927"""
    output = check50.run("python3 circle.py").stdin("10", prompt=False).stdout("314.15927").exit()
  
@check50.check(exists)
def test50():
    """input of 50 yields output of 7853.98163"""
    output = check50.run("python3 circle.py").stdin("50", prompt=False).stdout("7853.98163").exit()
  
@check50.check(exists)
def test27():
    """input of 2.7 yields output of 22.90221"""
    output = check50.run("python3 circle.py").stdin("2.7", prompt=False).stdout("22.90221").exit()
