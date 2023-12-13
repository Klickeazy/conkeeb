import board
import keypad
import neopixel

COLUMNS = 6
ROWS = 5

c_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0)]

pixels = neopixel.NeoPixel(board.GP8, 30, brightness=0.3)

keys = keypad.KeyMatrix(
    row_pins=(board.GP9, board.GP10, board.GP11, board.GP12, board.GP13),
    column_pins=(board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7),
    columns_to_anodes=False,
)


def key_to_pixel_map(key_number):
    row = key_number // COLUMNS
    column = (key_number % COLUMNS)
    if row % 2 == 1:
        column = COLUMNS - column - 1
    return row * COLUMNS + column


pixels.fill(c_list[0])
while True:
    key_event = keys.events.get()
    if key_event:
        print(key_event)
        if key_event.pressed:
            pixels[key_to_pixel_map(key_event.key_number)] = c_list[1]
        else:
            pixels[key_to_pixel_map(key_event.key_number)] = c_list[2]
