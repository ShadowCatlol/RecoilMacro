from pynput.mouse import Listener, Button, Controller
import pyautogui, threading, keyboard, win32api, win32con, ctypes, math, time, json, sys, os
from multiprocessing import Queue
from termcolor import cprint
    
os.system("")


class Main(Controller):
    def __init__(self):
        self.mouse_down = False
        self.toggle = True
        self.on_primary = True

        self.mouse = super()
        self.clicks = 0
        self.count = 0
        self.config_queue = Queue()

        self.load_config()

        threads = 1 + self.clicks_per_second // 65
        for _ in range(threads):
            threading.Thread(target=self.spam).start()

        threading.Thread(target=self.update_config).start()
        threading.Thread(target=self.title).start()

        keyboard.on_press(callback=self.listen)

        with Listener(on_click=self.on_click) as listener:
            listener.join()

    def log(self, text, message_type=None):
        if message_type == "error":
            text = f"[ERROR] {text}"
            cprint(text, "red")

        elif message_type == None:
            text = f"[LOG] {text}"
            print(text)

        else:
            text = f"[LOG] {text}"
            cprint(text, color)

    def load_config(self):
        try:
            config = json.load(open("config.json", "r+"))
        except FileNotFoundError as e:
            self.log("Cant find 'config.json' file, make sure its in the same directory", "error")
            self.log(e, "error")
            os.system("PAUSE")
            sys.exit(1)

        except json.JSONDecodeError as e:
            self.log("The data inside your 'config.json' file is not in proper json format.", "error")
            self.log("Check if you forgot a comma or quote at the end of a line", "error")
            self.log(e, "error")
            os.system("PAUSE")
            sys.exit(1)

        try:
            self.pulldown = bool(config['pulldown'])
            self.hold = bool(config['hold_mouse_down'])
            self.toggle_key = str(config['toggle_key'])
            self.clicks_per_second = int(config['clicks_per_second'])
            self.primary_pulldown_rate = float(config['primary_pulldown_rate'])
            self.secondary_pulldown_rate = float(config['secondary_pulldown_rate'])
            self.configs = dict(config['configs'])
        except ValueError as v:
            self.log(f"Invalid input: {v}", "error")

        self.pulldown_rate = float(self.primary_pulldown_rate)

    def update_config(self):
        while True:
            self.config_queue.get()
            config = {
                "pulldown": self.pulldown,
                "hold_mouse_down": self.hold, 
                "toggle_key": self.toggle_key, 
                "clicks_per_second": self.clicks_per_second, 
                "primary_pulldown_rate": round(self.pulldown_rate if self.on_primary else self.primary_pulldown_rate, 2),
                "secondary_pulldown_rate": round(self.pulldown_rate if not self.on_primary else self.secondary_pulldown_rate, 2),
                "configs": self.configs
            }

            try:
                with open("config.json", "w+") as file:
                    json.dump(config, file, indent=4)
            except Exception as e:
                self.log("Failed to update 'config.json' file", "error")
                self.log(e, "error")

    def title(self):
        while True:
            old = int(self.count)
            time.sleep(1)
            speed = self.count-old
            os.system(f'TITLE {speed}/s clicks per second, Pulldown rate: {round(self.pulldown_rate, 2)}')

    def click(self):
        self.clicks += 1
        self.mouse.press(Button.left)
        self.mouse.release(Button.left)

    def spam(self):
        while True:
            if self.mouse_down and self.toggle:
                self.count += 1
                threading.Thread(target=self.click).start()

                pulldown_rate = (self.pulldown_rate * 130) // self.clicks_per_second

                if self.pulldown_rate > 1:
                    extra = round(self.pulldown_rate - 1)
                    every_nth = 1
                else:
                    every_nth = int(1 // self.pulldown_rate)
                    extra = 0

                if not self.count % every_nth and self.pulldown:
                    threading.Thread(target=win32api.mouse_event, args=(win32con.MOUSEEVENTF_MOVE, 0, 1 + extra, 0, 0)).start()

                if not self.count % (every_nth * 15) and self.pulldown:
                    threading.Thread(target=win32api.mouse_event, args=(win32con.MOUSEEVENTF_MOVE, -(1 + extra), 0, 0, 0)).start()

            time.sleep(1/self.clicks_per_second)

    def listen(self, event):
        key = {
            True: "on",
            False: "off"
        }

        key_pressed = event.name.lower()

        if key_pressed == self.toggle_key:
            self.toggle = not self.toggle
            self.log(f"Toggled {key[self.toggle]}")

        if key_pressed in self.configs:
            self.pulldown_rate = self.configs[key_pressed]

        elif key_pressed == "-":
            self.pulldown_rate -= 0.001

        elif key_pressed == "=":
            self.pulldown_rate += 0.001
            
        elif key_pressed == "1":
            self.pulldown_rate = float(self.primary_pulldown_rate)
            self.on_primary = True

        elif key_pressed == "2":
            self.pulldown_rate = float(self.secondary_pulldown_rate)
            self.on_primary = False

        if key_pressed in ['-', '=']:
            if self.on_primary:
                self.pulldown_rate = float(self.pulldown_rate)

            else:
                self.secondary_pulldown_rate = float(self.pulldown_rate)

            self.config_queue.put(None)

    def on_click(self, x, y, button, pressed):
        if not button == Button.left:
            return
            
        if self.clicks: 
            if not pressed: 
                self.clicks -= 1
            return

        if self.hold:
            self.mouse_down = pressed
        elif pressed:
            self.mouse_down = not self.mouse_down

if __name__ == "__main__":
    Main()