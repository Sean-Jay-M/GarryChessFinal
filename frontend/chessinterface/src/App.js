import './App.css';
import { useState } from 'react';
import {Chessboard} from 'react-chessboard'
import {Chess} from 'chess.js'
import React, { useEffect } from 'react'
              
function App() {
  const [game, setGame] = useState(new Chess());
//Let's perform a function on the game state 
  const [fenCode, setfenCode] = useState(null);
 
function safeGameMutate(modify){
  setGame((g)=>{
    const update = {...g}
    modify(update)
    return update;
  })
}

useEffect(()=>{

  makeRandomMove()
  
  }, [])

async function getMoveBackend(board){
  const response = await fetch(`http://localhost:8000/api/?board=${encodeURIComponent(board)}`)
  const data = await response.json();
  return data
}

function timeout(delay) {
  return new Promise( res => setTimeout(res, delay) );
}

//Movement of computer
async function makeRandomMove(){
  const possibleMove = game.moves();

  //exit if the game is over 
  if(game.game_over() || game.in_draw() || possibleMove.length === 0) return;
  //select move from backend
  const botMove = await getMoveBackend(game.fen())

  console.log(botMove)
  const finalMove = botMove
  console.log(finalMove)
 //play random move 
  await timeout(500); //for short sec delay
  safeGameMutate((game)=>{
  game.move(finalMove);
  console.log(finalMove)
 })
}

//Perform an action when a piece is droped by a user
 
async function onDrop(source,target){
  let move = null;
  let squareColor = game.get(source)
  safeGameMutate((game)=>{
    move = game.move({
      from:source,
      to: target,
      promotion:'q'
    })
})
  //currently working here
  // wrong color
  if(squareColor === 'w') return false
  //if cannot figure out move on.

 //illegal move 
 if(move== null) return false
 //valid move 
 setTimeout(makeRandomMove, 200);
 return true;
}
  return (
    <div className="app">
      <Chessboard
      boardOrientation='black'  
      position={game.fen()}
      onPieceDrop ={onDrop}
      />
    <div className='description'>
    <img src={require("./assets/logo.png")} className="logo"></img>
      <p classNme='descParaTwo'>
        Hello ! Welcome to GarryChess. It is a custom Chess AI made by Sean Moiselle.
        <br></br>
        There are a few basic things to remember:
      <br></br>
     
      <br></br>The AI is optimised to play as white.
      <br></br>All moves by the AI are produced server side.
      <br></br>Frontend is still under development.
      <br></br>Frontend can be a little buggy sometimes.
      <br></br>Sean Moiselle is not a frontend developer.
      
      <br></br><br></br>
      </p>
      <p classNme='descPara'>It uses a Minimax Algorithm which analyses potential board positions using a Convulutional <br></br> Neural Network. The complexity
      of this Minimax algorithm can be defined as  O(b^m) where <br></br> the space complexity is O(bm). The model currently being used has only been trained to 10 <br></br> Epochs due to time constraints. 
      The final model will be trained to 1000 Epochs.
      Testing will <br></br> be conducted to produce a ELO  score for this Minimax/Convulutional model approach once <br></br> the final model is produced.
      </p>
    </div>
    </div>
  );
}

export default App;