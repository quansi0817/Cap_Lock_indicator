import rumps
from Quartz.CoreGraphics import CGEventSourceKeyState, kCGEventSourceStateHIDSystemState

class CapsLockIndicatorApp(rumps.App):
    def __init__(self):
        super(CapsLockIndicatorApp, self).__init__("Caps Lock")
        self.menu = ["Status"]
        self.timer = rumps.Timer(self.update_status, 1)
        self.timer.start()

    def update_status(self, _):
        caps_lock_on = CGEventSourceKeyState(kCGEventSourceStateHIDSystemState, 57)
        if caps_lock_on:
            self.title = "🟣"
            self.menu['Status'].title = "🟣"
        else:
            self.title = "⚪️"
            self.menu['Status'].title = "⚪️"

if __name__ == "__main__":
    CapsLockIndicatorApp().run()

