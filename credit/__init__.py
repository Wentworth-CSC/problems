import check50

@check50.check()
def exists():
    """credit.py exists."""
    check50.exists("credit.py")

@check50.check(exists)
def test1():
    """identifies <amex card number> as AMEX"""
    check50.run("python3 credit.py").stdin("378282246310005").stdout("AMEX\n").exit()

@check50.check(exists)
def test2():
    """identifies <another amex card number> as AMEX"""
    check50.run("python3 credit.py").stdin("371449635398431").stdout("AMEX\n").exit()

@check50.check(exists)
def test3():
    """identifies <mastercard> as MASTERCARD"""
    check50.run("python3 credit.py").stdin("5555555555554444").stdout("MASTERCARD\n").exit()

@check50.check(exists)
def test4():
    """identifies <another mastercaerd> as MASTERCARD"""
    check50.run("python3 credit.py").stdin("5105105105105100").stdout("MASTERCARD\n").exit()

@check50.check(exists)
def test5():
    """identifies <visa card> as VISA"""
    check50.run("python3 credit.py").stdin("4111111111111111").stdout("VISA\n").exit()

@check50.check(exists)
def test6():
    """identifies <another visa card> as VISA"""
    check50.run("python3 credit.py").stdin("4012888888881881").stdout("VISA\n").exit()

@check50.check(exists)
def test7():
    """identifies <invalid card> as INVALID"""
    check50.run("python3 credit.py").stdin("1234567890").stdout("INVALID\n").exit()
