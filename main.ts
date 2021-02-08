let 骰子 = 0
input.onGesture(Gesture.Shake, function () {
    骰子 = randint(1, 6)
    basic.showNumber(骰子)
    basic.pause(1000)
    basic.clearScreen()
})
