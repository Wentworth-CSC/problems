import check50
from re import escape


@check50.check()
def exists():
    """tea.py exists"""
    check50.exists("tea.py")


@check50.check(exists)
def test_no_tea():
    """input of \"D\" yields output of No Tea"""
    input = "D"
    output = "0 0 0 0 0 0"
    check50.run("python3 tea.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_order():
    """input of two teas yields output both teas in the correct order"""
    output = "200 100 0 0 0 0"
    check50.run("python3 tea.py").stdin("C 100", prompt=True).stdin("G 200", prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_list():
    """input of a series of teas give the correct result"""
    input = """C 3
E 4
P 9
L 21
C 5
S 4
E 19
G 5
C 7
P 1
D"""
    output = "5 15 23 10 21 4"
    check50.run("python3 tea.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

def regex(text):
    """match case-sensitively, allowing for characters on either side."""
    return fr'^.*{escape(text)}.*$'
