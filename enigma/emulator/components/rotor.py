class Rotor():
    def __init__ (self, wiring, starting_index, name = ""):
        self._wiring = []
        self._index = starting_index
        self._name = name
        for wire in wiring:
            self._wiring.append(ord(wire) - 65)

    def connect_forward(self, connection_index):
        return self._get_index_increment(self._wiring[self._get_index_increment(connection_index)])
    
    def connect_reverse(self, connection_index):
        ret_index = 0
        for index in self._wiring:
            if index == self._get_index_decrement(connection_index):
                return self._get_index_decrement(ret_index)
            ret_index+=1
        return 0
    
    def rotate(self, direction = True, _callback = None):
        if direction:
            self._index+=1
            if self._index == 26:
                self._index=0
                _callback(direction)
                return True
        else:
            self._index-=1
            if self._index == -1:
                self._index=25
                _callback(direction)
                return True
        _callback(direction)
        return False

    def _get_index_increment(self, index):
        return (index + self._index) % 26
    
    def _get_index_decrement(self, index):
        if (index - self._index) < 0:
            return 26 + index - self._index
        return (index - self._index) % 26
    
    def set_rotor_code(self, index):
        self._index = index

    def get_current_rotor_code(self):
        return chr(self._index + 65)
    
    def get_name(self):
        return self._name