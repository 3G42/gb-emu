from pathlib import Path

from cartridge_reader import read_cartridge_metadata
from Decoder import Decoder




p = Path('gb/snake.gb')
opcode_file="gb/Opcodes.json"

dec = Decoder.create(opcode_file=opcode_file, data=p.read_bytes(), address=0)

_, instruction = dec.decode(0x201)

instruction.print()

