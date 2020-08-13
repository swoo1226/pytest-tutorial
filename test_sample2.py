import pytest
@pytest.mark.set1
def test_file1_method1():
    x=5
    y=6
    assert x+1 == y, "test failed"
    assert x == y, f"test failed because x={x} y={y}!"
@pytest.mark.set1
def test_fil1_method2():
    x=5
    y=6
    assert x+1 == y,"test failed"