# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Linux Firefox', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.CONTROL, '['], False),
        (0x004000, 'Fwd >', [Keycode.CONTROL, ']'], False),
        (0x400000, 'Up', [Keycode.SHIFT, ' '], False),      # Scroll up

        # 2nd row ----------
        (0x202000, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB], False),
        (0x202000, 'Tab >', [Keycode.CONTROL, Keycode.TAB], False),
        (0x400000, 'Down', ' ', False),                     # Scroll down

        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.CONTROL, 'r'], False),
        (0x000040, 'Home', [Keycode.CONTROL, 'h'], False),
        (0x000040, 'Private', [Keycode.CONTROL, Keycode.SHIFT, 'p'], False),

        # 4th row ----------
        (0x101010, 'Ada', [Keycode.CONTROL, 't', -Keycode.CONTROL, 'www.adafruit.com\n'], False),   # adafruit.com in a new tab
        (0x000040, 'Dev Mode', [Keycode.F12], False),    # dev mode
        (0x101010, 'Digi', [Keycode.CONTROL, 't', -Keycode.CONTROL, 'digikey.com\n'], False), # digikey in a new tab

        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w'], False) # Close window/tab
    ]
}
