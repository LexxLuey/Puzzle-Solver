puzzle = [['P','G','T','H','S','S','M','A','L','L','F','O','R','W','A','R','D','J'],
['U','N','T','T','O','N','H','E','I','R','N','B','T','M','V','E','E','W'],
['Y','I','D','R','H','O','O','N','G','C','E','U','E','T','I','R','S','O'],
['A','S','R','O','U','R','P','I','O','N','O','B','S','N','S','R','L','R'],
['L','S','A','U','P','O','E','A','T','E','I','C','O','E','C','O','A','H'],
['R','A','U','T','O','R','C','E','M','U','O','L','Y','U','O','H','M','T'],
['E','P','G','O','I','H','O','I','P','R','T','F','B','G','N','D','D','E'],
['Y','B','G','F','N','R','T','V','E','O','A','I','N','B','R','D','U','E'],
['A','T','N','B','T','S','E','B','E','S','I','I','T','A','I','M','N','R'],
['L','S','I','O','S','K','O','T','N','R','L','N','W','S','A','R','K','F'],
['P','I','T','U','E','A','T','E','R','E','T','R','T','E','B','B','D','S'],
['B','S','O','N','R','A','A','T','V','A','O','I','T','E','L','U','H','L'],
['L','S','O','D','W','K','E','A','A','F','U','S','M','J','R','O','S','A'],
['O','A','H','S','E','K','R','F','R','M','E','Q','R','E','T','N','E','C'],
['C','L','S','R','S','T','O','E','B','A','C','K','B','O','A','R','D','S'],
['K','L','S','A','N','U','W','G','A','M','E','M','I','T','F','L','A','H'],
['A','A','B','C','L','O','C','K','I','R','E','F','E','R','E','E','S','M'],
['I','B','T','H','P','T','E','N','D','R','A','U','G','T','N','I','O','P'],]

tableLength = 18
tableHeight = 18



puzzlewordForward = []
puzzlewordDownForward = []
puzzlewordDown = []
puzzlewordDownBackward = []
puzzlewordBackward = []
puzzlewordUpBackward = []
puzzlewordUp = []
puzzlewordUpForward = []

puzzlewordPositionsForward = []
puzzlewordPositionsDownForward = []
puzzlewordPositionsDown = []
puzzlewordPositionsDownBackward = []
puzzlewordPositionsBackward = []
puzzlewordPositionsUpBackward = []
puzzlewordPositionsUp = []
puzzlewordPositionsUpForward = []



def displayTable():
	for row in range(0,18):
		for column in range(0,18):
			print(puzzle[row][column], end='      ')

			if column == 17:
				print('\n')

def displayResultTable(positions):
	for row in range(0,18):
		for column in range(0,18):
			puzzle[row][column] = '0'
			print(puzzle[row][column], end='      ')
			if row == positions[0][0] and column == positions[0][1]:
				print(puzzle[row][column], end='      ')
				

#displayTable()

word = str(input("Enter the word to search for in UPPERCASE: "))



def checkforward(Word):
        wordFound = ''
        for row in range(0, tableHeight):
                if wordFound == Word:
                        break
                else:
                        #print("Row: ", row," tableHeight: ", tableHeight)
                        for column in range(0, tableLength):
                                #print("Column: ", column," tableLength: ", tableHeight)
                                if puzzle[row][column] == Word[0]:
                                        #print("puzzle: ",row,"",column," == word 0: ",Word[0])
                                        #print("puzzle [",row,"][",column,"] = ",puzzle[row][column],"|| word[0] = ",Word[0])
                                        #print("checkforward(",row,", ",column,")")
                                        #print("checkforward: Row: ",Row,", Column: ", Column)
                                        #print("Column: ",Column," < (tableLength - len(word)): ",tableLength - len(word))
                                        if column < (tableLength - len(Word)):
                                                for columns in range(column, column + len(Word)):
                                                        #print("columns: ",columns, "in range(Column = ",Column,", Column + len(word)) = ",Column + len(word))
                                                        puzzlewordForward.append(puzzle[row][columns])
                                                        #print("puzzlewordForward: ",puzzlewordForward)
                                                        puzzlewordPositionsForward.append([row, columns])
                                                        #print("puzzlewordPositionsForward: ",puzzlewordPositionsForward)
                                                s = ''
                                                for i in range(len(puzzlewordForward)):
                                                        t = puzzlewordForward[i]
                                                        print(t)
                                                        print(s)
                                                        s = s + t
                                                if s == Word:
                                                        print(Word,"found!")
                                                        print("WORD POSITION: ",puzzlewordPositionsForward)
                                                        print("\nSTARTING FROM \tROW: ",row+1,"\t\tCOLUMN: ",columns+1,"\nTO \t\tROW: ",row - len(Word)+2,"\t\tCOLUMN: ",column+1)
                                                        
                                                        return s
                                                        wordFound = s
                                                        
                                                else:  

		                                                puzzlewordPositionsForward.clear()
		                                                #print("puzzlewordPositionsForward: ",puzzlewordPositionsForward)
		                                                puzzlewordForward.clear()
		                                                #print("puzzlewordForward: ",puzzlewordForward)
		                        
                                if row == tableHeight -1 and column == tableLength - 1:
                                                if s != Word:
                                                                print(Word," NOT FOUND CHECKING FORWARD!")
                                                                return
            


def checkupward(Word):
        wordFound = ''
        for row in range(0, tableHeight):
                if wordFound == Word:
                        break
                else:
##                        print("Row: ", row," tableHeight: ", tableHeight)
                        for column in range(0, tableLength):
#                                print("Column: ", column," tableLength: ", tableHeight)
                                if puzzle[row][column] == Word[0]:
##                                        print("puzzle: ",row,"",column," == word 0: ",Word[0])
##                                        print("puzzle [",row,"][",column,"] = ",puzzle[row][column],"|| word[0] = ",Word[0])
##                                        print("checkUpward(",row,", ",column,")")
##                                        #print("checkforward: Row: ",Row,", Column: ", Column)
                                        #print("Column: ",Column," < (tableLength - len(word)): ",tableLength - len(word))


                                        if row >= (len(Word) - 1) and row <= tableHeight:
                                                s = ''
##                                                print("if row(",row,") >= (len(Word) - 1)(",(len(Word) - 1),") :",row >= (len(Word) - 1))
##                                                print("FOR LOOP COMMENT BEFORE FOR LOOP: for row(",row,") in range(row(",row,"), (row - (len(Word) - 1)))(",(row - (len(Word) - 1)),"):")
                                                for rows in range(row,(row - len(Word)),-1):

##                                                        print("FOR LOOP COMMENT AFTER FOR LOOP:for rows(",rows,") in range(row(",row,"), len(Word))(",len(Word),"):")

                                                        puzzlewordUp.append(puzzle[rows][column])
##                                                        print("puzzlewordUp[",puzzlewordUp,"].append(puzzle[rows(",rows,")][column(",column,")])")
##

                                                        puzzlewordPositionsUp.append([rows, column])
##                                                        print("puzzlewordPositionsUp[",puzzlewordPositionsUp,"].append(puzzle[rows(",rows,")][column(",column,")])")
##                                                        print(puzzlewordPositionsUp)

                                                        
                                                for i in range(len(puzzlewordUp)):
                                                        t = puzzlewordUp[i]
##                                                        print(t)
##                                                        print(s)
                                                        s = s + t
##                                                        print("S: ",s)
##                                                        print("Word: ",Word)
##                                                        print("s == word evaluation: ", s == Word)
##                                                        print("s != word evaluation: ", s != Word)
                                                if s == Word:
                                                        print(Word,"found!")
                                                        print(Word," Position: ",puzzlewordPositionsUp)
                                                        
                                                        print("\nSTARTING FROM \tROW: ",row+1,"\t\tCOLUMN: ",column+1,"\nTO \t\tROW: ",row - len(Word)+2,"\t\tCOLUMN: ",column+1)
                                                        print(puzzlewordUp)
                                                        wordFound = s
                                                        return wordFound
                                                else:
                                                        puzzlewordPositionsUp.clear()
                                

                                                        puzzlewordUp.clear()

                                
                                if row == tableHeight -1 and column == tableLength - 1:
                                                if s != Word:
                                                                print(Word," NOT FOUND CHECKING UPWARD!")
                                                                return




def checkdownward(Word):
        wordFound = ''
        for row in range(0, tableHeight):
                
                if wordFound == Word:
                        break
                
                else:
                       # print("Row: ", row," tableHeight: ", tableHeight)
                        
                        for column in range(0, tableLength):
                                #print("Column: ", column," tableLength: ", tableHeight)
                        
                                if puzzle[row][column] == Word[0]:
                                        #print("puzzle: ",row,"",column," == word 0: ",Word[0])
                                        #print("puzzle [",row,"][",column,"] = ",puzzle[row][column],"|| word[0] = ",Word[0])
                                        #print("checkdownward(",row,", ",column,")")
                                        #print("checkforward: Row: ",Row,", Column: ", Column)
                                        #print("Column: ",Column," < (tableLength - len(word)): ",tableLength - len(word))

                                        if row <= (tableHeight - len(Word)):
                                                #print("if row(",row,") < (tableHeight - len(word))(",tableHeight - len(Word),"): ", row < (tableHeight - len(Word)))
                                                
                                                for rows in range(row, row + len(Word)):
                                                        #print("rows(",rows,") in range(row(",row,"), row + len(word))(",row + len(Word),"): ")
                                                        puzzlewordDown.append(puzzle[rows][column])
                                                        #print("puzzlewordDown.append(puzzle[",rows,"][",column,"])")
                                                        puzzlewordPositionsDown.append([rows, column])
                                                        #print("puzzlewordPositionsDown.append([",rows,", ",column,"])")
                                                s = ''

                                                for i in range(len(puzzlewordDown)):
                                                        t = puzzlewordDown[i]
                                                        #print("t =",t)
                                                        s = s + t
                                                        #print("s = ",s)
                                                
                                                if s == Word:
                                                        print(Word,"Found!")
                                                        print(puzzlewordPositionsDown)
                                                        print("WORD POSITION IS: ")
                                                        print("\nSTARTING FROM \tROW: ",row+1,"\t\tCOLUMN: ",column+1,"\nTO \t\tROW: ",row + len(Word),"\t\tCOLUMN: ",column+1)
                                                        wordFound = s
                                                        return s
                                                else:
                                                        puzzlewordDown.clear()
                                                        puzzlewordPositionsDown.clear()


		                        
                                if row == tableHeight -1 and column == tableLength - 1:
                                                if s != Word:
                                                                print(Word," NOT FOUND CHECKING DOWNWARD!")
                                                                return


def checkbackward(Word):
        wordFound = ''
        for row in range(0, tableHeight):
                
                if wordFound == Word:
                        break
                
                else:
                       # print("Row: ", row," tableHeight: ", tableHeight)
                        
                        for column in range(0, tableLength):
                                #print("Column: ", column," tableLength: ", tableHeight)
                        
                                if puzzle[row][column] == Word[0]:
                                        #print("puzzle: ",row,"",column," == word 0: ",Word[0])
                                        #print("puzzle [",row,"][",column,"] = ",puzzle[row][column],"|| word[0] = ",Word[0])
                                        #print("checkbackward(",row,", ",column,")")
                                        #print("checkforward: Row: ",Row,", Column: ", Column)
                                        #print("Column: ",Column," < (tableLength - len(word)): ",tableLength - len(word))
                                        #print("column (",column,") >= (len(Word) - 1)(",len(Word) - 1,"): ",column >= (len(Word) - 1))

                                        if column >= (len(Word) - 1) and column < tableLength:
                                                #print("column (",column,") >= (len(Word) - 1)(",len(Word) - 1,"): ",column >= (len(Word) - 1))

                                                for columns in range(column, column - len(Word),-1):
                                                        #print("columns(",columns,") in range(column(",column,"), column + len(Word)(",column + len(Word),"),-1)")
                                                        puzzlewordBackward.append(puzzle[row][columns])
                                                        #print("puzzlewordBackward.append(puzzle[",row,"][",columns,"])")
                                                        puzzlewordPositionsBackward.append([row,columns])
                                                        #print("puzzlewordPositionsBackward.append([",row,columns,"])")
                                                #print("puzzlewordBackward = ",puzzlewordBackward)
                                                s = ''
                                                for i in range(len(puzzlewordBackward)):
                                                        t = puzzlewordBackward[i]
                                                        #print("t: ",t)
                                                        s = s + t
                                                        #print("s: ",s)
                                                
                                                if s == Word:
                                                        print(Word,"found!")
                                                        print(puzzlewordPositionsBackward)
                                                        print("\n\t\t\tWORD POSITION IS: ")
                                                        print("\n\tSTARTING FROM \tROW: ",row+1,"\t\tCOLUMN: ",column+1,"\n\tTO \t\tROW: ",row+1,"\t\tCOLUMN: ",column-len(Word)+2)
                                                        wordFound = s
                                                        return s
                                                        
                                                else:
                                                        puzzlewordPositionsBackward.clear()
                                                        puzzlewordBackward.clear()


		                        
                                if row == tableHeight -1 and column == tableLength - 1:
                                                if s != Word:
                                                                print(Word," NOT FOUND CHECKING BACKWARD!")
                                                                return


def checkupforward(Word):
        wordFound = ''
        for row in range(0, tableHeight):
                
                if wordFound == Word:
                        break
                
                else:
                       # print("Row: ", row," tableHeight: ", tableHeight)
                        
                        for column in range(0, tableLength):
                                #print("Column: ", column," tableLength: ", tableHeight)
                        
                                if puzzle[row][column] == Word[0]:
                                        # print("puzzle: ",row,"",column," == word 0: ",Word[0])
                                        # #print("puzzle [",row,"][",column,"] = ",puzzle[row][column],"|| word[0] = ",Word[0])
                                        # #print("checkbackward(",row,", ",column,")")
                                        # #print("checkforward: Row: ",Row,", Column: ", Column)
                                        # #print("Column: ",Column," < (tableLength - len(word)): ",tableLength - len(word))
                                        # #print("column (",column,") >= (len(Word) - 1)(",len(Word) - 1,"): ",column >= (len(Word) - 1))
                                        # print("column(",column,") <= (tableLength - len(Word)(",len(Word),"))(",tableLength - len(Word),") or row(",row,") >= (len(Word) - 1)(",len(Word) - 1,") :\n column <= (tableLength - len(Word)) or row >= (len(Word) - 1) == ",column <= (tableLength - len(Word)))

                                        if (column <= (tableLength - len(Word)) and column < tableLength) and (row >= (len(Word) - 1) and row < tableHeight) :

                                                        counter = 0
                                                        for rows in range(row,row - len(Word),-1):
                                                                puzzlewordUpForward.append(puzzle[rows][column + counter])
                                                                print("puzzlewordUpForward.append(puzzle[",rows,"][",column," + ",counter," = ",column + counter," ])")
                                                                puzzlewordPositionsUpForward.append([rows, column + counter])
                                                                print("puzzlewordPositionsUpForward.append([",rows,", ",column," + ",counter," = ",column + counter," ])")
                                                                counter = counter + 1
                                                                print("counter = ",counter)
                                                        s = ''
                                                        for i in range(len(puzzlewordUpForward)):
                                                                t = puzzlewordUpForward[i]
                                                                print("t: ",t)
                                                                s = s + t
                                                                print("s: ",s)
                                                        if s == Word:
                                                                print(Word,"found!")
                                                                print(puzzlewordPositionsUpForward)
                                                                print("\n\t\t\tWORD POSITION IS: ")
                                                                print("\n\tSTARTING FROM \tROW: ",row+1,"\t\tCOLUMN: ",column+1,"\n\tTO \t\tROW: ",row-len(Word)+2,"\t\tCOLUMN: ",column+counter)
                                                        
                                                                wordFound = s
                                                                return s
                                                        else:
                                                                puzzlewordUpForward.clear()
                                                                puzzlewordPositionsUpForward.clear()

		                        
                                                                if row == tableLength - 1 and column == tableHeight - 1:
                                                                                if s != Word:
                                                                                                print(Word," NOT FOUND CHECKING UP FORWARD!")
                                                                                                return




def checkupbackward(Word):
        wordFound = ''
        for row in range(0, tableHeight):
                
                if wordFound == Word:
                        break
                
                else:
                    # print("Row: ", row," tableHeight: ", tableHeight)
                
                        for column in range(0, tableLength):
                                #print("Column: ", column," tableLength: ", tableHeight)
                        
                                if puzzle[row][column] == Word[0]:
                                        # print("puzzle: ",row,"",column," == word 0: ",Word[0])
                                        # #print("puzzle [",row,"][",column,"] = ",puzzle[row][column],"|| word[0] = ",Word[0])
                                        # #print("checkbackward(",row,", ",column,")")
                                        # #print("checkforward: Row: ",Row,", Column: ", Column)
                                        # #print("Column: ",Column," < (tableLength - len(word)): ",tableLength - len(word))
                                        # #print("column (",column,") >= (len(Word) - 1)(",len(Word) - 1,"): ",column >= (len(Word) - 1))
                                        # print("column(",column,") <= (tableLength - len(Word)(",len(Word),"))(",tableLength - len(Word),") or row(",row,") >= (len(Word) - 1)(",len(Word) - 1,") :\n column <= (tableLength - len(Word)) or row >= (len(Word) - 1) == ",column <= (tableLength - len(Word)))

                                        # print("\nif column >= len(Word) - 1 == ",column >= len(Word) - 1," or row >= (len(Word) - 1) == ",row >= (len(Word) - 1))

                                        if column >= len(Word) - 1 or row >= (len(Word) - 1):
                                                #print("\nInner if column >= len(Word) - 1 == ",column >= len(Word) - 1," or row >= (len(Word) - 1) == ",row >= (len(Word) - 1))
                                                counter = 0
                                                for rows in range(row, row - len(Word), -1):
                                                        #print("for rows in range(row(",row,"), row - len(Word)(",row - len(Word),"), -1):")
                                                        puzzlewordUpBackward.append(puzzle[rows][column - counter])
                                                        #print("puzzlewordUpBackward.append(puzzle[rows(",rows,")][column(",column,") - counter(",counter,") = ",column - counter," ])")
                                                        puzzlewordPositionsUpBackward.append([rows, column - counter])
                                                        #print("puzzlewordPositionsUpBackward.append([rows(",rows,"), column(",column,") - counter(",counter,") = ",column - counter,"])")
                                                        counter = counter + 1

                                                s = ''
                                                for i in range(len(puzzlewordUpBackward)):
                                                        
                                                        t = puzzlewordUpBackward[i]
                                                        print("t: ",t)
                                                        s = s + t
                                                        print("s: ",s)
                                                if s == Word:
                                                        print(Word,"found!")
                                                        print(puzzlewordPositionsUpBackward)
                                                        print(puzzlewordUpBackward)
                                                        print("\n\t\t\tWORD POSITION IS: ")
                                                        print("\n\tSTARTING FROM \tROW: ",row+1,"\t\tCOLUMN: ",column+1,"\n\tTO \t\tROW: ",row-len(Word)+2,"\t\tCOLUMN: ",column-counter+2)
                                                        wordFound = s
                                                        return s
                            
                                                else:
                                                        puzzlewordPositionsUpBackward.clear()
                                                        puzzlewordUpBackward.clear()

		                        
                                if row == tableHeight -1 and column == tableLength - 1:
                                                if s != Word:
                                                                print(Word," NOT FOUND CHECKING Up Backward!")
                                                                return


def checkdownforward(Word):
        wordFound = ''
        for row in range(0, tableHeight):
                
            if wordFound == Word:
                    break
            
            else:
                # print("Row: ", row," tableHeight: ", tableHeight)
                for column in range(0, tableLength):
                        #print("Column: ", column," tableLength: ", tableHeight)
                
                            if puzzle[row][column] == Word[0]:
                                        # print("puzzle: ",row,"",column," == word 0: ",Word[0])
                                        # #print("puzzle [",row,"][",column,"] = ",puzzle[row][column],"|| word[0] = ",Word[0])
                                        # #print("checkbackward(",row,", ",column,")")
                                        # #print("checkforward: Row: ",Row,", Column: ", Column)
                                        # #print("Column: ",Column," < (tableLength - len(word)): ",tableLength - len(word))
                                        # #print("column (",column,") >= (len(Word) - 1)(",len(Word) - 1,"): ",column >= (len(Word) - 1))
                                        # print("column(",column,") <= (tableLength - len(Word)(",len(Word),"))(",tableLength - len(Word),") or row(",row,") >= (len(Word) - 1)(",len(Word) - 1,") :\n column <= (tableLength - len(Word)) or row >= (len(Word) - 1) == ",column <= (tableLength - len(Word)))

                                        # print("\nif column >= len(Word) - 1 == ",column >= len(Word) - 1," or row >= (len(Word) - 1) == ",row >= (len(Word) - 1))


                                        if row <= (tableHeight - len(Word)) and column <= (tableLength - len(Word)):
                                                #print("\nInner if column >= len(Word) - 1 == ",column >= len(Word) - 1," or row >= (len(Word) - 1) == ",row >= (len(Word) - 1))
                                             
                                                counter = 0
                                                #print("for rows in range(row(",row,"), row - len(Word)(",row - len(Word),"), -1):")
                                                for rows in range(row, row + len(Word) ):

                                                        puzzlewordDownForward.append(puzzle[rows][column + counter])
                                                        puzzlewordPositionsDownForward.append([rows, column + counter])
                                                        # print("puzzlewordDownForward.append(puzzle[rows(",rows,")][column(",column,") + counter(",counter,") = ",column + counter," ])")
                                                        # print("puzzlewordPositionsDownForward.append([rows(",rows,"), column(",column,") + counter(",counter,") = ",column + counter,"])")

                                                        counter = counter + 1
                                                s = ''
                                                for i in range(len(puzzlewordDownForward)):
                                                        t = puzzlewordDownForward[i]
                                                        s = s + t
                                                        # print("t: ",t)
                                                        # print("s: ",s)
                                                if s == Word:
                                                        print(Word,"found!")
                                                        print(puzzlewordPositionsDownForward)
                                                        print(puzzlewordDownForward)
                                                        print("\n\t\t\tWORD POSITION IS: ")
                                                        print("\n\tSTARTING FROM \tROW: ",row+1,"\t\tCOLUMN: ",column+1,"\n\tTO \t\tROW: ",row+len(Word),"\t\tCOLUMN: ",column+counter)
                                                        wordFound = s
                                                        return s

                                                else:
                                                        puzzlewordPositionsDownForward.clear()
                                                        puzzlewordDownForward.clear()

		                        
                                        if row == tableHeight -1 and column == tableLength - 1:
                                                        if s != Word:
                                                                        print(Word," NOT FOUND CHECKING Down Forward!")
                                                                        return



def checkdownbackward(Word):
        wordFound = ''
        for row in range(0, tableHeight):
                
            if wordFound == Word:
                    break
            
            else:
                # print("Row: ", row," tableHeight: ", tableHeight)
                for column in range(0, tableLength):
                        #print("Column: ", column," tableLength: ", tableHeight)
                
                            if puzzle[row][column] == Word[0]:
                                        # print("puzzle: ",row,"",column," == word 0: ",Word[0])
                                        # #print("puzzle [",row,"][",column,"] = ",puzzle[row][column],"|| word[0] = ",Word[0])
                                        # #print("checkbackward(",row,", ",column,")")
                                        # #print("checkforward: Row: ",Row,", Column: ", Column)
                                        # #print("Column: ",Column," < (tableLength - len(word)): ",tableLength - len(word))
                                        # #print("column (",column,") >= (len(Word) - 1)(",len(Word) - 1,"): ",column >= (len(Word) - 1))
                                        # print("column(",column,") <= (tableLength - len(Word)(",len(Word),"))(",tableLength - len(Word),") or row(",row,") >= (len(Word) - 1)(",len(Word) - 1,") :\n column <= (tableLength - len(Word)) or row >= (len(Word) - 1) == ",column <= (tableLength - len(Word)))

                                        # print("\nif column >= len(Word) - 1 == ",column >= len(Word) - 1," or row >= (len(Word) - 1) == ",row >= (len(Word) - 1))



                                        if row >= (tableHeight - len(Word)) or column >= (len(Word) - 1):
                                                counter = 0
                                                for rows in range(row, row + len(Word)):
                                                        puzzlewordDownBackward.append(puzzle[rows][column - counter])
                                                        puzzlewordPositionsDownBackward.append([rows,column - counter])
                                                        counter = counter + 1
                                                s = ''
                                                for i in range(len(puzzlewordDownBackward)):
                                                        t = puzzlewordDownBackward[i]
                                                        s = s + t
                                                if s == Word:
                                                        print(Word,"found!")
                                                        print(puzzlewordPositionsDownBackward)
                                                        print(puzzlewordDownBackward)
                                                        print("\n\tSTARTING FROM \tROW: ",row+1,"\t\tCOLUMN: ",column+1,"\n\tTO \t\tROW: ",row+len(Word),"\t\tCOLUMN: ",column-counter+2)
                                                        wordFound = s
                                                        return s

                                                else:
                                                        puzzlewordPositionsDownBackward.clear()
                                                        puzzlewordDownBackward.clear()

		                        
                                                        if row == tableHeight - len(Word) and column == (len(Word) - 1):
                                                                        if s != Word:
                                                                                        print(Word," NOT FOUND CHECKING Down Backward!")
                                                                                        return






findUpward = checkupward(word)
##findUpForward = checkupforward(word)
##findForward = checkforward(word)
##findDownForward = checkdownforward(word)
##findDownward = checkdownward(word)
##findDownBackward = checkdownforward(word)
##findBackward = checkbackward(word)
##findUpBackward =  checkupbackward(word)
##






##if findDownward == word:
##        print("\n",word," IS DOWNWARD")
##        
##else:
##        print(word," NOT FOUND!")

                                
                        
##			checkdownward(row, column)
##		
##			checkbackward(row, column)
##
##			checkupward(row, column)
##
##			checkdownforward(row, column)
##		
##			checkdownbackward(row, column)
##		
##			checkupforward(row, column)
##		
##			checkupbackward(row, column)
##
##
