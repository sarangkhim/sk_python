while True:
    player = input('가위/바위/보/그만:')
    if player == '그만':
        break
    elif player == '가위':
        print('이김')
    elif player == '바위':
        print('짐')
    elif player == '보':
        print('비김')
