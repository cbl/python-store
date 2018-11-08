'''

'''
from src.utils import dict_merge
from src.helpers import Getter
from utils import class_methods, dict_array_search, module_name
from src.storage.actions import actions
from src.storage.mutations import mutations

class Store(object):
    '''
    The Store class.
    Controlls all store modules and the associated actions and mutations.
    '''

    _modules = []
    _actions = {}
    _mutations = {}
    _states = {}
    _mutation_states = {}

    def __init__(self, modules):
        # add modules
        for module in modules:
            self.add(module)

    def __getitem__(self, key):
        return Getter(self, key)

    def __getattr__(self, key):
        return Getter(self, key)

    def __str__(self):
        str = "Store:\n"
        for module, states in self._states.iteritems():
            module_states = {n: type(v) for n, v in states.iteritems()}
            str += '  {}: {}\n'.format(module, module_states)
        return str

    def add(self, module):
        '''
        Add a module to the store.
        '''
        # modules
        self._modules.append(module)
        # actions
        if hasattr(module, 'Actions'):
            self._actions = dict_merge(
                self._actions,
                dict_array_search(actions, class_methods(module.Actions))
                )
        # mutations
        if hasattr(module, 'Mutations'):
            mutations_dict = dict_array_search(mutations, class_methods(module.Mutations))
            self._mutations = dict_merge(
                self._mutations,
                mutations_dict
                )
            # save modules names for mutations
            for key in mutations_dict:
                self._mutation_states[key] = module_name(module)
        # states
        if hasattr(module, 'initial_states'):
            self._states[module_name(module)] = module.initial_states

    def dispatch(self, name, data=None):
        '''
        Dispatch an action.
        '''
        self._actions[name](self.commit, self.dispatch, data)

    def commit(self, name, data=None):
        '''
        Commit a mutation.
        '''
        self._mutations[name](
            self._states[self._mutation_states[name]],
            data
            )

    def states(self, key):
        return self._states[key]
