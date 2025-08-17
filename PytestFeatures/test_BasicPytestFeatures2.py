import pytest

@pytest.mark.order(3)
@pytest.mark.smoke
@pytest.mark.xfail
def test_Testcase1():
    assert 1 == 2 ,"Test case 1 failed"

@pytest.mark.order(4)
@pytest.mark.smoke
@pytest.mark.skip
def test_Testcase2():
    assert 1 == 1 ,"Test case 2 failed"

@pytest.mark.order(2)
@pytest.mark.regression
@pytest.mark.smoke
def test_Testcase3():
    assert 1 == 1, "Test case 3 failed"

@pytest.mark.order(1)
@pytest.mark.regression
@pytest.mark.smoke
def test_Testcase4():
    assert 1 != 2 ,"Test case 4 failed"