import pyglet
import config

class KeyboardView:
    def __init__(self):
        self.bg_layer = pyglet.graphics.Batch()
        self.text_layer = pyglet.graphics.Batch()

        self.keyboard_elements = []
        self.keyboard_labels = []
        self.info_labels = []

        self.box_size = self.get_box_size()
        self.box_half_size = self.box_size * 0.5

        # Get positions for the keyboard halfes
        self.pos_left, self.pos_right = self.get_keyboard_positions()

        # Draw both halfes
        self.draw_keyboard_half(config.LEFT_KEYS, self.pos_left[0], self.pos_left[1])
        self.draw_keyboard_half(config.RIGHT_KEYS, self.pos_right[0], self.pos_right[1])

        # Setup the labels
        self.text_y = self.get_space_below_keyboard()
        self.create_info_labels()

    @staticmethod
    def get_box_size():
        num_rows = max(len(config.LEFT_KEYS), len(config.RIGHT_KEYS))
        max_height_size = (config.WINDOW_HEIGHT - config.BORDER_MARGIN - config.BOTTOM_SPACING + (num_rows - 1) * config.BOX_THICKNESS) / num_rows

        cols_left = len(max(config.LEFT_KEYS, key=len))
        cols_right = len(max(config.RIGHT_KEYS, key=len))
        total_cols = cols_left + cols_right

        if config.KEYBOARD_DISTANCE == 0:
            max_width_size = (config.WINDOW_WIDTH - (2 * config.BORDER_MARGIN) + (total_cols - 1) * config.BOX_THICKNESS) / total_cols
        else:
            max_width_size = (config.WINDOW_WIDTH - (2 * config.BORDER_MARGIN) - config.KEYBOARD_DISTANCE - 2 * config.BOX_THICKNESS) / total_cols + config.BOX_THICKNESS

        return min(max_height_size, max_width_size)

    def get_key_pos_by_index(self, pos_keyboard_x, pos_keyboard_y, row_idx, key_idx):
        pos_x = pos_keyboard_x + (self.box_size - config.BOX_THICKNESS) * key_idx
        pos_y = pos_y = pos_keyboard_y - (self.box_size - config.BOX_THICKNESS) * row_idx
        return (pos_x, pos_y)

    def draw_key(self, text,x,y):
        label = pyglet.text.Label(text,
                                font_name='Times New Roman',
                                font_size=config.FONT_SIZE,
                                x=x, y=y,
                                anchor_x='center', anchor_y='center',
                                color=config.FONT_COLOR,
                                batch=self.text_layer)
        label.base_text = text
        key_bg = pyglet.shapes.Rectangle(x=(x - self.box_half_size),
                                y=(y - self.box_half_size),
                                width=self.box_size,
                                height=self.box_size,
                                color=config.BOX_BACKGROUND_COLOR,
                                batch=self.bg_layer)
        outline = pyglet.shapes.Box(x=(x - self.box_half_size),
                                y=(y - self.box_half_size),
                                width=self.box_size,
                                height=self.box_size,
                                thickness=config.BOX_THICKNESS,
                                color=config.BOX_COLOR,
                                batch=self.bg_layer)
        # Add them to a list to prevent the garbage collector of deleting them
        self.keyboard_labels.append(label)
        self.keyboard_elements.append(key_bg)
        self.keyboard_elements.append(outline)

    def draw_keyboard_half(self, keys,x,y):
        for row_idx, row in enumerate(keys):
            for key_idx, key in enumerate(row):
                pos_x, pos_y = self.get_key_pos_by_index(x, y, row_idx, key_idx)
                self.draw_key(key, pos_x, pos_y)

    def get_keyboard_positions(self):
        num_rows = max(len(config.LEFT_KEYS), len(config.RIGHT_KEYS))

        cols_left = len(max(config.LEFT_KEYS, key=len))
        cols_right = len(max(config.RIGHT_KEYS, key=len))

        width_left = cols_left * self.box_size - (cols_left - 1) * config.BOX_THICKNESS
        width_right = cols_right * self.box_size - (cols_right - 1) * config.BOX_THICKNESS

        total_keyboard_width = width_left + config.KEYBOARD_DISTANCE + width_right

        start_x = (config.WINDOW_WIDTH - total_keyboard_width) / 2

        pos_keyboard_left_x = start_x + self.box_half_size
        pos_keyboard_right_x = pos_keyboard_left_x + width_left + config.KEYBOARD_DISTANCE - (config.BOX_THICKNESS if config.KEYBOARD_DISTANCE == 0 else 0)

        pos_keyboard_y = config.WINDOW_HEIGHT - self.box_half_size - config.BORDER_MARGIN

        pos_keyboard_left = (pos_keyboard_left_x, pos_keyboard_y)
        pos_keyboard_right = (pos_keyboard_right_x, pos_keyboard_y)
        return (pos_keyboard_left, pos_keyboard_right)

    def get_space_below_keyboard(self):
        num_rows = max(len(config.LEFT_KEYS), len(config.RIGHT_KEYS))

        keyboard_height = num_rows * self.box_size - (num_rows - 1) * config.BOX_THICKNESS

        bottom_y = config.WINDOW_HEIGHT - config.BORDER_MARGIN - keyboard_height

        return bottom_y

    def create_info_labels(self):
        labels_info = [
            ("space: LT + RT", 20, -40),
            ("shift: L3 or R3", 20, -80),
            ("backspace: ← + ←", 320, -40),
            ("special characters: ↑ + ↑", 320, -80),
            ("enter: Y", 620, -80),
            ("toggle overlay: X", 620, -40),
            ("exit: B / ALT + Q", 850, -40)
            
        ]

        for text, offset_x, offset_y in labels_info:
            lbl = pyglet.text.Label(text,
                                    font_name='Times New Roman',
                                    font_size=config.FONT_SIZE,
                                    x=offset_x, y=self.text_y + offset_y,
                                    anchor_x='left', anchor_y='center',
                                    color=config.FONT_COLOR,
                                    batch=self.text_layer)
            self.info_labels.append(lbl)

