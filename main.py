骰子 = 0

def on_gesture_shake():
    global 骰子
    骰子 = randint(1, 6)
    basic.show_number(骰子)
    basic.pause(1000)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
