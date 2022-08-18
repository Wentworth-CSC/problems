import check50

@check50.check()
def exists():
    """isbn.py exists."""
    check50.exists("isbn.py")

@check50.check(exists)
def test_valid_isbn_1():
    """Validates a valid ISBN: 1112223339"""
    check50.run("python isbn.py").stdin("1112223339").stdout("YES").exit()

@check50.check(exists)
def test_valid_isbn_2():
    """Validates a valid ISBN: 1234554321"""
    check50.run("python isbn.py").stdin("1234554321").stdout("YES").exit()
    
@check50.check(exists)
def test_valid_isbn_3():
    """Validates a valid ISBN: 048665088X"""
    check50.run("python isbn.py").stdin("048665088X").stdout("YES").exit()

@check50.check(exists)
def test_valid_isbn_3():
    """rejects an invalid ISBN: 1112223334"""
    check50.run("python isbn.py").stdin("111222333").stdout("NO").exit()

@check50.check(exists)
def test_valid_isbn_3():
    """rejects an invalid ISBN: 1112223339X"""
    check50.run("python isbn.py").stdin("1112223339X").stdout("NO").exit()

@check50.check(exists)
def test_valid_isbn_3():
    """rejects an invalid ISBN: 1234512345"""
    check50.run("python isbn.py").stdin("1234512345").stdout("NO").exit()
