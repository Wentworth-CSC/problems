import check50

HASHES = {
    "muppet_01.jpg" : '521759559861a370743ba59e3c3a08a22c92f99bf6c257d9878dc106f48acb25',
    "muppet_02.jpg" : 'b99d17352f29f836d36316a706c06e530268d003c78313cdf577adc427ab3520',
    "muppet_03.jpg" : '8cc10b9f0acab1072ed781cc0fec1dde8730f24e7bd2c04198298cc5f0f485de',
    "muppet_04.jpg" : '1903b4332ffda57d2e59a634f0d6f44945d07900ad313385af432dcf983ea435',
    "muppet_05.jpg" : 'a841305cdee3a9f7167264841e44773cb3b867de1869eec181d94f1d9822362f',
    "muppet_06.jpg" : '50fbe244c96e2f78c3971c359572dcdc4474c632fae910f89be058ee1cd5f28f',
}


@check50.check()
def exists():
    """shirt.py exists"""
    check50.exists("shirt.py")
    check50.include("shirt.png")


@check50.check(exists)
def test_fewer_arguments():
    """shirt.py exits given zero command-line arguments"""
    exit = check50.run("python3 shirt.py").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_invalid_extension():
    """shirt.py exits given a file without a .jpg, .jpeg, or .png extension"""
    check50.include("invalid_extension.bmp")
    exit = check50.run("python3 shirt.py invalid_extension.bmp").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_non_existent_file():
    """shirt.py exits given a non-existent file"""
    exit = check50.run("python3 shirt.py non_existent_file.jpg").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_mismatched_extension():
    """shirt.py exits given an output file with a different extension than input file"""
    check50.include("muppet_01.jpg")
    exit = check50.run("python3 shirt.py muppet_01.jpg muppet_01_out.png").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_more_arguments():
    """shirt.py exits given more than two command-line arguments"""
    for file in ["muppet_01.jpg", "muppet_02.jpg", "muppet_03.jpg"]:
        check50.include(file)
    exit = check50.run("python3 lines.py muppet_01.jpg muppet_02.jpg muppet_03.jpg").exit()
    if exit == 0:
        raise check50.Failure(f"Expected non-zero exit code.")


@check50.check(exists)
def test_muppet_01():
    """shirt.py correctly displays shirt on muppet_01.jpg"""
    test_shirt("muppet_01.jpg")


@check50.check(exists)
def test_muppet_02():
    """shirt.py correctly displays shirt on muppet_02.jpg"""
    test_shirt("muppet_02.jpg")


@check50.check(exists)
def test_muppet_03():
    """shirt.py correctly displays shirt on muppet_03.jpg"""
    test_shirt("muppet_03.jpg")


@check50.check(exists)
def test_muppet_04():
    """shirt.py correctly displays shirt on muppet_04.jpg"""
    test_shirt("muppet_04.jpg")


@check50.check(exists)
def test_muppet_05():
    """shirt.py correctly displays shirt on muppet_05.jpg"""
    test_shirt("muppet_05.jpg")


@check50.check(exists)
def test_muppet_06():
    """shirt.py correctly displays shirt on muppet_06.jpg"""
    test_shirt("muppet_06.jpg")


def test_shirt(photo):
    check50.include(photo)
    check50.run(f"python3 shirt.py {photo} {photo[:-4]}_out.jpg").exit(0)
    hash = check50.hash(f"{photo[:-4]}_out.jpg")
    if hash != HASHES[photo]:
        raise check50.Failure("Image does not match")