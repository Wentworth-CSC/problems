import check50

@check50.check()
def exists():
    """punch.py exists."""
    check50.exists("punch.py")
    check50.include("22.txt", "23.txt", "34.txt", "58.txt")

#@check50.check(exists)
#def test_reject_negative():
#    """rejects a width of -1"""
#    check50.run("python3 punch.py").stdin("-1").reject()

#@check50.check(exists)
#def test0():
#    """rejects a height of 0"""
#    check50.run("python3 punch.py").stdin("0").reject()

@check50.check(exists)
def test1():
    """handles a height of 2 2 correctly"""
    out = check50.run("python3 punch.py").stdin("2 2").stdout()
    check_card(out, open("22.txt").read())

@check50.check(exists)
def test2():
    """handles a height of 2 3 correctly"""
    out = check50.run("python3 punch.py").stdin("2 3").stdout()
    check_card(out, open("23.txt").read())

@check50.check(exists)
def test34():
    """handles a height of 3 4 correctly"""
    out = check50.run("python3 punch.py").stdin("3 4").stdout()
    check_card(out, open("34.txt").read())
    
@check50.check(exists)
def test58():
    """handles a height of 5 8 correctly"""
    out = check50.run("python3 punch.py").stdin("5 8").stdout()
    check_card(out, open("58.txt").read())

#@check50.check(exists)
#def test24():
#    """rejects a height of 9, and then accepts a height of 2"""
#    (check50.run("python3 punch.py").stdin("9").reject()
#            .stdin("2").stdout(open("2.txt")).exit(0))

#@check50.check(exists)
#def test_reject_foo():
#    """rejects a non-numeric height of "foo" """
#    check50.run("python3 punch.py").stdin("foo").reject()

#@check50.check(exists)
#def test_reject_empty():
#    """rejects a non-numeric height of "" """
#    check50.run("python3 punch.py").stdin("").reject()


def check_card(output, correct):
    if output == correct:
        return

    output = [line for line in output.splitlines() if line != ""]
    correct = correct.splitlines()

    help = None
    if len(output) == len(correct):
        if all(ol.rstrip() == cl for ol, cl in zip(output, correct)):
            help = "Did you add too much trailing whitespace to the end of your card?"
        elif all(ol[1:] == cl for ol, cl in zip(output, correct)):
            help = "Are you printing an additional character at the beginning of each line?"

    raise check50.Mismatch(correct, output, help=help)

    
