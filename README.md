# GarryChessFinal

** Documentation is still being written **

A React - Django web application which utilizes Deep Learning techniques (Convolutional Neural Networks) to play chess. Testing is currently underway to ascertain the ELO of the Model.
This application was made over the course of a number of months with by one individual with extensive research:

[Sean-Jay-M](https://github.com/Sean-Jay-M)

![Architecture](https://github.com/Sean-Jay-M/GarryChessFinal/blob/documentation/garrychessinterface.PNG)

## Branches
*Main:*  The Main branch contains the web application, containing the React - Django files.

*modelBuilding:* Contains jupyter notebooks used to build the model and instructions on how to replicate the results.

*Documentation:* The documentation branch contains details on how to run this project locally and various images of the application. This has not been completed.

## Application Architecture
<p align="center">
![Architecture](https://github.com/Sean-Jay-M/GarryChessFinal/blob/documentation/webGarryChess.png)
</p>

The architecture is a simple React-Django Application which utilizes API's in order to get AI Moves. The npm packages chess.js@0.13.3 and react-chessboard@1.2.5 are utilized to provide the frontend logic and interface. It is imperative that these specific versions are utilized, please read how to run for more details. The backend is supported by the ChessMove class which makes use of a convulutional neural network in order to provide moves. Py_client contains a simple script which will provide a prediction without the need for installing or running the frontend application, this is included for ease of use and for those who are only interested in the API itself and not the frontend user interface.

## Chess Class

Both the backend and the model building made use of this class (or group of functions in the case of the model building). It is important to understand how this works in order to understand the role of the Neural Network. The Convolutional Neural Network provides board evaluations i.e is this board position beneficial for white. This evaluation is utilized as part of a Minimax Algorithm with the complexity of O(b^m) in order to provide the best move. To view this class within the web application click [here.](https://github.com/Sean-Jay-M/GarryChessFinal/blob/main/backend/api/chessfuncs.py)

<p align="center">
![class](https://github.com/Sean-Jay-M/GarryChessFinal/blob/documentation/chessClass.png)
</p>

## Notes

Documentation on how to run this locally is being written. 
For any questions please contact [Sean-Jay-M](https://github.com/Sean-Jay-M)
