#!/usr/bin/env python3

import lines

s1 = set(["a", "b", "c", "d"])
s2 = set(["c", "d", "e", "f"])


def test_union():
    assert set(lines.union(s1, s2)) == set(["a", "b", "c", "d", "e", "f"])

def test_intersection():
    assert set(lines.intersection(s1, s2)) == set(["c", "d"])

def test_relative_complement():
    assert set(lines.relative_complement(s1, s2)) == set(["a", "b"])

def test_symmetric_difference():
    assert set(lines.symmetric_difference(s1, s2)) == set(["a", "b", "e", "f"])

    

    
