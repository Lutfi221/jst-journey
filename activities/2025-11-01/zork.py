print('1. Go into house (LOCKED) 2. Look around')
ans = input('>')
ans = int(ans)
hands = ''
while True:
    print('1. Go into house (LOCKED) 2. Look around')
    ans = input('>')
    ans = int(ans)
    if ans == 1:
        if hands != 'key':
            print('Cannot open the door')
        elif hands == 'key':
            print('Opens the door')
    if ans == 2:
        if hands != 'key':
            print('You look around, and finds a key. You take the key')
            hands = 'key'
        elif hands =='key':
            print('There is nothing more to see')