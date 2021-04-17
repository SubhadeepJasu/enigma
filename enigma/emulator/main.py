import enigma_machine as em

message_string = "ICHHEISEADHIRAJ"

enigma_machine = em.EnigmaMachine()
enigma_machine.connect_rotor(1, enigma_machine.get_rotor_by_name("IIC"))
enigma_machine.connect_rotor(2, enigma_machine.get_rotor_by_name("I-K"))
enigma_machine.connect_rotor(3, enigma_machine.get_rotor_by_name("IIIC"))
enigma_machine.remap_plugboard('A','X')

cypher = ""
for alphabet in message_string:
    cypher += enigma_machine.type_alphabet(alphabet)

print(cypher)

enigma_machine.set_rotor_config(0,0,0)

original = ""
for alphabet in cypher:
    original += enigma_machine.type_alphabet(alphabet)

print(original)