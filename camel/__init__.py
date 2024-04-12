import check50
from re import escape


@check50.check()
def exists():
    """camel.py exists"""
    check50.exists("camel.py")


@check50.check(exists)
def test_name():
    """input of \"<secret 1>\" yields output of \"<secret 1>\""""
    input = "variable"
    output = "variable"
    check50.run("python3 camel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_firstName():
    """input of \"<secret 2>\" yields output of \"<secret 2>\""""
    input = "myFirstName"
    output = "my_first_name"
    check50.run("python3 camel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_preferredFirstName():
    """input of \"<secret 3>\" yields output of \"<secret 3>\""""
    input = "wentworthComputerScienceCollege"
    output = "wentworth_computer_science_college"
    check50.run("python3 camel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(text):
    """match case-sensitively, allowing for characters on either side."""
    return fr'^.*{escape(text)}.*$'
