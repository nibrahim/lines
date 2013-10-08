Lines
=====

Introduction
------------

Lines is a simple program that allows you to manipulate lines of a
file as if they were members of a set. It also provides a few other
useful functions to analyse such files.

Set operations
--------------
Given two files 

`file1` containing

    a
    b
    c
    d

and `file2` with
   
    c
    d
    e
    f

It's possible to do things like

* *Unions*

`lines -u file1 file2`

gives

    a
    b
    c
    d
    e
    f

* *Intersections*

`lines -i file1 file2`

gives
    
    c
    d
    
* *Difference* (All elements in `file1` that are not in `file2`).

`lines -d file1 file2`

gives

    a
    b

* *Symmetric difference* (All elements present in only one of the
   sets). 

`lines -s file1 file2`

gives

    a
    b
    e
    f
    
   
Other Operations
----------------

These are a few other operations which I've found useful

* *Squeeze blanks*

This operation squeezes out the blank lines in a file. 

So, If you run
`lines --squeeze file1` where `file1` looks like this


    a
    b
    c
    
    d

    f

You'd get

    a
    b
    c
    d
    f
    
* *Identify Patterns*

This partitions the elements of the set into subsets all of whose
members have an upper bound on the levenshtein distance from each
other. This is useful to identify patterns in the input file.

So, if I have a file `examples/f6` that looks like this

    Archive.001-of-020.part
    Archive.002-of-020.part
    Archive.003-of-020.part
    Archive.004-of-020.part
    Archive.005-of-020.part
    Archive.006-of-020.part
    Archive.007-of-020.part
    .Archive.008-of-020.part.zbnrw
    Archive.009-of-020.part
    Archive.010-of-020.part
    Archive.011-of-020.part
    Archive.012-of-020.part
    Archive.013-of-020.part
    Archive.014-of-020.part
    Archive.015-of-020.part
    Archive.016-of-020.part
    Archive.017-of-020.part
    Archive.018-of-020.part
    Archive.019-of-020.part
    Archive.020-of-020.part

I can run `python lines.py --patterns -l 5 examples/f6` and get


    19 elements
    1 elements - {'.Archive.008-of-020.part.zbnrw'}

The `-l 5` is to set the upper bound on the levenshtein distance
to 5. The `-p` option allows us to specify an "outlier percentage". If
the number of elements in a subset is below this, it will print all
the elements of the subset. This is useful to see the items that don't
match the general pattern in the file.






