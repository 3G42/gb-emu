from pyboy import PyBoy

print('start')
pyboy = PyBoy('gb/snake.gb')
while pyboy.tick():
    pass
pyboy.stop()