from load_opcodes import load_opcodes

def test_load_opcodes():
    prefixed,regular = load_opcodes("gb/Opcodes.json")
    
    
    assert "0x00" in regular
    assert regular["0x00"].opcode == "0x00"
    assert len(regular["0x00"].operands) == 0
    
    print(prefixed["0x00"].print())
    
    print("Todos os testes passaram.")
    
if __name__ == "__main__":
    test_load_opcodes()