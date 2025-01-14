from dataclasses import dataclass, field
from typing import List, Literal, Optional


@dataclass(frozen=True)
class Operand:

    immediate: bool
    name: str
    bytes: Optional[int]
    adjust: Optional[Literal["+", "-"]]
    value: Optional[int] = None

    def create(self, value: Optional[int]):
        return Operand(
            immediate=self.immediate,
            name=self.name,
            bytes=self.bytes,
            value=value,
            adjust=self.adjust,
            
        )
    def copy(self, value: Optional[int] = None):
        return Operand(
            immediate=self.immediate,
            name=self.name,
            bytes=self.bytes,
            value=value if value is not None else self.value,
            adjust=self.adjust,
        )
    def print(self):
        if self.adjust is None:
            adjust = ""
        else:
            adjust = self.adjust
        if self.value is not None:
            if self.bytes is not None:
                val = hex(self.value)
            else:
                val = self.value
            v = val
        else:
            v = self.name
        v = v + adjust
        if self.immediate:
            return v
        return f'({v})'

@dataclass
class Instruction:
    opcode:int
    immediate: bool
    cycles:list[int]
    bytes:int
    mnemonic:str
    operands: List[Operand] = field(default_factory=list)
    comment: str =""
    flags:str=''
    
    def create(self,operands):
        return Instruction(
            opcode=self.opcode,
            immediate=self.immediate,
            operands=operands,
            cycles=self.cycles,
            bytes=self.bytes,
            mnemonic=self.mnemonic,
            flags=self.flags)
    def copy(self,operands=None):
        return Instruction(
            opcode=self.opcode,
            immediate=self.immediate,
            operands=operands if operands is not None else self.operands,
            cycles=self.cycles,
            bytes=self.bytes,
            mnemonic=self.mnemonic,
            flags=self.flags
        )
    def print(self):
        ops = ', '.join(op.print() for op in self.operands)
        s = f"{self.mnemonic:<8} {ops}"
        if self.comment:
            s = s + f" ; {self.comment:<10}"
        return s
