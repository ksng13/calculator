#this script is make for handle input

from test01 import check_sequence

in1='2*x^3+45*x'

def handleinput(input):
    var='x'
    varArray=[]
    operatorArray = []
    numberArray=[]
    funcArray=[]
    operators = ['+','-','*','/','^','(',')']
    resultArray = []

    array1=('@'.join(input)).split('@')

    for index,char in enumerate(array1):
        if char.isdigit():
            numberArray.append(index)
            numberArray.append(char)
        elif char==var:
            varArray.append(index)
            varArray.append(char)
        elif char in operators:
            operatorArray.append(index)
            operatorArray.append(char)
        elif char not in (operators and var) or not char.isdigit():
            funcArray.append(index)
            funcArray.append(char)



    print(operatorArray)
    print(varArray)
    print(numberArray)
    print(check_sequence(numberArray))
    return resultArray

def calcFunc(string,value):
    import os

    f = open("gen1.py", "w")
    f.write('def tinh(x):\n')
    f.write('   return %s\n'%funcHandle(string))

    f.write('print("Gia tri f(x) khi x = %d la ",tinh(%d))\n'%(value,value))
    f.close()

    os.system('py gen1.py')

def funcHandle(funcString):
    if '^' in funcString:
        newString=funcString.replace('^','**')
    else:
        newString=funcString
    return newString

def funcDerivative(funcString):
    for index, char in enumerate(funcString):
        if char =='^':
            pass

calcFunc(in1,3)