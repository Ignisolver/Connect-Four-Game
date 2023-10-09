# Connect Four
## Summary
This project is an implementation of simple "Connect Four" (https://en.wikipedia.org/wiki/Connect_Four) game.
## Installation
To install the necessary modules, please follow these steps:
1. Open your terminal.
2. Navigate to the project directory (is-connect-four) using the ```cd``` command. 
3. Type the following command:  
```pip install -r requirements.txt```  
This will install the required module, windows-curses.
Please note that the project requires Python version 3.11.
## Run 
To run the game, please follow these steps:   
1. Open your terminal.
2. Navigate to the project directory (is-connect-four) using the ```cd``` command.
3. Type the following command:  
```python main.py```
## Usage
### Providing player names
When you start the game, you will be prompted to provide the names of the players.
After entering each name, press ```Enter``` to confirm.
### Playing
Players take turns alternately.
Use the right and left arrow keys to change the position of the token.
Press ```Enter``` to drop the token into the column below.
You cannot drop a token into a full column.
After a token is dropped, the turn will switch to the next player.
### End of the game
To quit the game at any time, you can press ```Ctrl + C```.
When a player wins or the tokens run out, you will be notified that the game has ended and who the winner is.
To quit the game, press the ```Esc``` key. To play again, press any other key.