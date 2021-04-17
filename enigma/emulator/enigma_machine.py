import components.rotor     as rt
import components.reflector as rf
import components.plugboard as pb

class EnigmaMachine():
    rotor1 = object
    rotor2 = object
    rotor3 = object

    rotate_callback_1 = None
    rotate_callback_2 = None
    rotate_callback_3 = None

    def __init__(self):
        self._rotorArray = \
        [rt.Rotor("DMTWSILRUYQNKFEJCAZBPGXOHV", 0, "IC"),   \
         rt.Rotor("HQZGPJTMOBLNCIFDYAWVEUSRKX", 0, "IIC"),  \
         rt.Rotor("UQNTLSZFMREHDPXKIBVYGJCWOA", 0, "IIIC"), \
         rt.Rotor("PEZUOHXSCVFMTBGLRINQJWAYDK", 0, "I-K"),  \
         rt.Rotor("ZOUESYDKFWPCIQXHMVBLGNJRAT", 0, "II-K"), \
         rt.Rotor("EHRVXGAOBQUSIMZFLYNWKTPDJC", 0, "III-K")]
        self._reflectorUKW = rf.Reflector("QYHOGNECVPUZTFDJAXWMKISRBL")
        self._plugboard = pb.PlugBoard()

    def get_all_rotor_names(self):
        names = []
        for rotor in self._rotorArray:
            names.append(rotor.get_name())
        return names
    
    def get_number_of_rotors(self):
        return len(self._rotorArray)

    def get_rotor_by_name(self, name):
        for rotor in self._rotorArray:
            if (rotor.get_name() == name):
                return rotor
        return None

    def connect_rotor(self, index, rotor, _callback = None):
        if index == 1:
            self.rotor1 = rotor
            self.rotate_callback_1 = _callback
        elif index == 2:
            self.rotor2 = rotor
            self.rotate_callback_2 = _callback
        elif index == 3:
            self.rotor3 = rotor
            self.rotate_callback_3 = _callback
        else:
            self.rotor1 = rotor
            self.rotate_callback_1 = _callback

    def set_rotor_config(self, index1, index2, index3):
        self.rotor1.set_rotor_code(index1)
        self.rotor2.set_rotor_code(index2)
        self.rotor3.set_rotor_code(index3)

    def rotate_rotor_1(self, direction):
        self.rotor1.rotate(direction, self._handle_rotate_rotor1)

    def rotate_rotor_2(self, direction):
        self.rotor2.rotate(direction, self._handle_rotate_rotor2)

    def rotate_rotor_3(self, direction):
        self.rotor3.rotate(direction, self._handle_rotate_rotor3)

    def remap_plugboard(self, alpha1, alpha2):
        self._plugboard.remap(alpha1, alpha2)

    def type_alphabet(self, alphabet):
        plug_in = self._plugboard.get_map(ord(alphabet) - 65)
        if self.rotor1.rotate(True, self._handle_rotate_rotor1):
            if self.rotor2.rotate(True, self._handle_rotate_rotor2):
                self.rotor3.rotate(True, self._handle_rotate_rotor3)
        index1 = self.rotor1.connect_forward(plug_in)
        index2 = self.rotor2.connect_forward(index1)
        index3 = self.rotor3.connect_forward(index2)
        index4 = self._reflectorUKW.reflect(index3)
        index5 = self.rotor3.connect_reverse(index4)
        index6 = self.rotor2.connect_reverse(index5)
        index7 = self.rotor1.connect_reverse(index6)
        plug_out = self._plugboard.get_map(index7)
        return chr(plug_out + 65)
    
    def _handle_rotate_rotor1(self, direction):
        if self.rotate_callback_1 is not None:
            self.rotate_callback_1(direction)
    
    def _handle_rotate_rotor2(self, direction):
        if self.rotate_callback_2 is not None:
            self.rotate_callback_2(direction)

    def _handle_rotate_rotor3(self, direction):
        if self.rotate_callback_3 is not None:
            self.rotate_callback_3(direction)

    def get_rotor1_alphabet (self):
        return self.rotor1.get_current_rotor_code()

    def get_rotor2_alphabet (self):
        return self.rotor2.get_current_rotor_code()

    def get_rotor3_alphabet (self):
        return self.rotor3.get_current_rotor_code()