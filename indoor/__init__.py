import check50


@check50.check()
def exists():
    """indoor.py exists"""
    check50.exists("indoor.py")

@check50.check(exists)
def testhello():
    """input of HELLO yields output of hello"""
    check50.run("python3 indoor.py").stdin("HELLO", prompt=False).stdout("hello").exit()

@check50.check(exists)
def testWCSC():
    """input of WELCOME TO WENTWORTH COMPUTER SCIENCE COLLEGE yields output of welcome to wentworth computer science college"""
    check50.run("python3 indoor.py").stdin("WELCOME TO WENTWORTH COMPUTER SCIENCE COLLEGE", prompt=False).stdout("welcome to wentworth computer science college").exit()

@check50.check(exists)
def testnumber():
    """input of 50 yields output of 50"""
    check50.run("python3 indoor.py").stdin("50", prompt=False).stdout("50").exit()
    
@check50.check(exists)
def testmix():
    """input of Two (2) slabs of Chocolate are YUMMY yields output of 50"""
    check50.run("python3 indoor.py").stdin("Two (2) slabs of Chocolate are YUMMY", prompt=False).stdout("two (2) slabs of chocolate are yummy").exit()
