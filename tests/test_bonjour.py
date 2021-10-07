#!/usr/bin/env pytest-3
# -*- coding: utf-8 -*-

from pyboost import Bonjour

def test_bonjour_init():
    b = Bonjour()
    assert b.msg == ""
    assert b.int == 7
    b = Bonjour("1")
    assert b.msg == "1"
    assert b.int == 7
    b = Bonjour("2", 2)
    assert b.msg == "2"
    assert b.int == 2
    b = Bonjour(msg = "3", x = 3)
    assert b.msg == "3"
    assert b.int == 3
    b = Bonjour(x = 4, msg = "4")
    assert b.msg == "4"
    assert b.int == 4

def test_bonjour_get_set_msg():
    msg1 = "Salut"
    msg2 = "Hello"
    b = Bonjour(msg1)
    assert b.msg == msg1
    b.msg = msg2
    assert b.msg == msg2

def test_bonjour_sum():
    b = Bonjour("")
    assert b.sum(10, 2) == 12
