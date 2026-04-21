from pynput import keyboard
from pynput.keyboard import Controller

current_text = ""
pointer = 0

def on_press(key):
    global current_text, pointer

    match key:
        case keyboard.Key.enter | keyboard.Key.space:
            print("space")
            current_text = ""
            return
    
    if key == keyboard.Key.backspace:
        print("backspace")
        current_text = current_text[0:-1]
        return
    
    if key == keyboard.Key.left:
        print("left")
        pointer -= 1
        return
    
    if key == keyboard.Key.right:
        print("right")
        if pointer < 0:
            pointer += 1
        return

    if hasattr(key, 'char') and key.char is not None:
        print(f"key pressed: {key.char}")

        if key.char == "=":
            print(current_text)
            sum = ""
            try:
                sum = str(eval(current_text))
                print(sum)
                cont = Controller()
                cont.type(sum)
            except Exception as e:
                print(e)
            current_text = sum
            return

        print("before:")
        print(current_text)
        print(f"pointer: {pointer}")
        current_text = current_text[:pointer] + key.char + current_text[pointer:]

        # current_text+=key.char

    else:
        print(f"key pressed: {key}")

if __name__ == "__main__":
    print("CalcKeyBoard Started")
    listener = keyboard.Listener(on_press=on_press)
    # start the listener, thread is handeled by pynput
    listener.start()
    while True:
        pass