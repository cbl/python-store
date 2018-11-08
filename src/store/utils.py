
def class_methods(cls):
    return [getattr(cls, x) for x in dir(cls) if not x.startswith("__")]

def dict_array_search(dict, array):
    return {n: v for n, v in dict.iteritems() if v in array}

def module_name(module):
    return module.__name__.split('.')[-1]
