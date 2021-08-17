# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values
from adafruit_hid.consumer_control import ConsumerControl # REQUIRED if using ConsumerControlCode.* values
from adafruit_hid.consumer_control_code import ConsumerControlCode # REQUIRED if using ConsumerControlCode.* values


app = {                         # REQUIRED dict, must be named 'app'
    'name' : 'Multimedia',      # Application name
    'macros' : [                # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x101010, 'Prev', [ConsumerControlCode.SCAN_PREVIOUS_TRACK], True),
        (0x004000, 'Play', [ConsumerControlCode.PLAY_PAUSE], True),
        (0x101010, 'Next', [ConsumerControlCode.SCAN_NEXT_TRACK], True),

        # 2nd row ----------
        (0x000040, 'Vol -', [ConsumerControlCode.VOLUME_DECREMENT], True),
        (0x000000, '', '', False),
        (0x000040, 'Vol +', [ConsumerControlCode.VOLUME_INCREMENT], True),

        # 3rd row ----------
        (0x000000, '', '', False),
        (0x000000, '', '', False),
        (0x000000, '', '', False),

        # 4th row ----------
        (0x000000, '', '', False),
        (0x000000, '', '', False),
        (0x000000, '', '', False),

        # Encoder button ---
        (0x000000, '', '', False)
    ]
}
