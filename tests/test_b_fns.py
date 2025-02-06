import pytest
from b_fns import calc

def test_true():
    assert True

def test_add():
    assert calc(1, 4, "+") == 5

def test_mult():
    assert calc(2, 4, "*") == 8

def test_subtract():
    assert calc(6, 4, "-") == 2