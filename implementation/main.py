import pyglet
from pynput import keyboard

# Import all the modules
from window_setup import KeyboardWindow
from keyboard_view import KeyboardView
from input_handler import InputHandler

window = KeyboardWindow()
view = KeyboardView()
inputs = InputHandler(window, view)

# Close the overlay on alt+q using global hotkeys
hotkeys = keyboard.GlobalHotKeys({
    '<alt>+q': pyglet.app.exit
})
hotkeys.start()

# Schedule the joystick update loop
pyglet.clock.schedule_interval(inputs.update_sticks, 1 / 120.0)

@window.event
def on_draw():
    window.clear()

    view.bg_layer.draw()
    inputs.selection_square_left.draw()
    inputs.selection_square_right.draw()
    view.text_layer.draw()

pyglet.app.run()
