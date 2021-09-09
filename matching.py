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
handleinput(in1)