from schemeLexer import schemeLexer

##Turns the Tokenized data into a list
def _lexerToList(data):

    listToBeParsed = []
    lexer = schemeLexer()
    for tok in lexer.tokenize(data):
        listToBeParsed.append(tok)
    listToBeParsed = listToBeParsed[1:len(listToBeParsed)-1]
    return listToBeParsed

def _nestListHelper(lexList, startIndex, finalIndex):
    index = startIndex
    retVal = []

    while(index <= finalIndex):
        if(lexList[index].type == 'LPAREN'):
            index += 1
            inRetVal, index = _nestListHelper(lexList, index, finalIndex)
            retVal.append(inRetVal)
        elif(lexList[index].type == 'RPAREN'):
            index += 1
            return retVal, index
        else: 
            retVal.append(lexList[index])
            index += 1
    return retVal

##Using the parentheses inside of the aforementioned list
##Turns the list into a nested list that will be parsed
##later
def _nestList(lexList):
    return _nestListHelper(lexList, 0, len(lexList) - 1)

def _lexerToNestedList(data):
    list1 = _lexerToList(data)
    list2 = _nestList(list1)
    return list2

##Wrapper for ALLDAT
def preParser(data):
    return _lexerToNestedList(data)

##Test for me
if __name__ == '__main__':
    data = "(car '(1 2 3))"
    nestList = _lexerToNestedList(data)
    print(nestList)
    lst = [1, 2, 3, 4]
    lst2 = lst[1:]
    lst2[0] = '*'
    print(lst2)
    print(type(0))
    