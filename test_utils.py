import pytest
import utils

def test_fact():
    # À compléter...
    assert utils.fact(4)==24
    assert utils.fact(3)==6

def test_roots():
    # À compléter...
    assert utils.roots(1,0,-1)==(-1,1)
    assert utils.roots(1,-6,9)==(3)

def test_integrate():
    # À compléter...
    assert utils.integrate(x**2,1,2)==7
    assert utils.integrate(x-7,0,4)==-12
