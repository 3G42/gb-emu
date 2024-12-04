from dataclasses import dataclass
from pathlib import Path
import sys


@dataclass
class Decoder:
    
    data:bytes
    address:int
    prefixed_instructions:dict
    instructions:dict
    
    @classmethod
    def create(cls, opcode_file: Path, data:bytes, address:int=0 ):
        prefixed, regular = load_opcodes(opcode_file)
        return cls(
            prefixed_instructions=prefixed,
            instructions=regular,
            data=data,
            address=address
        )
    def read(self, address:int, count: int = 1):
        """
        Lê `count` bytes iniciando de `address`
        """
        
        if 0 <= address + count <= len(self.data):
            v = self.data[address : address + count]
            return int.from_bytes(v, sys.byteorder)
