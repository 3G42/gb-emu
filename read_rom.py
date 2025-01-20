from pathlib import Path

from cartridge_reader import read_cartridge_metadata
from Decoder import Decoder

def disassemble(decoder: Decoder, address:int, count:int):
    for _ in range(count):
        try:
            new_address,instruction = decoder.decode(address)
            pp = instruction.print()
            print(f'{address:>04X}  {pp}')
            address = new_address
        except IndexError as e:
            print('ERROR - {e!s}')
            break





if __name__ == "__main__":
    p = Path('gb/snake.gb').read_bytes()
    opcode_file="gb/Opcodes.json"
    dec = Decoder.create(opcode_file=opcode_file, data=p, address=0)
    disassemble(dec,0x150,16)

