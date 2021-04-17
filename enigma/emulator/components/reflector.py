class Reflector:
    def __init__ (self, wiring):
        self._wiring = []
        for wire in wiring:
            self._wiring.append(ord(wire) - 65)

    def reflect(self, index):
        # print("reflect")
        # print(self._wiring[index])
        return self._wiring[index]