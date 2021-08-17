# For extended hotkeys F13 to F24

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                           # REQUIRED dict, must be named 'app'
    'name' : 'Extra Functions',   # Application name
    'macros' : [                  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'F13', [Keycode.F13]),
        (0x000040, 'F14', [Keycode.F14]),
        (0x000040, 'F15', [Keycode.F15]),

        # 2nd row ----------
        (0x000040, 'F16', [Keycode.F16]),
        (0x000040, 'F17', [Keycode.F17]),
        (0x000040, 'F18', [Keycode.F18]),

        # 3rd row ----------
        (0x000040, 'F19', [Keycode.F19]),
        (0x000040, 'F20', [Keycode.F20]),
        (0x000040, 'F21', [Keycode.F21]),

        # 4th row ----------
        (0x000040, 'F22', [Keycode.F22]),
        (0x000040, 'F23', [Keycode.F23]),
        (0x000040, 'F24', [Keycode.F24]),

        # Encoder button ---
        (0x000000, '', [''])
    ]
}
