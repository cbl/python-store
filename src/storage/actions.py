
actions = {}

def name(name):
    def cb(fn):
        actions[name] = fn
        return staticmethod(fn)
    return cb
