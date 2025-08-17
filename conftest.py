import pytest

@pytest.fixture(autouse=False)
def generic_printing():
    print(" Fixture -- Before test cases strated.....")
    print()
    yield
    print("Fixture -- After test case finsihed .....")
