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

This groups the elements of the set into groups all of whose members
don't have an edit distance of more than (by default) 3 between
them. It's useful to identify "irregular patterns" in a large file.

TBD



