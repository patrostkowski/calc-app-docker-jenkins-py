#!/usr/bin/env python3

import pytest
from calc import add, subtract, multiply, divide, power

def test_add1():
    assert add(2,2) == 4

def test_add2():
    assert add(-1,1) == 0

def test_add3():
    assert add(4,4) == 8

def test_subtract1():
    assert subtract(2,2) == 0

def test_subtract2():
    assert subtract(1,-1) == 2

def test_multiply1():
    assert multiply(2,0) == 0

def test_multiply2():
    assert multiply(1,2) == 2

def test_divide1():
    assert divide(2,1) == 2

def test_divide2():
    assert divide(3,2) == 1.5

def test_power1():
    assert power(2,2) == 4

def test_power2():
    assert power(2,3) == 8

