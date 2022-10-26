import requests
import random
import chess
#creating python api client end point


#This is the url or a URL which belongs to this project. 
# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

#here we are testing the api
# This produces a random board which will later be analyzed
def randomBoardGenerator(max_depth=200):
    chessBoard = chess.Board()
    depth = random.randrange(0, max_depth)

#for i in range of the depth,create a list of all moves. Choose a random value from that list.
#make move, if game is over break, if not return the chessboard
    for i in range(depth):
        allMoves = list(chessBoard.legal_moves)
        randomMove = random.choice(allMoves)
        chessBoard.push(randomMove)
        if chessBoard.is_game_over():
            break
    
    chessBoard = chessBoard.board_fen()
    return chessBoard


#params are the most important part of our API. These will send the 
get_response = requests.get(endpoint, params={'board': 'rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq d3 0 1'}) #API  #http request #REST will carry JSON or XML

print(requests.get(endpoint, params={'board': randomBoardGenerator()}, json={"move":"Making a Move"}))
#print(get_response.text) # print raw text response
#print(get_response.status_code) 

print(get_response.json())