import chess
from chess import engine
import numpy
from keras.models import load_model
import os

#load in the convulutional model #smssyfsdoifspdj
workingDirectory = str(os.getcwd())
modelDirectory = workingDirectory + "\\api\model\model.h5"
model = load_model(modelDirectory)

#here is defined a dictionary which sets the board positions.
#Where a: 0 b: 1 and so on. This will define the row, or the column within the 2d array the piece or pawn is on.
boardPositions = {
  'a': 0,
  'b': 1,
  'c': 2,
  'd': 3,
  'e': 4,
  'f': 5,
  'g': 6,
  'h': 7
}


class chessMove():
    def __init__(self, **kwargs):
        self.board = kwargs['board']

    #this function will find the square which the function resides on.
    def square_to_index(self, square):
        #find the algebraic notation for the square name
        letter = chess.square_name(square)
        # return 8 (number of rows) minus the value of the character at index 1 in letter, eg 'a1'. This will find the row the piece exists on.
        # also return the letter or column which the piece exists on.
        return 8 - int(letter[1]), boardPositions[letter[0]]

    """
    Splits the board into a 3d matrix.
    Matrix 1 represents all white pawns, 2 knights, 3 bishops, 4 Rooks, 5 Queen and 7 King.
    Repeat for black Pieces.
    The second to last matrixes represent all the available squares where white can move.
    The final matrix represents all the available squares where black can move.
    """
    def split_dims(self, board):
        board3d = numpy.zeros((14, 8, 8), dtype=numpy.int8)

    # here we add the pieces's view on the matrix
        for piece in chess.PIECE_TYPES:
            for square in board.pieces(piece, chess.WHITE):
                idx = numpy.unravel_index(square, (8, 8))
                board3d[piece - 1][7 - idx[0]][idx[1]] = 1
        for square in board.pieces(piece, chess.BLACK):
                idx = numpy.unravel_index(square, (8, 8))
                board3d[piece + 5][7 - idx[0]][idx[1]] = 1

    # add attacks and valid moves too
    # so the network knows what is being attacked
        aux = board.turn
        board.turn = chess.WHITE
        for move in board.legal_moves:
            i, j = self.square_to_index(move.to_square)
            board3d[12][i][j] = 1
        board.turn = chess.BLACK
        for move in board.legal_moves:
            i, j = self.square_to_index(move.to_square)
            board3d[13][i][j] = 1
        board.turn = aux

        return board3d
    
    def minimax_eval(self, board):
        board3d = self.split_dims(board)
        board3d = numpy.expand_dims(board3d, 0)
        return model.predict(board3d)[0][0]

    #this is the actual minimax algorithm
    def minimax(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0 or board.is_game_over():
            return self.minimax_eval(board)
    
        if maximizing_player:
            max_eval = -numpy.inf
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, alpha, beta, False)
                board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = numpy.inf
            for move in board.legal_moves:
                board.push(move)
                eval = self.minimax(board, depth - 1, alpha, beta, True)
                board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

    def get_ai_move(self, depth=1):
        board = self.board
        max_move = None
        max_eval = -numpy.inf

        for move in board.legal_moves:
            board.push(move)
            eval = self.minimax(board, depth - 1, -numpy.inf, numpy.inf, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                max_move = move
    
        return max_move