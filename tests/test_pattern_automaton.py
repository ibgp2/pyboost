#!/usr/bin/env pytest-3
# -*- coding: utf-8 -*-

# Note that everything is packed in pattern_clustering.so, so we import
# this module without regards of the imported class.
from pattern_clustering import PatternAutomaton

def test_pattern_automaton_init():
    g = PatternAutomaton(
        num_vertices = 5,
        alphabet_size = 10,
        word = "abc"
    )
    assert g.num_vertices() == 5
    assert g.alphabet_size() == 10
    assert g.num_edges() == 0

def test_pattern_automaton_add_vertex():
    g = PatternAutomaton(5, 10, "abc")
    assert g.num_vertices() == 5
    g.add_vertex()
    assert g.num_vertices() == 6

def test_pattern_automaton_add_edge():
    g = PatternAutomaton(5, 10, "abc")
    assert g.num_edges() == 0
    g.add_edge(0, 1, 2) # (q, r, a)
    assert g.num_edges() == 1
    # TODO check RuntimeError
    #g.add_edge(0, -1, 2) # Raise a RuntimeError

def test_pattern_automaton_to_string():
    g = PatternAutomaton(5, 10, "abc")
    g.add_edge(0, 1, 2)
    g.add_edge(0, 1, 3)
    assert str(g) == '0--[2]-->1\n0--[3]-->1\n'
