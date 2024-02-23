testAnsPairList = []

testStringAnsPair1 = ('''(if 
                    (> 5 (* 3 5 (/ 3 5)))
                    '() 
                    (car (cdr '(1 2 3)))
            )''', 2.0)
#2.0
testAnsPairList.append(testStringAnsPair1)

testStringAnsPair2 =('''(+ 3 5 6 
                (/ 3 6) 
                (* 7 4 (/ 1 2))
                )''' , 28.5)
#28.5
testAnsPairList.append(testStringAnsPair2)

testStringAnsPair3 =('''(apply 
                + 
                '(1 2 3 4 5)
                )
                ''' , 15)
#15
testAnsPairList.append(testStringAnsPair3)

testStringAnsPair4 =('''(eval 
                '(car (cdr '(1 2 3)))
                )
                ''', 2)
#2
testAnsPairList.append(testStringAnsPair4)

testStringAnsPair5 =( '''(cons
                 (car (cdr '(5 7 6)))
                 '(car 5 7 and)
                 )''', "'(7.0 car 5.0 7.0 and)" )
#'(7.0 car 5.0 7.0 and)
testAnsPairList.append(testStringAnsPair5)

testStringAnsPair6 = ('''(append 
                 '(1 2 3 4)
                 (cdr '(1 2 3))
                 (cons car '(6))
                 )
                ''', "'(1 2 3 4 2.0 3.0 car 6.0)")
#'(1 2 3 4 2.0 3.0 car 6.0)
testAnsPairList.append(testStringAnsPair6)

testStringAnsPair7 = ('''(map - 
                '(1 2 3 4)
                 )
                ''', "'(-1.0 -2.0 -3.0 -4.0)")
#'(-1.0 -2.0 -3.0 -4.0)
testAnsPairList.append(testStringAnsPair7)

testStringAnsPair8 = ('''1''', 1)
#1
testAnsPairList.append(testStringAnsPair8)

testStringAnsPair9 = (''''(1 2 3)''', "'(1 2 3)")
#'(1 2 3)
testAnsPairList.append(testStringAnsPair9)

testStringAnsPair10 = ('''(if
                  (null? (cdr '(1)))
                  (apply * '(1 3 23))
                  420
                  )
                ''', 69.0)
#69.0
testAnsPairList.append(testStringAnsPair10)

testStringAnsPair11 = ('''(if
                  (null? (cdr '(1 2)))
                  (apply * '(1 3 23))
                  420
                  )
                ''', 420)
#420
testAnsPairList.append(testStringAnsPair11)

testStringAnsPair12 =('''(< 
                 1
                 (length '(1 2 3))
                 )''', 1)
#1
testAnsPairList.append(testStringAnsPair12)

testStringAnsPair13 = ('''(and 1 1 (or 1 0))    
                ''', 1.0)
#1.0
testAnsPairList.append(testStringAnsPair13)
