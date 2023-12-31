import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# from kb import data_pin
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide
from storage import getmount

from kmk.modules.layes import Layers
keyboard.modules.append(Layers())

# keyboard = KMKKeyboard()

# side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

# split = Split(split_side=SplitSide.LEFT)
# keyboard.modules.append(split)

# split = Split( # NAME DRIVES AS CIRCUITPYL and CIRCUITPYR respectively
#     split_flip=True,  # If both halves are the same, but flipped, set this True - check wiring
#     split_type=SplitType.UART,  # Defaults to UART
#     split_target_left=True,  # Assumes that left will be the one on USB. Set to False if it will be the right
#     uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
#     data_pin=board.GP1,  # The primary data pin to talk to the secondary device with
#     data_pin2=board.GP0,  # Second uart pin to allow 2 way communication
#     uart_flip=True,  # Reverses the RX and TX pins if both are provided
#     use_pio=False,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
# )


# side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT

# if side == SplitSide.RIGHT:
#     keyboard.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
#     keyboard.row_pins = (board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)
#     # keyboard.data_pin = 
#     # keyboard.diode_orientation = ...
# else:
#     keyboard.col_pins = (board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2)
#     keyboard.row_pins = (board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)

# keyboard.diode_orientation = DiodeOrientation.ROW2COL

# keyboard.col_pins = (board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2)
# keyboard.row_pins = (board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)
# keyboard.diode_orientation = DiodeOrientation.COL2ROW

# thumb-cluster on left half : Row 5, Col (0,1), Col(2,3)
# thumb-cluster on right half : Row 5, Col (0,1), Col(2,3)

# [ 0 1 2 3 4 5
#  6 7 8 9 10 11
#  12 13 14 15 16 17
#  18 19 20 21 22 23    24 25
#              28 29    26 27]

# http://kmkfw.io/docs/keycodes/

keyboard.keymap = [
    [   #0
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.GRV,
        KC.GRAVE, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSLS,
        KC.QUOTE, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.RSFT,
        KC.HOME, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RCTL,
        None, KC.LALT, KC.SPC, KC.LSHIFT, None, KC.TO(1), None, KC.FN, None, None, None, None
    ],
    [   #1 - Function Layer pass through
        KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12,
        None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None, None, None,
    ]
]


if __name__ == '__main__':
    keyboard.go()