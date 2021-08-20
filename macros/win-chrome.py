# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Chrome Browser', # Application name
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
        (0x000040, 'Incog', [Keycode.CONTROL, 'N'], False),

        # 4th row ----------
        (0x101010, 'Dev Tools', [Keycode.F12], False),
        (0x000000, '', '', False),
        (0x101010, 'Weather', [Keycode.CONTROL, 'n', -Keycode.COMMAND, 'www.weather.gov/fgf/\n'], False), # weather in a new window
        
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w'], False) # Close tab
    ]
}
