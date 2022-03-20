from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout


def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard.unbind(on_key_up=self.on_keyboard_up)
    self._keyboard = None

def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'left':
        self.current_speed_x = self.SPEED_X
    elif keycode[1] == 'right':
        self.current_speed_x = -self.SPEED_X
    elif keycode[1] == 'up':
        self.current_speed_y = self.SPEED_Y * 2
    elif (keycode[1] == 'spacebar' or keycode[1] == 'enter') and self.menu_widget.opacity == 1:
        self.on_menu_button_pressed()
    elif keycode[1] == 'escape':
        Window.close()
    return True

def on_keyboard_up(self, keyboard, keycode):
    self.current_speed_x = 0
    if keycode[1] == 'up':
        self.current_speed_y = self.SPEED_Y
    return True

def on_touch_down(self, touch):
    if self.state_game_has_started and not self.state_game_over:
        if touch.x < self.width / 2:
            self.current_speed_x = self.SPEED_X
        else:
            self.current_speed_x = -self.SPEED_X
    return super(RelativeLayout, self).on_touch_down(touch)


def on_touch_up(self, touch):
    self.current_speed_x = 0