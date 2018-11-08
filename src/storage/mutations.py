
mutations = {}

def name(name):
    def cb(fn):
        mutations[name] = fn
        return staticmethod(fn)
    return cb
