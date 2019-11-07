import re
import string

def print_result(length, a, b, c, d) :
    print('The text contains ' + str(length) + ' characters: ')
    print('- ' + str(a) + ' upper letters')
    print('- ' + str(b) + ' lower letters')
    print('- ' + str(c) + ' punctuation marks')
    print('- ' + str(d) + ' spaces')

def text_analyzer(*text) :
    """
      This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.  
    """
    txt = text[0]
    print(txt)
    txtLen = len(txt)
    print(txtLen)
    upperLen = 0
    lowerLen = 0
    punctuationLen = 0
    spaceLen = 0
    if txtLen == 0 :
        print("empty str")
        print_result(0, 0, 0, 0, 0)
    else :
        for c in txt :
            if c.isupper() :
                upperLen += 1
            elif c.islower() :
                lowerLen += 1
            elif c.isspace() :
                spaceLen += 1
            elif c in string.punctuation :
                punctuationLen += 1
        print_result(txtLen, upperLen, lowerLen, punctuationLen, spaceLen)


if __name__ == '__main__' :
    print ("from count import text_analyzer")
    while 1 :
        text = input()
        if re.fullmatch("^text_analyzer\(\".*\"\)$", text) :
            text_analyzer(text[15:-2])
        elif re.fullmatch("^text_analyzer\(\)$", text) :
            print('What is the text to analyse?')
            text = input()
            text_analyzer(text)
    