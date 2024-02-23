from preParser import preParser
import math
from decimal import Decimal
from fractions import Fraction

def arithmProcessor(lst):
    if(lst[0].value == '+'):
        retVal = 0
        for i in range(1, len(lst)):
            if(type(lst[i]) == type([])):
                lstRes1 = listProcessor(lst[i])
                assert lstRes1.type == "NUMBER", "Arg %s Does Not Equate To a Number" % i
                retVal += lstRes1.value
            elif(lst[i].type == 'NUMBER'):
                retVal += lst[i].value
            else:
                print("Error, + does not take %s as an argument" % lst[i].type)
                exit()    
                
    elif(lst[0].value == '-'):
        retVal = 0

        if(type(lst[1]) == type([])):
            lstRes = listProcessor(lst[1])
            assert lstRes.type == "NUMBER", "Arg %s Does Not Equate To a Number" % i
            retVal = lstRes.value
        elif(lst[1].type == 'NUMBER'):
            retVal = lst[1].value
        else:
            print("Error, - does not take %s as an argument" % lst[i].type)
            exit() 

        if(len(lst) == 2):
            retVal = -retVal

        for i in range(2, len(lst)):
            if(type(lst[i]) == type([])):
                lstRes1 = listProcessor(lst[i])
                assert lstRes1.type == "NUMBER", "Argument %s does not get processed into a number" % i
                retVal -= lstRes1.value
            elif(lst[i].type == 'NUMBER'):
                retVal -= lst[i].value
            else:
                print("Error, - does not take %s as an argument" % lst[i].type)
                exit() 
        
    elif(lst[0].value == '*'):
        retVal = 1  

        for i in range(1, len(lst)):
            if(type(lst[i]) == type([])):
                lstRes1 = listProcessor(lst[i])
                assert lstRes1.type == "NUMBER", "Argument %s does not get processed into a number" % i
                retVal *= lstRes1.value
            elif(lst[i].type == 'NUMBER'):
                retVal *= lst[i].value
            else:
                print("Error, * does not take %s as an argument" % lst[i].type)
                exit() 

    elif(lst[0].value == '/'):
        Num = 1
        Denom = 1

        if(type(lst[1]) == type([])):
            lstRes1 = listProcessor(lst[1])
            assert lstRes1.type == "NUMBER", "Argument %s does not get processed into a number" % 1  
            Num = lstRes1.value          
        elif(lst[1].type == 'NUMBER'):
            Num = lst[1].value
        else:
            print("Error, / does not take %s as an argument" % lst[i].type)
            exit()         

        for i in range(2, len(lst)):
            if(type(lst[i]) == type([])):
                lstRes1 = listProcessor(lst[i])
                assert lstRes1.type == "NUMBER", "Argument %s does not get processed into a number" % i
                Denom *= lstRes1.value
            elif(lst[i].type == 'NUMBER'):
                Denom *= lst[i].value
            else:
                print("Error, / does not take %s as an argument" % lst[i].type)
                exit() 

        retVal = Num/Denom

    stri = "("
    stri += str(retVal)
    stri += ")"
    return preParser(stri)[0]

def logicProcessor(lst):
    if(lst[0].value == 'and'):
        retVal = 1
        for i in range(1, len(lst)):
            if(type(lst[i]) == type([])):
                lstRes1 = listProcessor(lst[i])
                assert lstRes1.type == "NUMBER", "Argument %s does not get processed into a number" % i   
                if(lstRes1.value == 0):
                    retVal = 0
            elif(lst[i].type == 'NUMBER'):
                if(lst[i].value == 0):
                    retVal = 0
            else:
                print("Error, and does not take %s as an argument" % lst[i].type)
                exit()           

    if(lst[0].value == 'or'):
        retVal = 0
        for i in range(1, len(lst)):
            if(type(lst[i]) == type([])):
                lstRes1 = listProcessor(lst[i])
                assert lstRes1.type == "NUMBER", "Argument %s does not get processed into a number" % i   
                if(lstRes1 != 0):
                    retVal = 1
            elif(lst[i].type == 'NUMBER'):
                if(lst[i].value != 0):
                    retVal = 1
            else:
                print("Error, or does not take %s as an argument" % lst[i].type)
                exit()         

    stri = "("
    stri += str(retVal)
    stri += ")"
    return preParser(stri)[0]

def lispProcessor(lst):
    if(lst[0].value == "car"):
        assert len(lst) == 2, "Car Takes 1 List as an argument"

        if(type(lst[1]) == type([])):
            lstRes = listProcessor(lst[1])
            assert lstRes.type == "LIST", "Car Takes 1 List as an argument"
            removeApostrophe = lstRes.value[1:]
            listify = preParser(removeApostrophe)
            assert len(listify) > 0, "Car Does Not Work On an Empty List"
            return listify[0]    
        elif(lst[1].type == "LIST"):
            removeApostrophe = (lst[1].value)[1:]
            listify = preParser(removeApostrophe)
            assert len(listify) > 0, "Car Does Not Work On an Empty List"
            return listify[0]
        else:
            print("Error, car does not take %s as an argument" % lst[1].type)
            exit()                    

    if(lst[0].value == "cdr"):
        assert len(lst) == 2, "cdr Takes 1 List as an argument"
        if(type(lst[1]) == type([])):
            lstRes = listProcessor(lst[1])
            assert lstRes.type == "LIST", "cdr Takes 1 List as an argument"
            removeApostrophe = lstRes.value[1:]
            listify = preParser(removeApostrophe)

            assert len(listify) > 0, "cdr Does Not Work on an empty List"
            
            listify = listify[1:]

            stri = "('("
            for i in listify:
                stri += str(i.value)
                stri += " "
            if(len(listify)!=0):
                stri = stri[0:-1]
            stri += '))'
            return preParser(stri)[0]
        elif(lst[1].type == "LIST"):
            removeApostrophe = (lst[1].value)[1:]
            listify = preParser(removeApostrophe)

            assert len(listify) > 0, "cdr Does Not Work on an empty List"

            listify = listify[1:]
            stri = "('("
            for i in listify:
                stri += str(i.value)
                stri += " "
            if(len(listify)!=0):
                stri = stri[0:-1]
            stri += '))'
            return preParser(stri)[0]
        else:
            print("Error, cdr does not take %s as an argument" % lst[1].type)
            exit()                  

    if(lst[0].value == "cons"):
        assert len(lst) == 3, "Cons takes 2 Arguments"
        
        lstCons = 0
        if(type(lst[1]) == type([])):
            lstCons = listProcessor(lst[1])
        else:
            lstCons = lst[1]
        
        lstConsed = 0
        if(type(lst[2]) == type([])):
            lstConsed = listProcessor(lst[2])
        else:
            lstConsed = lst[2]
        assert lstConsed.type == "LIST", "The Second Argument Should be a list"

        lstConsed = lstConsed.value
        removeApostrophe = (lstConsed)[1:]
        listify = preParser(removeApostrophe)

        stri = "('("
        stri += str(lstCons.value)
        stri += " "
        for i in listify:
            stri += str(i.value)
            stri += " "
        stri = stri[0:-1]
        stri += '))'

        return preParser(stri)[0]

    if(lst[0].value == "append"):
        argList = []
        for i in range(1, len(lst)):
            if(type(lst[i]) == type([])):
                arg = listProcessor(lst[i])
                assert arg.type == "LIST", "Arg %s Does not Equate to a list" % i   
                argList.append(arg.value)
            elif(lst[i].type == "LIST"):
                argList.append(lst[i].value)
            else:
                print("Error, append does not take %s as an argument" % lst[i].type)
                exit()
        elemList = []
        for i in argList:
            removeParens = i[2:-1]
            elemsi = removeParens.split(" ")
            elemList += elemsi
        
        stri = "('("
        for i in elemList:
            stri += str(i)
            stri += " "
        stri = stri[0:-1]
        stri += '))'
        return preParser(stri)[0]

    if(lst[0].value == "map"):
        assert len(lst) == 3, "Map Takes 1 Procedure and 1 List as an Argument"
        if(len(lst) == 3):
            procedure = lst[1].value
            arg = 0
            if(type(lst[2]) == type([])):
                arg = listProcessor(lst[2])
            else:
                arg = lst[2]
            assert arg.type == "LIST", "The Second Argument Must Be a LIST"
            arg = arg.value[2:-1]
            arg = arg.split(" ")

            resList = []
            for i in arg:
                stri = "("
                stri += str(procedure)
                stri += " "
                stri += str(i)
                stri += ")"
                resList.append(Parser(stri).value)

            stri = "('("
            for i in resList:
                stri += str(i)
                stri += " "
            stri = stri[0:-1]
            stri += '))'
            return preParser(stri)[0]

def helperFuncProcessor(lst):
    if(lst[0].value == "length"):
        assert len(lst) == 2, "Length Takes 1 List as an Argument"

        ans = 0
        if(type(lst[1]) == type([])):
            lstRes = listProcessor(lst[1])
            assert lstRes.type == "LIST", "Length Takes 1 List as an argument"
            lstRes = lstRes.value[2:-1]
            lstRes = lstRes.split(" ")
            ans = len(lstRes)
        elif(lst[1].type == "LIST"):
            lstRes = lst[1].value[2:-1]
            lstRes = lstRes.split(" ")
            ans = len(lstRes)
        else:
            print("Error, length does not take %s as an argument" % lst[1].type)
            exit()   
        retVal = "(" + str(ans) + ")"
        return preParser(retVal)[0]        

    if(lst[0].value == "null?"):
        assert len(lst) == 2, "null? Takes 1 List as an Argument"

        ans = 0
        if(type(lst[1]) == type([])):
            lstRes = listProcessor(lst[1])
            assert lstRes.type == "LIST", "null? Takes 1 List as an argument"
            lstRes = lstRes.value[2:-1]
            if(lstRes == ''): ans = 1
            else: ans = 0
        elif(lst[1].type == "LIST"):
            lstRes = lst[1].value[2:-1]
            if(lstRes == ''): ans = 1
            else: ans = 0
        else:
            print("Error, null? does not take %s as an argument" % lst[1].type)
            exit()   
        retVal = "(" + str(ans) + ")"
        return preParser(retVal)[0] 

def applevalProcessor(lst):
    if(lst[0].value == 'apply'):
        assert len(lst) == 3, "Apply Takes 2 Arguments, A Procedure, And A List"
        procedure = lst[1].value
        lstArg = []

        if(type(lst[2]) == type([])):
            lstRes = listProcessor(lst[2])
            assert lstRes.type == "LIST", "Apply Takes A List as the second argument"
            lstArg = lstRes.value
        elif(lst[2].type == "LIST"):
            lstArg = lst[2].value
        else:
            print("Error, apply does not take %s as an argument" % lst[2].type)
            exit()   
        ans = "(" + str(procedure) + " " + lstArg[2:]
        return Parser(ans)

    if(lst[0].value == 'eval'):
        assert len(lst) == 2, "Eval Takes 1 List As An Argument"
        
        lstArg = 0
        if(type(lst[1]) == type([])):
            lstRes = listProcessor(lst[1])
            assert lstRes.type == "LIST", "Eval Takes A List as the argument"
            lstArg = lstRes.value
        elif(lst[1].type == "LIST"):
            lstArg = lst[1].value
        else:
            print("Error, eval does not take %s as an argument" % lst[1].type)
            exit()   
        lstArg = lstArg[1:]
        return Parser(lstArg)

def ifProcessor(lst):
    assert len(lst) == 4, "If Takes 3 Arguments, The Condition, The Positive Output, And The Negative Output"
    lstRes = 0
    if(type(lst[1]) == type([])):
        lstRes = listProcessor(lst[1])
    elif(lst[1].type == "LIST"):
        s = "(eval "
        s += lst[1].value
        s += ")"
        lstRes = Parser(s)
    elif(lst[1].type == "NUMBER"):
        lstRes = lst[1]
    else:
        print("Condition Has to Evaluate To a Boolean (A Number)")
        exit()
    assert lstRes.type == "NUMBER", "The Condition Needs to Evaluate To a Boolean (A Number)"
    
    if(lstRes.value != 0):
        if(type(lst[2]) == type([])):
            lstRes = listProcessor(lst[2])
            return lstRes
        else:
            return lst[2]
    else:
        if(type(lst[3]) == type([])):
            lstRes = listProcessor(lst[3])
            return lstRes
        else:
            return lst[3]

def compProcessor(lst):
    assert(len(lst) == 3), "You Can Only Compare Two Things To Eachother"
    retVal = 0
    lstRes1 = 0
    lstRes2 = 0
    if(type(lst[1]) == type([])):
        lstRes1 = listProcessor(lst[1])
    else:
        lstRes1 = lst[1]
    if(type(lst[2]) == type([])):
        lstRes2 = listProcessor(lst[2])
    else:
        lstRes2 = lst[2]
       
    if(lst[0].value == '='):
        if(lstRes1.type == lstRes2.type and lstRes1.value == lstRes2.value):
            retVal = 1
        else:
            retVal = 0
    if(lst[0].value == '>'):
        assert lstRes1.type == "NUMBER" and lstRes2.type == "NUMBER", "The Arguments have to be Numbers"
        if(lstRes1.value > lstRes2.value):
            retVal = 1
        else:
            retVal = 0
    if(lst[0].value == '<'):  
        assert lstRes1.type == "NUMBER" and lstRes2.type == "NUMBER", "The Arguments have to be Numbers"
        if(lstRes1.value < lstRes2.value):
            retVal = 1
        else:
            retVal = 0        

    stri = "("
    stri += str(retVal)
    stri += ")"
    return preParser(stri)[0]

def listProcessor(lst):

    if(lst[0].type == 'ARITHMETIC'):
        return arithmProcessor(lst)
    
    if(lst[0].type == 'LOGIC'):
        return logicProcessor(lst)

    if(lst[0].type == 'LISP'):
        return lispProcessor(lst)
    
    if(lst[0].type == 'HELPERFUNC'):
        return helperFuncProcessor(lst)

    if(lst[0].type == 'APPLEVAL'):
        return applevalProcessor(lst)

    if(lst[0].type == 'IF'):
        return ifProcessor(lst)
    
    if(lst[0].type == 'COMP'):
        return compProcessor(lst)
    
def Parser(data):
    if(data[0] != '('):
        st = '(' + data + ')'
        stt = preParser(st)
        return stt[0]

    nestedList = preParser(data)
    if(type(nestedList) == type(())):
        nestedList = nestedList[0]
        cnt = (nestedList[1].value).count('(')
        for i in range(0, cnt - 1):
            nestedList[1].value += ")"
    processedList =  listProcessor(nestedList)

    return processedList

if __name__ == '__main__':
    data = '''(and 1 1 (or 1 0))    
                '''
    print(preParser(data))
    print(Parser(data))
