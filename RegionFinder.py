import mouse

list = [0, 0, 0]

def downCallback():
    xValOld, yValOld = mouse.get_position()
    list[0] = xValOld
    list[1] = yValOld
    # print(xValOld ,' ', yValOld, ' pressed')

def upCallback():
    xVal, yVal = mouse.get_position()
    # print(xVal ,' ', yVal, ' released')
    # print(list)
    # print('\b' * list[2], end='', flush=True)
    printString = '({0}, {1}, {2}, {3})'.format(list[0], list[1], xVal-list[0], yVal-list[1])
    list[2] = len(printString)
    print(printString)

mouse.on_button(downCallback,(), mouse.LEFT, mouse.DOWN)

mouse.on_button(upCallback,(), mouse.LEFT, mouse.UP)

# while True:
#     x, y = mouse.get_position()
#     positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#     print(positionStr, end='')
#     print('\b' * len(positionStr), end='', flush=True)


mouse.wait(button=None,target_types=None)


