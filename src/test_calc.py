#!/usr/bin/env python3

import pytest
from calc import add, subtract, multiply, divide, power

def test_add():
    assert add(2,2) == 4

def test_subtract():
    assert subtract(2,2) == 0

def test_multiply():
    assert multiply(2,0) == 0

def test_divide():
    assert divide(2,1) == 2

def test_power():
    assert power(2,2) == 4

