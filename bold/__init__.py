import check50
import check50.c

@check50.check()
def exists():
    """bold.py exists"""
    check50.exists("bold.py")

@check50.check(exists)
def emma():
    """responds to a name Bob"""
    check50.run("python hello.py").stdin("Bob").stdout("*Bob*").exit()

@check50.check(exists)
def rodrigo():
    """responds to a colour red"""
    check50.run("python hello.py").stdin("red").stdout("*red*").exit()

@check50.check(exists)
def rodrigo():
    """responds to a sentence \"Welcome to Wentworth\""""
    check50.run("python hello.py").stdin("Welcome to Wentworth").stdout("*Welcome*to*Wentworth*").exit()

@check50.check(exists)
def rodrigo():
    """responds to an unknown test"""
    check50.run("python hello.py").stdin("42 Green Flies! How awful!").stdout("*42*Green*Flies!*How*awful!*").exit()
