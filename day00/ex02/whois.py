import sys

argvLen = len(sys.argv)

if argvLen == 2:
    if not sys.argv[1].isdigit() :
        print ("ERROR")
    elif int(sys.argv[1]) == 0 :
        print('I\'am Zero.')
    elif int(sys.argv[1]) % 2 == 0 :
        print('I\'m Even.')
    elif int(sys.argv[1]) % 2 != 0:
        print('I\'am Odd.')
elif argvLen > 2:
    print ("ERROR")