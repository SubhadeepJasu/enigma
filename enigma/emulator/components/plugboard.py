class PlugBoard:
    def __init__ (self):
        self._mapping = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

    def remap(self, alpha1, alpha2):
        self._mapping[ord(alpha1) - 65] = ord(alpha2) - 65
        self._mapping[ord(alpha2) - 65] = ord(alpha1) - 65

    def get_map(self, index):
        return self._mapping[index]