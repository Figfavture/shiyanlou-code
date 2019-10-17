for a in range(1,100):
    if a % 7 == 0:
        print('jump7.1')
    elif a % 10 == 7:
        print('jump7.2')
    elif a // 10 == 7:
        print('jump7.3')
    else :
        print('a is:{}'.format(a))


