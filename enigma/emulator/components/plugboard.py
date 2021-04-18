class PlugBoard:
    def __init__ (self):
        self._wiring = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        self._key_alphabets = "QWERTZUIOASDFGHJKPYXCVBNML"

    def remap(self, alpha1, alpha2):
        self._wiring[ord(alpha1) - 65] = ord(alpha2) - 65
        self._wiring[ord(alpha2) - 65] = ord(alpha1) - 65

    def get_map(self, index):
        return self._wiring[index]

    def get_plugged_entries(self):
        mapping_array = []
        index = 0
        while index < 26:
            if index != self._wiring[index]:
                mapping_array.append(True)
            else:
                mapping_array.append(False)
            print(index != self._wiring)
            index+=1
        index = 0
        arranged_array = []
        while index < 26:
            arranged_array.append(mapping_array[ord(self._key_alphabets[index]) - 65])
            index += 1
        return arranged_array