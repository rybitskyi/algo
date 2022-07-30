from collections import OrderedDict


class DigraphSpec:

    def __init__(self):
        self.g = self._new_g()

    def _new_g(self):
        '''
        Directed Graph.
        :return: Adjacency Lists graph representation.
        '''
        return OrderedDict([('q', ['s', 't', 'w']),
                            ('r', ['u', 'y']),
                            ('s', ['v']),
                            ('t', ['x', 'y']),
                            ('u', ['y']),
                            ('v', ['w']),
                            ('w', ['s']),
                            ('x', ['z']),
                            ('y', ['q']),
                            ('z', ['x'])])

    def get_discovered_times(self):
        return {'q': 1, 's': 2, 'v': 3, 'w': 4, 't': 8, 'x': 9, 'z': 10, 'y': 13, 'r': 17, 'u': 18}

    def get_finished_times(self):
        return {'w': 5, 'v': 6, 's': 7, 'z': 11, 'x': 12, 'y': 14, 't': 15, 'q': 16, 'u': 19, 'r': 20}
