from kb import KMKKeyboard
import board

from kmk.keys import KC

from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType, SplitSide
from kmk.extensions.RGB import RGB
from storage import getmount

keyboard = KMKKeyboard()

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
print(side)

layers = Layers()

split = Split(
    split_flip=False,  # If both halves are the same, but flipped, set this True
    split_side=side,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    split_target_left=True,  # Assumes that left will be the one on USB. Set to False if it will be the right
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP0,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP1,  # Second uart pin to allow 2 way communication
    uart_flip=True,  # Reverses the RX and TX pins if both are provided
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)


rgb = RGB(pixel_pin=keyboard.led_pin, num_pixels=keyboard.led_count)

keyboard.modules = [layers, split]
# keyboard.modules = [layers]

keyboard.extensions.append(rgb)

keyboard.keymap = [
    [   #0
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.GRV,
        KC.GRAVE, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSLS,
        KC.QUOTE, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.RSFT,
        KC.HOME, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RCTL,
        KC.NO, KC.LALT, KC.SPC, KC.LSHIFT, KC.NO, KC.TO(1), KC.NO, KC.TO(1), KC.NO, KC.NO, KC.NO, KC.NO
    ],
    [   #1 - Function Layer pass through
        KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()