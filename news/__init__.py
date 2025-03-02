import check50
import check50.c

@check50.check()
def exists():
    """news.py exists"""
    check50.exists("news.py")

@check50.check(exists)
def OneWord():
    """responds to the word \"hello\""""
    check50.run("python hello.py").stdin("hello").stdout("Hello").exit()

@check50.check(exists)
def OneCapWord():
    """responds to the word \"HELLO\""""
    check50.run("python hello.py").stdin("HELLO").stdout("Hello").exit()

@check50.check(exists)
def Sentence():
    """responds to \"Welcome to Wentworth\""""
    check50.run("python hello.py").stdin("Welcome to Wentworth").stdout("Welcome To Wentworth").exit()

@check50.check(exists)
def Sentence():
    """responds to a hidden case"""
    check50.run("python hello.py").stdin("this IS a TEST of ThE pRoGraMmE 42!").stdout("This Is A Test Of The Programme 42!").exit()
