from Parser import Parser
from Tests import *

def SchemeInterpreter(data):
    return Parser(data).value

def tester(testAndAnsPairList):
    coun = 1
    for i in testAndAnsPairList:
        if(SchemeInterpreter(i[0]) == i[1]):
            print("Test %s Passed" % coun)
        coun += 1

tester(testAnsPairList)