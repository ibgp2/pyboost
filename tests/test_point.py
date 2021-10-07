#!/usr/bin/env pytest-3
# -*- coding: utf-8 -*-

from pyboost import Point, extract_x, extract_y

def test_point():
    p1 = Point()
    assert p1.x == 0
    assert p1.y == 0
    p2 = Point(1, 2)
    assert p2.x == 1
    assert p2.y == 2

def test_point_extract():
    p2 = Point(1, 2)
    assert extract_x(p2) == p2.x
    assert extract_y(p2) == p2.y
