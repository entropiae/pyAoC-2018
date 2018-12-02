import os


def read_file(fname):
    abs_fname = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "data", fname))
    with open(abs_fname) as f:
        return f.readlines()
