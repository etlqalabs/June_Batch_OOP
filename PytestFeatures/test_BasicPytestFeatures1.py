import pytest
import os
import time

@pytest.mark.prebuild
def test_Testcase1():
    print(f"Process id {os.getpid()}")
    time.sleep(2)
    assert 1 == 2 ,"Test case 1 failed"

@pytest.mark.prebuild
@pytest.mark.skip
def test_Testcase2():
    print(f"Process id {os.getpid()}")
    time.sleep(2)
    assert 1 == 1 ,"Test case 2 failed"

@pytest.mark.prebuild
def test_Testcase3():
    print(f"Process id {os.getpid()}")
    time.sleep(2)
    assert 1 > 2, "Test case 3 failed"

@pytest.mark.prebuild
@pytest.mark.skip
def test_Testcase4():
    print(f"Process id {os.getpid()}")
    time.sleep(2)
    assert 1 != 2 ,"Test case 4 failed"