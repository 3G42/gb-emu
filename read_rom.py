from pathlib import Path

from gb.cartridge_reader import read_cartridge_metadata




p = Path('snake.gb')
text = read_cartridge_metadata(p.read_bytes())

print(text)