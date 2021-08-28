# Sleep Macro to turn off display and key lights. 

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : '', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', '', False),
        (0x000000, '', '', False),
        (0x000000, '', '', False),

        # 2nd row ----------
        (0x000000, '', '', False),
        (0x000000, '', '', False),
        (0x000000, '', '', False),

        # 3rd row ----------
        (0x000000, '', '', False),
        (0x000000, '', '', False),
        (0x000000, '', '', False),

        # 4th row ----------
        (0x000000, '', '', False),
        (0x000000, '', '', False),
        (0x000000, '', '', False),
        
        # Encoder button ---
        (0x000000, '', '', False),
    ]
}
