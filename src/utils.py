import os


def expandedpath(path):
    """uses echo from system to find the path with variables for cases like user"""
    return os.path.expanduser(os.path.expandvars(path))


def pathexists(path):
    """sees if the folder exists"""
    return os.path.isdir(path)
