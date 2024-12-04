from dataclasses import dataclass
import numpy as np



@dataclass
class Registers:
    a = np.uint8(0)
    b = np.uint8(0)
    c = np.uint8(0)
    d = np.uint8(0)
    e = np.uint8(0)
    h = np.uint8(0)
    l = np.uint8(0)
    pc = np.uint8(0)
    sp = np.uint8(0)
    m = np.uint8(0)
    t = np.uint8(0)
    f = np.uint8(0)
    
    def get_af(self) -> np.uint16:
        af = (np.uint16(self.a) << 8) | np.uint16(self.f)
        return af
    def set_af(self, value:np.uint16):
        self.a = np.uint8((value & 0xFF00) >> 8)
        self.f = np.uint8(value & 0xFF)
    def get_bc(self) -> np.uint16:
        bc = (np.uint16(self.b) << 8) | np.uint16(self.c)
        return bc
    def set_bc(self, value:np.uint16):
        self.b = np.uint8((value & 0xFF00) >> 8)
        self.c = np.uint8(value & 0xFF)
    def get_de(self) -> np.uint16:
        de = (np.uint16(self.d) << 8) | np.uint16(self.e)
        return de
    def set_de(self, value:np.uint16):
        self.d = np.uint8((value & 0xFF00) >> 8)
        self.e = np.uint8(value & 0xFF)
    def get_hl(self) -> np.uint16:
        hl = (np.uint16(self.h) << 8) | np.uint16(self.l)
        return hl
    def set_hl(self, value:np.uint16):
        self.h = np.uint8((value & 0xFF00) >> 8)
        self.l = np.uint8(value & 0xFF)
    def get_zero(self) -> bool:
        return (self.f & 0x80) != 0
    def get_subtract(self) -> bool:
        return (self.f & 0x40) != 0
    def get_half_carry(self) -> bool:
        return (self.f & 0x20) != 0
    def get_carry (self) -> bool:
        return (self.f & 0x10) != 0
    def check_f(self,value):
        if(value & 0x000F != 0):
            ValueError('O valor deve ser um byte')
            return value & 0xfff0
        return value