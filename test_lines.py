import sys
import io

import lines

s1 = set(["a", "b", "c", "d"])
s2 = set(["c", "d", "e", "f"])


def test_union():
    sys.stdout = io.StringIO()
    lines.main(["-u", "examples/f1", "examples/f2"])
    output = set(sys.stdout.getvalue().split())
    assert output == set(["a", "b", "c", "d", "e", "f"])

def test_intersection():
    sys.stdout = io.StringIO()
    lines.main(["-i", "examples/f1", "examples/f2"])
    output = set(sys.stdout.getvalue().split())
    assert output == set(["c", "d"])

def test_relative_complement():
    sys.stdout = io.StringIO()
    lines.main(["-d", "examples/f1", "examples/f2"])
    output = set(sys.stdout.getvalue().split())
    assert output == set(["a", "b"])

def test_symmetric_difference():
    sys.stdout = io.StringIO()
    lines.main(["-s", "examples/f1", "examples/f2"])
    output = set(sys.stdout.getvalue().split())
    assert output == set(["a", "b", "e", "f"])

def test_squeeze():
    sys.stdout = io.StringIO()
    lines.main(["--squeeze", "examples/f3"])
    output = sys.stdout.getvalue()
    assert output == "a\nb\nc\nd\ne\nf\n"

def test_patterns():
    sys.stdout = io.StringIO()
    lines.main(["--patterns", "examples/f4"])
    output = sys.stdout.getvalue()
    assert output == "17 elements\n1 elements - {'Wintermute'}\n"
    

    

    
