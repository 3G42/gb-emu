import sys
import struct
from collections import namedtuple
import hypothesis.strategies as st
from hypothesis import given

HEADER_START = 0x100
HEADER_END = 0x14F
HEADER_SIZE = (HEADER_END - HEADER_START) + 1

FIELDS = [
    (None, "="), # "Native" endian.
    (None, 'xxxx'), # 0x100-0x103 (entrypoint)
    (None, '48x'), # 0x104-0x133 (nintendo logo)
    ("title", '15s'), # 0x134-0x142 (cartridge title) (0x143 is shared with the cgb flag)
    ("cgb", 'B'), # 0x143 (cgb flag)
    ("new_licensee_code", 'H'), # 0x144-0x145 (new licensee code)
    ("sgb", 'B'), # 0x146 (sgb `flag)
    ("cartridge_type", 'B'), # 0x147 (cartridge type)
    ("rom_size", 'B'), # 0x148 (ROM size)
    ("ram_size", 'B'), # 0x149 (RAM size)
    ("destination_code", 'B'), # 0x14A (destination code)
    ("old_licensee_code", 'B'), # 0x14B (old licensee code)
    ("mask_rom_version", 'B'), # 0x14C (mask rom version)
    ("header_checksum", 'B'), # 0x14D (header checksum)
    ("global_checksum", 'H'), # 0x14E-0x14F (global checksum)
]

CARTRIDGE_HEADER = "".join(format_type for _, format_type in FIELDS)



@given(data=st.binary(min_size=HEADER_SIZE + HEADER_START,
        max_size=HEADER_SIZE+HEADER_START))
def test_read_cartridge_metadata_smoketest(data):
    def read(offset,count=1):
        return data[offset:offset+count+1]
    metadata = read_cartridge_metadata(data)
    assert metadata.title == read(0x135,14)
    checksum = read(0x14E,2)
    
    assert metadata.global_checksum == int.from_bytes(checksum, sys.byteorder)




CartridgeMetadata = namedtuple(
    "CartridgeMetadata",
    [field_name for field_name, _ in FIELDS if field_name is not None]
)

def read_cartridge_metadata(buffer, offset:int = 0x100):
    data = struct.unpack_from(CARTRIDGE_HEADER,buffer,offset=offset)
    return CartridgeMetadata._make(data)