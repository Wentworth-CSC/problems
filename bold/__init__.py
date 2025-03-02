import check50
import check50.c

@check50.check()
def exists():
    """bold.py exists"""
    check50.exists("bold.py")

@check50.check(exists)
def bob():
    """responds to a name Bob"""
    check50.run("python bold.py").stdin("Bob", prompt="flase").stdout("*Bob*").exit()

@check50.check(exists)
def red():
    """responds to a colour red"""
    check50.run("python bold.py").stdin("red", prompt="flase").stdout("*red*").exit()

@check50.check(exists)
def sentence():
    """responds to a sentence \"Welcome to Wentworth\""""
    check50.run("python bold.py").stdin("Welcome to Wentworth", prompt="flase").stdout("*Welcome*to*Wentworth*").exit()

@check50.check(exists)
def hidden():
    """responds to an unknown test"""
    check50.run("python bold.py").stdin("42 Green Flies! How awful!", prompt="flase").stdout("*42*Green*Flies!*How*awful!*").exit()
