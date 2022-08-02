import check50
import check50.c

@check50.check()
def exists():
    """hello.py exists"""
    check50.exists("hello.py")

@check50.check(exists)
def emma():
    """responds to name Emma"""
    check50.run("python hello.py").stdin("Emma").stdout("Emma").exit()

@check50.check(exists)
def rodrigo():
    """responds to name Rodrigo"""
    check50.run("python hello.py").stdin("Rodrigo").stdout("Rodrigo").exit()
