#!/usr/bin/env python3
# coding=utf-8

import sys
import argparse

from pylev import levenshtein

__version__ = "0.1.0-a"

def union(s1, s2):
    return list(s1.union(s2))

def intersection(s1, s2):
    return list(s1.intersection(s2))

def relative_complement(s1, s2):
    return list(s1 - s2)

def symmetric_difference(s1, s2):
    return s1.union(s2) - s1.intersection(s2)

def squeeze(f1, *args):
    for i in f1:
        if i.strip():
            yield i.strip()

def patterns(f1, dist = 55, outlier=10):
    """Will partition elements into subsets. The elements of a subset will
    not have a Levenshtein distance of more than :dist: from the other
    members of the same subset
    """
    sets = []
    seen = set()
    for i in (x.strip() for x in f1 if x.strip()):
        if i in seen:
            continue
        s = set([i])
        seen.add(i)
        others = set(x.strip() for x in f1 if x.strip()) - seen
        for j in others:
            v = levenshtein(i, j) 
            if v <= dist:
                s.add(j)
                seen.add(j)
        sets.append(s)

    # Format for printing
    outlier /= 100.0
    retval = []
    total = len(list(x.strip() for x in f1 if x.strip()))
    for i in sets:
        l = float(len(i))
        if l/total < outlier:
            retval.append("{} elements - {}".format(len(i), i))
        else:
            retval.append("{} elements".format(len(i)))
    
    return retval
        
        
two_set_operations = {"u" : union,
                      "i" : intersection,
                      "d" : relative_complement,
                      "s" : symmetric_difference}

one_set_operations = {"squeeze" : squeeze,
                      "patterns" : patterns}

def parse_args(args):
    parser = argparse.ArgumentParser(prog = "lines", description = "Perform set operations on lines in file(s)")
    parser.add_argument('file1', type=str, help = "First file", default = None)
    parser.add_argument('file2', type=str, help = "Second file", default = None, nargs = "?")

    operation = parser.add_mutually_exclusive_group(required = True)
    operation.add_argument('-u', action="store_true", help = "file1 ∪ file2 (union)")
    operation.add_argument('-i', action="store_true", help = "file1 ∩ file2 (intersection)")
    operation.add_argument('-d', action="store_true", help = "file1 - file2 (relative complement)")
    operation.add_argument('-s', action="store_true", help = "(file1 ∪ file2) - (file1 ∩ file2) (symmetric difference)")
    operation.add_argument('--squeeze', action="store_true", help = "squeezes out newlines from input file1")
    operation.add_argument('--patterns', action="store_true", help = "Groups lines by pattern")
    pattern_params = parser.add_argument_group(title = "pattern parameters", description = "parameters for pattern detection")
    pattern_params.add_argument("-l", type=int, help = "Edit distance used to group elements. Lower means more refined.", default = 10)
    pattern_params.add_argument("-p", type=float, help = "Number of elements (as a percentage) below which actual elements should be displayed along with groups.", default = 10)
    
    ret = parser.parse_args(args)
    try:
        operation = next((x for x in "u i d s squeeze patterns".split() if getattr(ret,x)))
    except StopIteration as s:
        raise argparse.ArgumentTypeError("Unknown operation")
    
    return (operation, ret.file1, ret.file2, ret.l, ret.p)

def display(result):
    for i in result:
        print (i)

def operate(operation, f1, f2, distance, outlier_limit):
    if operation in two_set_operations:
        with open(f1) as f1, open(f2) as f2:
            s1 = set(x.strip() for x in f1)
            s2 = set(x.strip() for x in f2)
            result = two_set_operations[operation](s1, s2)
    elif operation in one_set_operations:
        with open(f1) as f1:
            result = one_set_operations[operation](list(f1), distance, outlier_limit)
    else:
        raise KeyError("Couldn't find implementation of operation '-{}'".format(operation))
    return result


def main(args):
    operation, f1, f2, distance, outlier_limit = parse_args(args)
    try:
        result = operate(operation, f1, f2, distance, outlier_limit)
        display(result)
        return 0
    except KeyError as k:
        print(k)
        return -1
    except IOError as e:
        print (str(e))
        return -1

def entry():
    sys.exit(main(sys.argv[1:]))

if __name__ == '__main__':
    entry()
