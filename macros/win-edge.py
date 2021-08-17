# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Windows Edge', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.ALT, Keycode.LEFT_ARROW], False),
        (0x004000, 'Fwd >', [Keycode.ALT, Keycode.RIGHT_ARROW], False),
        (0x400000, 'Up', [Keycode.SHIFT, ' '], False),      # Scroll up

        # 2nd row ----------
        (0x202000, '- Size', [Keycode.CONTROL, Keycode.KEYPAD_MINUS], False),
        (0x202000, 'Size +', [Keycode.CONTROL, Keycode.KEYPAD_PLUS], False),
        (0x400000, 'Down', ' ', False),                     # Scroll down

        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.CONTROL, 'r'], False),
        (0x000040, 'Home', [Keycode.ALT, Keycode.HOME], False),
        (0x000040, 'Private', [Keycode.CONTROL, 'N'], False),

        # 4th row ----------
        (0x000000, 'Ada', [Keycode.CONTROL, 'n', -Keycode.COMMAND, 'www.adafruit.com\n'], False),   # Adafruit in new window
        (0x800000, 'Digi', [Keycode.CONTROL, 'n', -Keycode.COMMAND, 'www.digikey.com\n'], False),   # Digi-Key in new window
        (0x101010, 'Hacks', [Keycode.CONTROL, 'n', -Keycode.COMMAND, 'www.hackaday.com\n'], False), # Hack-a-Day in new win
        
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w'], False) # Close tab
    ]
}
