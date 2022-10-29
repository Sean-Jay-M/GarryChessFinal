# GarryChess
The model is a convolutional neural network trained to 10 Epochs. I will retrain the model at a later date to 1000 Epochs once I have access to better hardware.
There is code included which will create a dataset, you need to set an appropriate amount of values for your machine to create the dataset.

On a very high level, the Neural Networks aim is to predict the evauluation of a given board. It trains using evaluations provided by the worlds best/second best chess engine 'Stockfish'.

This neural network is then utilized by a minimax algorithm to evaluate all potential positions out of the available moves. The best move is then selected.
