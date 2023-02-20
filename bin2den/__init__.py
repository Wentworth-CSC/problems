import check50
import check50.c

@check50.check()
def exists():
    """bin2den.py exists"""
    check50.exists("bin2den.py")

@check50.check(exists)
def nibble_1():
    """responds to one nibble (1111)"""
    check50.run("python bin2den.py").stdin("1111").stdout("15").exit()

@check50.check(exists)
def nibble_2():
    """responds to one nibble (0000)"""
    check50.run("python bin2den.py").stdin("0000").stdout("0").exit()

@check50.check(exists)
def nibble_3():
    """responds to one nibble (1100)"""
    check50.run("python bin2den.py").stdin("1100").stdout("10").exit()

@check50.check(exists)
def byte_1():
    """responds to one byte"""
    check50.run("python bin2den.py").stdin("00000000").stdout("0").exit()
    
@check50.check(exists)
def byte_2():
    """responds to one byte with a space"""
    check50.run("python bin2den.py").stdin("0000 0000").stdout("0").exit()
    
@check50.check(exists)
def byte_3():
    """responds to one byte"""
    check50.run("python bin2den.py").stdin("11111111").stdout("255").exit()
    
@check50.check(exists)
def byte_4():
    """responds to one byte"""
    check50.run("python bin2den.py").stdin("1111 1111").stdout("255").exit()
    
@check50.check(exists)
def byte_5():
    """responds to one byte"""
    check50.run("python bin2den.py").stdin("1001 1100").stdout("156").exit()
    
@check50.check(exists)
def odd length_1():
    """responds to binary streams of odd lengths"""
    check50.run("python bin2den.py").stdin("10000").stdout("16").exit()
   
