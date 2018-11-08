
class Model(object):

    @classmethod
    def values(cls):
        return [getattr(cls, x) for x in cls.__dict__ if not x.startswith("__")]
