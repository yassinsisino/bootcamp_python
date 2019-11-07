import sys
argvLen = len(sys.argv)
string = []
if  argvLen > 1 :
    for x in range(1, argvLen):
        string.insert(x, sys.argv[x]);
    string = ' '.join(string);
    string = string.swapcase();
    print (string[::-1])