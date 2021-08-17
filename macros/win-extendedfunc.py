# For extended hotkeys F13 to F24

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                           # REQUIRED dict, must be named 'app'
    'name' : 'Extra Functions',   # Application name
    'macros' : [                  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000040, 'F13', [Keycode.F13], False),
        (0x000040, 'F14', [Keycode.F14], False),
        (0x000040, 'F15', [Keycode.F15], False),

        # 2nd row ----------
        (0x000040, 'F16', [Keycode.F16], False),
        (0x000040, 'F17', [Keycode.F17], False),
        (0x000040, 'F18', [Keycode.F18], False),

        # 3rd row ----------
        (0x000040, 'F19', [Keycode.F19], False),
        (0x000040, 'F20', [Keycode.F20], False),
        (0x000040, 'F21', [Keycode.F21], False),

        # 4th row ----------
        (0x000040, 'F22', [Keycode.F22], False),
        (0x000040, 'F23', [Keycode.F23], False),
        (0x000040, 'F24', [Keycode.F24], False),

        # Encoder button ---
        (0x000000, '', [''], False)
    ]
}
