# Window Size
WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 380

# Box und Font Size
BOX_THICKNESS = 2
BOX_SELECTION_THICKNESS = 4
FONT_SIZE = 18

#Colors
FONT_COLOR = (0, 0, 0, 255)
BOX_COLOR = (0, 0, 0)
BOX_BACKGROUND_COLOR = (255, 255, 255)
SELECTION_COLOR = (255, 0, 0)

# Distances and margines
KEYBOARD_DISTANCE = 100
BORDER_MARGIN = 20
BOTTOM_SPACING = 100

# Controller values
DEADZONE = 0.3
GESTURE_THRESHOLD = 0.8
GESTURE_WINDOW = 0.08 # Window to detect if a gesture is performed
DELAY = 0.2 # Cooldown after a possible gesture got registered
BLOCK_DURATION = 0.25 # Cooldown after a Input for continues movement

TRIGGER_WINDOW = 0.08 # Window to detect if both triggers got pushed

# Standard layouts
LEFT_KEYS = [
    ["esc", "q", "w", "e", "r", "t"],
    ["tab", "a", "s", "d", "f", "g"],
    ["ctrl", "z", "x", "c", "v", "b"]
]

RIGHT_KEYS = [
    ["y", "u", "i", "o", "p", "\\"],
    ["h", "j", "k", "l", ";", "'"],
    ["n", "m", ",", ".", "/", "alt"]
]

# Special character layouts
# TODO Add special characters and replace the dummy characters
LEFT_KEYS_SPECIAL = [
    ["-", "+", ":", ",", ".", "*"],
    ["tab", "a", "s", "d", "f", "g"],
    ["ctrl", "z", "x", "c", "v", "b"]
]

RIGHT_KEYS_SPECIAL = [
    ["´", "?", "(", ")", "{", "}"],
    ["-", "j", "k", "l", ";", "-"],
    ["-", "m", ",", ".", "/", "-"]
]
