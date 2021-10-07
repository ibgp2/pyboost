#!/usr/bin/env pytest-3
# -*- coding: utf-8 -*-

from pyboost import StlExample, Floats, MapStrFloat

def test_stl_example_list_get():
    s = StlExample()
    assert isinstance(s.ints, list)
    assert s.ints == [1, 2, 3]

def test_stl_example_list_set():
    s = StlExample()
    new_ints = 10 * [1, 2, 3]
    s.ints = new_ints
    assert s.ints == new_ints

def test_stl_example_dict_get():
    s = StlExample()
    assert isinstance(s.map_str_int, dict)
    assert s.map_str_int == {"a" : 10, "b" : 20, "c" : 30}

def test_stl_example_dict_set():
    s = StlExample()
    new_map_str_int = {"A" : 1, "B" : 2, "C" : 3}
    s.map_str_int = new_map_str_int
    assert s.map_str_int == new_map_str_int

def to_list(vector):
    return [x for x in vector]

def test_stl_example_vector_get():
    s = StlExample()
    assert isinstance(s.floats, Floats)
    assert to_list(s.floats) == [1.1, 2.2, 3.3]

def test_stl_example_vector_set():
    def to_floats(l):
        floats = Floats()
        floats.extend(l)
        return floats

    s = StlExample()
    new_floats = to_floats([-1.1, -2.2, -3.3])
    assert isinstance(new_floats, Floats)
    assert to_list(s.floats) != to_list(new_floats)
    s.floats = new_floats
    assert to_list(s.floats) == to_list(new_floats)

def to_dict(m):
    return {p.key() : p.data() for p in m}

def test_stl_example_map_get():
    s = StlExample()
    assert isinstance(s.map_str_float, MapStrFloat)
    assert to_dict(s.map_str_float) == {"a" : 10.1, "b" : 20.2, "c" : 30.3}

def test_stl_example_map_set():
    def to_map_str_float(d):
        map_str_float = MapStrFloat()
        for (k, v) in d.items():
            map_str_float[k] = v
        return map_str_float

    s = StlExample()
    new_map_str_float = to_map_str_float({"A" : -1.1, "b" : -2.2, "c" : -3.3})
    assert isinstance(new_map_str_float, MapStrFloat)
    assert to_dict(s.map_str_float) != to_dict(new_map_str_float)
    s.map_str_float = new_map_str_float
    assert to_dict(s.map_str_float) == to_dict(new_map_str_float)
