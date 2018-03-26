# json-diff

Compares json files. Right now supports only certain format. Generalizing will be done soon.

##### Usage
    python json-diff.py <file1> <file2> [<file3> [<file4>] ...]

The output will contain the differences, and the program will also create the diff json under <code>diff</code> directory. All the files will be diffed against each other.