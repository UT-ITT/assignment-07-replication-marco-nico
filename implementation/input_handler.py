import time
import pyglet
import config

# Extend the pyglet box by more parameters
class SelectionSquare(pyglet.shapes.Box):
    def __init__(self, color, size, is_left=True):
        super().__init__(x=0, y=0, width=size, height=size,
                         thickness=config.BOX_SELECTION_THICKNESS, color=color)
        self.is_left = is_left
        self.row_idx = 0
        self.key_idx = 0
        self.blocked = False
        self.active = False
        self.vector = pyglet.math.Vec2(0, 0)
        self.input_start_time = -1

    def unblock_callback(self, dt):
        self.blocked = False

class InputHandler:
    def __init__(self, window, view):
        self.window = window
        self.view = view

        self.is_uppercase = False

        # Layout State
        self.layout_index = 0
        self.layouts = [(config.LEFT_KEYS, config.RIGHT_KEYS),
                        (config.LEFT_KEYS_SPECIAL, config.RIGHT_KEYS_SPECIAL)]

        self.selection_square_left = SelectionSquare(config.SELECTION_COLOR, self.view.box_size, is_left=True)
        self.selection_square_right = SelectionSquare(config.SELECTION_COLOR, self.view.box_size, is_left=False)

        # Set the inital stick positions
        self.set_selection_to_index(1,2,self.selection_square_left)
        self.set_selection_to_index(1,2,self.selection_square_right)

        # Controller setup
        self.controller_manager = pyglet.input.ControllerManager()
        self.active_controller = None

        # Allow hot plugging a controller
        self.controller_manager.on_connect = self.on_controller_connect
        self.controller_manager.on_disconnect = self.on_controller_disconnect

        # Inital controller setup
        initial_controllers = self.controller_manager.get_controllers()
        if initial_controllers:
            self.on_controller_connect(initial_controllers[0])

    def set_selection_to_index(self, row_idx, key_idx, selection_square):
        keyboard_pos = self.view.pos_left if selection_square.is_left else self.view.pos_right
        keys = config.LEFT_KEYS if selection_square.is_left else config.RIGHT_KEYS
        pos_x, pos_y = self.view.get_key_pos_by_index(keyboard_pos[0], keyboard_pos[1], row_idx, key_idx)
        selection_square.x = pos_x - self.view.box_half_size
        selection_square.y = pos_y - self.view.box_half_size
        selection_square.row_idx = row_idx
        selection_square.key_idx = key_idx

    def toggle_case(self):
        self.is_uppercase = not self.is_uppercase
        for label in self.view.keyboard_labels:
            if len(label.text) == 1 and label.text.isalpha():
                label.text = label.text.upper() if self.is_uppercase else label.text.lower()

    def toggle_layout(self):
        self.layout_index = (self.layout_index + 1) % len(self.layouts)
        flat_layout = [
            char for side in self.layouts[self.layout_index] for row in side for char in row
        ]
        for idx, label in enumerate(self.view.keyboard_labels):
            label.text = flat_layout[idx]

    def update_sticks(self, dt):
        self.process_stick_selection(self.selection_square_left, config.LEFT_KEYS)
        self.process_stick_selection(self.selection_square_right, config.RIGHT_KEYS)

    def process_stick_selection(self, selection_square, layout):
        if abs(selection_square.vector.x) > 0 or abs(selection_square.vector.y) > 0:
            self.check_gestures()
            elapsed_time = time.time() - selection_square.input_start_time

            if selection_square.blocked or elapsed_time < config.GESTURE_WINDOW:
                return

            if self.is_gesture_possible(self.selection_square_left.vector, self.selection_square_right.vector):
                if elapsed_time < config.DELAY:
                    return

            selection_square.active = True
            curr_row, curr_key = selection_square.row_idx, selection_square.key_idx

            if abs(selection_square.vector.x) > config.DEADZONE:
                curr_key += 1 if selection_square.vector.x > 0 else -1
                curr_key = max(0, min(curr_key, len(layout[0]) - 1))

            if abs(selection_square.vector.y) > config.DEADZONE:
                curr_row += 1 if selection_square.vector.y > 0 else -1
                curr_row = max(0, min(curr_row, len(layout) - 1))

            self.set_selection_to_index(curr_row, curr_key, selection_square)
            selection_square.blocked = True
            pyglet.clock.schedule_once(selection_square.unblock_callback, config.BLOCK_DURATION)
        else:
            selection_square.active = False
            if selection_square.blocked:
                pyglet.clock.unschedule(selection_square.unblock_callback)
                selection_square.blocked = False

    def check_gestures(self):
        if self.selection_square_left.active or self.selection_square_right.active:
            return
        # TODO Implement the requiered Gestures
        perf_gesture = False
        left_up = self.selection_square_left.vector.y < -config.GESTURE_THRESHOLD
        right_up = self.selection_square_right.vector.y < -config.GESTURE_THRESHOLD
        left_left = self.selection_square_left.vector.x < -config.GESTURE_THRESHOLD
        right_left = self.selection_square_right.vector.x < -config.GESTURE_THRESHOLD

        if left_up and right_up:
            self.toggle_layout()
            perf_gesture = True
        elif left_left and right_left:
            print("TODO both left gesture: Backspace")
            perf_gesture = True

        if perf_gesture:
            self.selection_square_left.blocked = self.selection_square_right.blocked = True
            self.selection_square_left.active = self.selection_square_right.active = True

    # A methode to check if a gesture is even possible to reduce delay
    def is_gesture_possible(self, l_vec, r_vec):
        # TODO Implement the requiered Gestures possibilities to reduce latency
        left_up = l_vec.y < -config.DEADZONE
        right_up = r_vec.y < -config.DEADZONE
        left_left = l_vec.x < -config.DEADZONE
        right_left = r_vec.x < -config.DEADZONE
        return (left_up and right_up) or (left_left and right_left)

    def register_events(self, controller_device):
        @controller_device.event
        def on_button_press(device, button):
            if button =='x':
                self.window.toggle()

            if not self.window.visible:
                return

            # TODO Add missing buttons

            if button == 'a':
                pyglet.app.exit()
            elif button in ('leftstick', 'rightstick', 'b'):
                self.toggle_case()
            #print(button)

        @controller_device.event
        def on_trigger_motion(device, trigger_name, value):
            if not self.window.visible:
                return

            # TODO Implement the trigger presses and simultanious press

            threshold = 0.5
            if trigger_name == "lefttrigger":
                if value > threshold:
                    pass

            elif trigger_name == "righttrigger":
                if value > threshold:
                    pass

        @controller_device.event
        def on_stick_motion(device, name, vec):
            if not self.window.visible:
                return

            has_x = abs(vec.x) > config.DEADZONE
            has_y = abs(vec.y) > config.DEADZONE
            x = vec.x if has_x else 0
            y = vec.y if has_y else 0

            target = self.selection_square_left if name == 'leftstick' else self.selection_square_right
            if target.input_start_time > 0 and not (has_x or has_y):
                target.input_start_time = -1
            elif target.input_start_time == -1 and (has_x or has_y):
                target.input_start_time = time.time()

            target.vector = pyglet.math.Vec2(x, -y)

    def on_controller_connect(self, new_controller):
        if self.active_controller is None:
            self.active_controller = new_controller
            self.active_controller.open()
            self.register_events(self.active_controller)
            print(f"New Controller connected: {self.active_controller.name}")

    def on_controller_disconnect(self, old_controller):
        if self.active_controller == old_controller:
            print(f"Controller disconnected: {old_controller.name}")
            self.active_controller.close()
            self.active_controller = None

            # When disconnecting a controller try to get another one
            others = self.controller_manager.get_controllers()
            if other_controllers:
                self.on_controller_connect(others[0])

