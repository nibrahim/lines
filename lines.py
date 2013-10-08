#!/usr/bin/env python3
# coding=utf-8

import sys
import argparse

__version__ = "0.1.0-a"

def union(s1, s2):
    return list(s1.union(s2))

def intersection(s1, s2):
    return list(s1.intersection(s2))

def relative_complement(s1, s2):
    return list(s1 - s2)

def symmetric_difference(s1, s2):
    return s1.union(s2) - s1.intersection(s2)
        
operations = {"u" : union,
              "i" : intersection,
              "d" : relative_complement,
              "s" : symmetric_difference}

def parse_args(args):
    parser = argparse.ArgumentParser(description = "Perform set operations on lines in file(s)")

    parser.add_argument('file1', type=str, help = "First file")
    parser.add_argument('file2', type=str, help = "Second file")

    operation = parser.add_mutually_exclusive_group(required = True)
    operation.add_argument('-u', action="store_true", help = "file1 ∪ file2 (union)")
    operation.add_argument('-i', action="store_true", help = "file1 ∩ file2 (intersection)")
    operation.add_argument('-d', action="store_true", help = "file1 - file2 (relative complement)")
    operation.add_argument('-s', action="store_true", help = "(file1 ∪ file2) - (file1 ∩ file2) (symmetric difference)")

    ret = parser.parse_args(args)
    operation = next((x for x in "u i d s".split() if getattr(ret,x)))
    
    return (operation, ret.file1, ret.file2)

def display(result):
    for i in result:
        print (i)

def main():
    operation, f1, f2 = parse_args(sys.argv[1:])
    try:
        with open(f1) as f1, open(f2) as f2:
            s1 = set(x.strip() for x in f1)
            s2 = set(x.strip() for x in f2)
            result = operations[operation](s1, s2)
            display(result)
        return 0
    except KeyError:
        print ("Couldn't find implementation of operation '-{}'".format(operation))
        return -1
    except IOError as e:
        print (str(e))
        return -1

if __name__ == '__main__':
    sys.exit(main())
