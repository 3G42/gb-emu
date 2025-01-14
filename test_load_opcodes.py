from load_opcodes import load_opcodes

def test_load_opcodes():
    prefixed,regular = load_opcodes("gb/Opcodes.json")
    
    
    for opcode in regular:
        print(regular[opcode])
    print(prefixed['0x26'])
if __name__ == "__main__":
    test_load_opcodes()