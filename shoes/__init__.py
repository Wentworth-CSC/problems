import check50
from re import escape


@check50.check()
def exists():
    """shoes.py exists"""
    check50.exists("shoes.py")


@check50.check(exists)
def test_greenmissing():
    """input of \"GGG\" yields output of \"A Green shoe has no partner.\""""
    input = "GGG"
    output = "A Green shoe has no partner."
    check50.run("python3 shoes.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_fullset():
    """input of \"BlBrBrBlGBGBrBlBrMR\" yields output showing 4 missing shoes"""
    input = "BlBrBrBlGBGBrBlBrMR"
    output = """A Black shoe has no partner.
A Red shoe has no partner.
A Blue shoe has no partner.
A Mustard shoe has no partner."""
    check50.run("python3 shoes.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

@check50.check(exists)
def test_happyset():
    """input of \"GGBBBlBlBrBrRRMM\" yields output of \"first_name\""""
    input = "GGBBBlBlBrBrRRMM"
    output = "All paired up!"
    check50.run("python3 shoes.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()

def regex(text):
    """match case-sensitively, allowing for characters on either side."""
    return fr'^.*{escape(text)}.*$'
