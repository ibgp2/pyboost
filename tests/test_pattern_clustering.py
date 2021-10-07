#!/usr/bin/env pytest-3
# -*- coding: utf-8 -*-

# Note that everything is packed in pattern_clustering.so, so we import
# this module without regards of the imported class.

from pattern_clustering import PatternAutomaton, PatternClustering

def make_pattern_automata():
    alphabet_size = 26

    n1 = 5
    g1 = PatternAutomaton(n1, alphabet_size, "abc")
    for i in range(n1 - 1):
        g1.add_edge(i, i + 1, 0)

    n2 = 3
    g2 = PatternAutomaton(n2, alphabet_size, "def")
    for i in range(n2 - 1):
        g2.add_edge(i, i + 1, 0)

    return [g1, g2]

def make_densities():
    return [1.23, 4.56]

def test_pattern_clustering():
    pattern_automata = make_pattern_automata()
    densities = make_densities()
    pattern_clustering = PatternClustering(
        pattern_automata = pattern_automata,
        densities = densities,
        threshold = 0.5
    )
    pattern_clustering.compute()
