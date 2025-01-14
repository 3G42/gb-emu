import json
from pathlib import Path

from cpu.classes import Instruction, Operand




def load_opcodes(opcode_file):
    print(opcode_file)
    f = open(opcode_file)

    data = json.load(f)
    print("")
    prefixed = dict()
    regular = dict()
    for key, v in data["cbprefixed"].items():
        
        ops = []
        if len(v['operands']) > 0:
            for o in v['operands']:
                ops.append(
                    Operand(
                        immediate=o['immediate'],
                        name=o['name'],
                        bytes=o['bytes'] if 'bytes' in o else None,
                        adjust=o['adjust'] if 'adjust' in o else None,
                    ).create(value = o['value'] if 'value' in o and 'bytes' in o and o['bytes']>0 else None)
                )
        prefixed[int(key,0)] = Instruction(
            bytes=v['bytes'],
            opcode=int(key,0),
            immediate=v['immediate'],
            cycles=v['cycles'],
            mnemonic=v['mnemonic'],
            comment=v['comment'] if 'comment' in v else None,
            flags=v['flags'],
        ).create(ops)
    for key, v in data["unprefixed"].items():
        ops = []
        if len(v['operands']) > 0:
            for o in v['operands']:
                ops.append(
                    Operand(
                        immediate=o['immediate'],
                        name=o['name'],
                        bytes=o['bytes'] if 'bytes' in o else None,
                        adjust=o['adjust'] if 'adjust' in o else None,
                    ).create(value = o['value'] if 'value' in o and 'bytes' in o and o['bytes']>0 else None)
                )
        regular[int(key,0)] = Instruction(
            bytes=v['bytes'],
            opcode=int(key,0),
            immediate=v['immediate'],
            cycles=v['cycles'],
            mnemonic=v['mnemonic'],
            comment=v['comment'] if 'comment' in v else None,
            flags=v['flags'],
        ).create(ops)

    f.close()
    
    return prefixed,regular


