# This setups the window and applies some hacks to bypass the pyglet window getting focused

import ctypes
import platform
import pyglet
from config import WINDOW_HEIGHT, WINDOW_WIDTH

class KeyboardWindow(pyglet.window.Window):
    def __init__(self):
        #gl_config = pyglet.gl.Config(alpha_size=8, double_buffer=True)
        super().__init__(
            WINDOW_WIDTH, WINDOW_HEIGHT,
            style=pyglet.window.Window.WINDOW_STYLE_OVERLAY, # We use WINDOW_STYLE_OVERLAY to make our keyboard a true overlay
            visible=False,
            #config=gl_config
        )

        #pyglet.gl.glClearColor(0, 0, 0, 0)
        pyglet.gl.glClearColor(255,255,255,255)

        self.apply_focus_bypass()
        self.show_window()


    # Do really want this? And does it work on windows and mac? I only tested the linux implementation
    # Apply focus-bypass rules
    def apply_focus_bypass(self):
        current_os = platform.system()

        if current_os == "Windows":
            hwnd = self._hwnd
            user32 = ctypes.windll.user32
            current_style = user32.GetWindowLongW(hwnd, -20)
            user32.SetWindowLongW(hwnd, -20, current_style | 0x08000000)

        elif current_os == "Linux":
            from pyglet.libs.x11 import xlib
            display = self.display._display
            x_window = self._window
            hints = xlib.XAllocWMHints()
            hints.contents.flags = xlib.InputHint
            hints.contents.input = 0
            xlib.XSetWMHints(display, x_window, hints)
            xlib.XFree(hints)

        elif current_os == "Darwin":
            objc = ctypes.cdll.LoadLibrary('/System/Library/Frameworks/Cocoa.framework/Cocoa')
            ns_window = self._ns_window
            objc.objc_msgSend(ns_window, objc.sel_registerName(b"setCanBecomeKeyWindow:"), False)

    @staticmethod
    def get_middle_position():
        screen = pyglet.display.get_display().get_default_screen()
        screen_width = screen.width
        screen_height = screen.height

        x_pos = int((screen_width - WINDOW_WIDTH) / 2)
        y_pos = int(screen_height - WINDOW_HEIGHT)

        return (x_pos, y_pos)

    # Positions the window in the bottom middle of the screen
    def position_window(self):
        x_pos, y_pos = self.get_middle_position()
        self.set_location(x_pos, y_pos)

    def show_window(self):
        self.set_visible(True)
        self.position_window()

    def hide_window(self):
        self.set_visible(False)

    def toggle(self):
        if self.visible:
            self.hide_window()
        else:
            self.show_window()


