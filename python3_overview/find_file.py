"""Function annotations demo using plac
https://pypi.python.org/pypi/plac

Command line arguments are specified in function annotations. Try:

    python find_file.py -h
"""
import os
from fnmatch import filter

def main(pattern: "File pattern to match, e.g. '*.py'",
         sort: ("Sort results alphabetically", 'flag', 's'),
         directory: ("Directory in which to search", 'option') ='.'
        ):
    results = []
    for dirpath, dirnames, filenames in os.walk(directory):
        results.extend([os.path.join(dirpath, fn) for fn in filter(filenames, pattern)])
    if sort:
        results.sort()
    print(*results, sep='\n')

if __name__ == '__main__':
    import plac; plac.call(main)
