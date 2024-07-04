# command = ""
started = False

while True:
    command = input('>').lower()
    if (command == 'help'):
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to end the game')

    elif (command == 'start'):
        if (started):
            print('already started !!!')
        else:
            started = True
            print('car is started..')

    elif (command == 'stop'):
        if not started:
            print('already stopped')
        else:
            started = False
            print('car is stopped')

    elif (command == 'quit'):
        print('end game')
        break
    else:
        print("i don't understand")
