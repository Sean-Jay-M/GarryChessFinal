# How To Run

## Prerequisites 

### Python 

To get started, you should [install Python](https://realpython.com/installing-python/)
on your system. Please install a version no less than 3.8.

After that, you should [install pip](https://pip.pypa.io/en/stable/installation/)
for managing python packages.

Be ensure to pip install the required packages listed in *requirements.txt*. It is best to do this in an environment. Some Packages will need to be installed in the global environment.

### Node.js and React 

Install [Node.js](https://nodejs.org/en/)

Run the following command in the *frontend* directory 

    npx create-react-app my-react-app

or

    npm install react

Be sure to npm install any required packages.

## Setting Up The Backend

You must pip install the relevent packages. These packages are within the requirements.txt file.

To run locally simply run the command:

      python manage.py runserver 8000

## setting up the frontend 

Change to the directory *frontend/chessinterface* ensure you have npx installed React and the relevent modules. It is important that you npm install these specific modules at these particular versions:

 chess.js@0.13.3 and react-chessboard@1.2.5 

run the following command:

    $ npm start run
  
This will open up the application and run it.
