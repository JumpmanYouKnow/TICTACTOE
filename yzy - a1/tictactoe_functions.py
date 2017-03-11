EMPTY = '-'


def is_between(value, min_value, max_value):
    """ (number, number, number) -> bool

    Precondition: min_value <= max_value

    Return True if and only if value is between min_value and max_value,
    or equal to one or both of them.

    >>> is_between(1.3, 0.5, 2)
    True
    >>> is_between(0, 2, 3)
    False
    """
    return (value >= min_value) & (value <= max_value)

def game_board_full(myStr):
    """ (str) -> bool
    
    Precondition: myStr is a valid tic-tac-toe game board.
    
    Return True if and only if all of the cells in the game board have 
    been chosen. That is, True is returned if and only if 
    there are no EMPTY characters in the game board.
    
    >> game_board_full("ooxx") 
    Ture
    >> game_board_full("___x")
    False
    """
    if EMPTY not in myStr:
        return True
    else:
        return False
    
def get_board_size(myStr):
    """(str) -> int
    
    Precondition: myStr refers to a valid tic-tac-toe game board.The length 
    of the parameter is a perfect square
    
    Return the length of each side of the given tic-tac-toe game board
    
    >> get_board_size("XOXO")
    2
    >> get_board_size("XOXOXOXOX")
    3
    """
    length = len(myStr)
    return int(length ** (0.5))
    
def make_empty_board(size):
    """ (int) -> str
    
    Precondition: Size refers to the size of a valid tic-tac-toe game board,
    assume value is >= 1 and <= 9 
    Return the return a string for storing information 
    about a tic-tac-toe game board whose size is given by the parameter.
    
    >> make_empty_board(4)
    "____"
    >> make_empty_board(9)
    "_________"
    
    """
    myBoard = ""
    for x in range(0, size):
        for x in range(0, size):
            myBoard += EMPTY
        
    return myBoard

def get_str_index(row, col, size):
    """(int, int, int) -> int
    
    Precondition:The first and second parameters should be the row and column 
    indices, respectively, of a cell in a valid tic-tac-toe game board 
    whose size is given by the third parameter. 
    
    Return the str_index of the cell in the string representation 
    of the game board corresponding to the given row and column indices.
    
    >> get_str_index(1, 1, 2):
    0
    >> get_str_index(1, 2, 2):
    1
    """
    
    return int((row - 1) * size + col - 1)

def make_move(sym, row, col, myBoard):
    """(str, int, int, str) -> str
    
    Precondition: The first parameter should be a one character string 
    containing a symbol (usually, but not necessarily, an 'X' or 'O'). 
    The second and third parameters should be valid row and column of the symobl
    The fourth parameter is a string which is the valid tic-tac-toe game board.
    
    Return return the tic-tac-toe game board that results when the given 
    symbol is placed at the given cell position in the 
    given tic-tac-toe game board.
    
    >>make_move("O", 1, 2, "____")
    "_O__"
    >>make_move("X", 3, 3, "XXXOOO___")
    "XXXOOO__X"
    
    """
    size = get_board_size(myBoard)
    index = get_str_index(row, col, size)
    myBoard = myBoard[0:(index)] + sym + myBoard[(index + 1):]
    return myBoard
    
def extract_line(myBoard, direction, col_or_row):
    """(str, str, int) -> str
    
    
    Precondition:The first parameter should be a valid tic-tac-toe game board. 
    The second parameter should be a string that describes one of 
    the directions: 'down', 'across', 'down_diagonal' or 'up_diagonal'. 
    The third parameter should be a valid row or column number in
    the tic-tac-toe game board referred to by the first parameter.
    
    Return the characters that make up the specified row (when the second 
    parameter refers to 'across'), column (when the second parameter is 'down') 
    or diagonal from the given tic-tac-toe game board.
    
    >>extract_line("XOXO", 'down_diagonal', 3)
    "XO"
    >>extract_line("XOOO", 'up_diagonal', 11)
    "OO"
    >>extract_line("XOXO", 'down', 1)
    "XX"
    >>extract_line("XOXO", 'down', 2)
    "OO"
    extract_line("XXXOOOXXX", 'down', 1)
    'XOX'
    >>extract_line("OXOX", 'across', 0)
    "OX"
    >>extract_line("XOXX", 'across', 1)
    "XO"
    >>extract_line("XXXOOOXXX", 'across', 1)
    'XXX'
    """
    retval = ""
    size = get_board_size(myBoard)
    if (direction == 'down_diagonal'):
        for x in range (0, size):
            index = get_str_index(x + 1, x + 1, size)
            retval += myBoard[index]
    elif (direction == 'up_diagonal'):  
        for x in range (0, size):
            index = get_str_index(size - x, x + 1, size)
            retval += myBoard[index]
    elif (direction == "down"):    
        for x in range (0, size):
            index = get_str_index(x + 1, col_or_row, size)
            retval += myBoard[index]
    elif (direction == "across"):       
        for x in range (0, size):
            index = get_str_index(col_or_row, x + 1, size)
            retval += myBoard[index]    
    

    return retval    
    
    
    
    
    
    
    
    
    
    

    # Students are to complete the body of this function, and then put their
    # solutions for the other required functions below this function.
