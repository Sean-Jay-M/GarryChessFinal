#this is of course for formatting the api
from django.http import JsonResponse
from .chessfuncs import chessMove
import json
from chess import Board

#takes a request, pass in arguments and kwarguments
#alter this


### Possibly change all responses to a dictionary ! 

def api_home(request, *args, **kwargs):
    # request is a HttpRequest, no relation to python requests.
    # request.body
    body = request.body #byte string of JSON Data
    data = {}
    try:
        data['params'] = dict(request.GET)
    except:
        return JsonResponse('Invalid Data, what are you doing ?', safe=False)
    print(data.keys())
    data['params'] = dict(request.GET)
    print(data)
    currentBoard = data['params']['board']
    actualBoard = Board(currentBoard[0])
    #convertBoard = Board(currentBoard)
    try:
        moveHold = chessMove(board=actualBoard).get_ai_move()
    except:
        return JsonResponse('Invalid Data Section Two, what are you doing ?', safe=False)
    print(str(moveHold))
    moveOne = str(moveHold)[:2]
    moveTwo = str(moveHold)[-2:]
    move = {"from": moveOne, "to": moveTwo}
    returnMove = move
    return JsonResponse(returnMove, safe=True)
    #try return the move at first, if not return the whole board.