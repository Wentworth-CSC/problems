import check50

@check50.check()
def exists():
    """isbn.py exists."""
    check50.exists("isbn.py")

@check50.check(exists)
def test_valid_isbn_1():
    """Validates a valid ISBN: <1>"""
    check50.run("python isbn.py").stdin("1112223339").stdout("YES").exit()

@check50.check(exists)
def test_valid_isbn_2():
    """Validates a valid ISBN: <2>"""
    check50.run("python isbn.py").stdin("1234554321").stdout("YES").exit()
    
@check50.check(exists)
def test_valid_isbn_3():
    """Validates a valid ISBN: <3>"""
    check50.run("python isbn.py").stdin("048665088X").stdout("YES").exit()

@check50.check(exists)
def test_invalid_isbn_1():
    """rejects an invalid ISBN: <4>"""
    check50.run("python isbn.py").stdin("111222333").stdout("NO").exit()

@check50.check(exists)
def test_invalid_isbn_2():
    """rejects an invalid ISBN: <5>"""
    check50.run("python isbn.py").stdin("1112223339X").stdout("NO").exit()

@check50.check(exists)
def test_invalid_isbn_3():
    """rejects an invalid ISBN: <6>"""
    check50.run("python isbn.py").stdin("1234512345").stdout("NO").exit()
