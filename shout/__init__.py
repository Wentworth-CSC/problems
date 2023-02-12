import check50


@check50.check()
def exists():
    """shout.py exists"""
    check50.exists("shout.py")

@check50.check(exists)
def testhello():
    """input of Hello! yields output of HELLO!"""
    check50.run("python3 shout.py").stdin("Hello!", prompt=False).stdout("HELLO!").exit()

@check50.check(exists)
def testWCSC():
    """input of Welcome to Wentworth Computer Science College yields output of WELCOME TO WENTWORTH COMPUTER SCIENCE COLLEGE"""
    check50.run("python3 shout.py").stdin("welcome to Wentworth Computer Science College", prompt=False).stdout("WELCOME TO WENTWORTH COMPUTER SCIENCE COLLEGE").exit()

@check50.check(exists)
def testnumber():
    """input of 50 yields output of 50"""
    check50.run("python3 shout.py").stdin("50", prompt=False).stdout("50").exit()
    
@check50.check(exists)
def testmix():
    """input of Two slabs of Chocolate are YUMMY yields output of TWO SLABS OF CHOCOLATE ARE YUMMY"""
    check50.run("python3 shout.py").stdin("Two slabs of Chocolate are YUMMY", prompt=False).stdout("TWO SLABS OF CHOCOLATE ARE YUMMY").exit()
