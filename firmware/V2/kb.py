import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

from storage import getmount

class KMKKeyboard(_KMKKeyboard):
    
    split_check = str(getmount('/').label)[-1]
    
    if split_check == 'L':
        col_pins = (board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2)
    else:
        col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)

    row_pins = (board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)

    diode_orientation = DiodeOrientation.ROW2COL

    led_pin = board.GP8
    led_count = 30

    data_pin_TX = board.GP0
    data_pin_RX = board.GP1
    
    coord_mapping = [
        0,  1,  2,  3,  4,  5,      30, 31, 32, 33, 34, 35,
        6,  7,  8,  9,  10, 11,     36, 37, 38, 39, 40, 41,
        12, 13, 14, 15, 16, 17,     42, 43, 44, 45, 46, 47,
        18, 19, 20, 21, 22, 23,     48, 49, 50, 51, 52, 53,
        24, 25, 26, 27, 28, 29,     54, 55, 56, 57, 58, 59
    ]
