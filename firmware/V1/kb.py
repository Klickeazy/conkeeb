import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

from kmk.modules.split import Split, SplitSide

from storage import getmount

side = str(getmount('/').label)[-1]

class KMKKeyboard(_KMKKeyboard):
    side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
    
    if side == 'L':
        col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
        row_pins = (board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)
    else:
        col_pins = (board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2)
        row_pins = (board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)
        
    rgp_pixel_pin = board.GP8
    num_pixels = 30

    diode_orientation = DiodeOrientation.COL2ROW
    # data_pin = 
    # data_pin2 =
    # rgb_pixel_pin = pins[avr['D3']]
    # num_pixels = 12

    # flake8: noqa
    # fmt: off
    
    coord_mapping = [
        0,  1,  2,  3,  4,  5,      30, 31, 32, 33, 34, 35,
        6,  7,  8,  9,  10, 11,     36, 37, 38, 39, 40, 41,
        12, 13, 14, 15, 16, 17,     42, 43, 44, 45, 46, 47,
        18, 19, 20, 21, 22, 23,     48, 49, 50, 51, 52, 53,
        24, 25, 26, 27, 28, 29,     54, 55, 56, 57, 58, 59
    ]