# So you can execute the file with python to test the file
if __name__ == "__main__":
    import subprocess
    # use -k <string> to only run tests which contain the provided string
    subprocess.run('pytest')
    exit()

import pytest
from main import *

def test_1():
    assert True

def test_2():
    assert True

def test_dependencies():
    res = func1()
    print(res)
    assert True