
class Getter(object):

    def __init__(self, store, name):
        self._store = store
        self._name = name

    def __getitem__(self, key):
        return self._store.states(self._name)[key]

    def __getattr__(self, key):
        return self._store.states(self._name)[key]

    def __str__(self):
        return str(self._store.states(self._name))
