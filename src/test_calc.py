#!/usr/bin/env python3

import pytest
from calc import add, subtract, multiply, divide, power

def test_add1():
    assert add(2,2) == 4

def test_subtract1():
    assert subtract(2,2) == 0

def test_multiply1():
    assert multiply(2,0) == 0

def test_divide1():
    assert divide(2,0) == 2

def test_power1():
    assert power(2,2) == 4
