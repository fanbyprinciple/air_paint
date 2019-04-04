from pynput.keyboard import Key, Controller

keyboard = Controller()
i = 10000000000000000
while i:
    keyboard.press(Key.space)
    i = i -1
keyboard.release(Key.space)
print("Done")