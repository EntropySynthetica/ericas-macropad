# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                     # REQUIRED dict, must be named 'app'
    'name' : 'Arrows',      # Application name
    'macros' : [            # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', '', False),
        (0x202000, '^', [Keycode.UP_ARROW], False),
        (0x000000, '', '', False),
        # 2nd row ----------
        (0x202000, '<', [Keycode.LEFT_ARROW], False),
        (0x000000, '', '', False),
        (0x202000, '>', [Keycode.RIGHT_ARROW], False),
        # 3rd row ----------
        (0x000000, '', '', False),
        (0x202000, 'v', [Keycode.DOWN_ARROW], False),
        (0x000000, '', '', False),
        # 4th row ----------
        (0x000000, '', '', False),
        (0x000000, '', '', False),
        (0x000000, '', '', False),
        # Encoder button ---
        (0x000000, '', '', False),
    ]
}
