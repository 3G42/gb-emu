from dataclasses import dataclass
from pathlib import Path


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