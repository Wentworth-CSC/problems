import check50
from re import escape


@check50.check()
def exists():
    """twttr.py exists"""
    check50.exists("twttr.py")


@check50.check(exists)
def test_twitter():
    """input of <word> yields output of <twitterised word>"""
    input = "Twitter"
    output = "Twttr"
    check50.run("python3 twttr.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_name():
    """input of \"<question>?\" yields output of \"<shortened question>?\""""
    input = "What's your name?"
    output = "Wht's yr nm?"
    check50.run("python3 twttr.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_cs50():
    """input of <code> yields output of <code>"""
    input = "WCSC50"
    output = "WCSC50"
    check50.run("python3 twttr.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_python():
    """input of <language> yields output of <Language>"""
    input = "PYTHON"
    output = "PYTHN"
    check50.run("python3 twttr.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


def regex(text):
    """match case-sensitively, allowing for characters on either side"""
    return fr'^.*{escape(text)}.*$'
