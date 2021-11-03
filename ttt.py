class moves:
  x = []
  o = []
  currentPlayer = "x"
  allowed = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
  ]

# Get the move from the input
def getMove(player):
  move = input(player + "'s turn. Pick a field: ")

  if move not in moves.allowed:
    print("This move is not allowed. Please choose a field between 1 and 9")
    return getMove(player)

  if move in moves.x or move in moves.o:
    print("This field is already taken")
    return getMove(player)

  if player == "x":
    moves.currentPlayer = "o"
    moves.x.append(move)
  else:
    moves.currentPlayer = "x"
    moves.o.append(move)
  
  if isWin():
    printField()
    print("Player " + isWin() + " won. Congratulations")
    return exit()

  loadGame()

# Print the field
def printField():
  rows = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
  ]

  for move in moves.x:
    rows[rowOfField(move)][moveIndex(move)] = "x"
  
  for move in moves.o:
    rows[rowOfField(move)][moveIndex(move)] = "o"

  for row in rows:
    i = rows.index(row)
    rows[i] = " | ".join(row)

  print("\n".join(rows))

# Print the new field and wait for the next input for the move
def loadGame():
  printField()
  getMove(moves.currentPlayer)

# Get the index of the field in the row
def moveIndex(field):
  if field in ["1", "4", "7"]:
    return 0
  
  if field in ["2", "5", "8"]:
    return 1
  
  if field in ["3", "6", "9"]:
    return 2

# Get the row of the field
def rowOfField(field):
  if field in ["1", "2", "3"]:
    return 0
  
  if field in ["4", "5", "6"]:
    return 1
  
  if field in ["7", "8", "9"]:
    return 2

# Check if a user wins
def isWin():
  if "1" in moves.x and "2" in moves.x and "3" in moves.x:
    return "x"
  
  if "4" in moves.x and "5" in moves.x and "6" in moves.x:
    return "x"

  if "7" in moves.x and "8" in moves.x and "9" in moves.x:
    return "x"
  
  if "1" in moves.x and "4" in moves.x and "7" in moves.x:
    return "x"
  
  if "2" in moves.x and "5" in moves.x and "8" in moves.x:
    return "x"

  if "3" in moves.x and "6" in moves.x and "9" in moves.x:
    return "x"
  
  if "1" in moves.x and "5" in moves.x and "9" in moves.x:
    return "x"

  if "3" in moves.x and "5" in moves.x and "7" in moves.x:
    return "x"
  

  if "1" in moves.o and "2" in moves.o and "3" in moves.o:
    return "o"
  
  if "4" in moves.o and "5" in moves.o and "6" in moves.o:
    return "o"

  if "7" in moves.o and "8" in moves.o and "9" in moves.o:
    return "o"
  
  if "1" in moves.o and "4" in moves.o and "7" in moves.o:
    return "o"

  if "2" in moves.o and "5" in moves.o and "8" in moves.o:
    return "o"

  if "3" in moves.o and "6" in moves.o and "9" in moves.o:
    return "o"
  
  if "1" in moves.o and "5" in moves.o and "9" in moves.o:
    return "o"

  if "3" in moves.o and "5" in moves.o and "7" in moves.o:
    return "o"

# Start the game
loadGame()