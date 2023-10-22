Rock Paper Scissors Game
This is a simple implementation of the classic Rock Paper Scissors game in Python. It allows a user to play against the computer and keeps track of the scores. The game is played until a specified score limit is reached.

How to Play
Run the Python program.
Follow the on-screen instructions to play the game.
Enter your choice by typing the corresponding number:
1 for Rock
2 for Paper
3 for Scissors
The computer will make its choice, and the winner of each round will be determined based on the game's rules.
The scores of both the user and the computer are displayed after each round.
The game continues until one of the players reaches the specified score limit.
Rules
Rock beats Scissors
Scissors beat Paper
Paper beats Rock
Customization
You can set the score limit for the game at the beginning to determine how long the game will last. The first player to reach or exceed the score limit wins.

File Description
rock_paper_scissors.py: The main Python program containing the game logic.
README.md: This documentation file.
Example
Here is a sample run of the game:

rust
Copy code
Welcome to Rock Paper Scissors Game!!!!

Winning rules of the Rock Paper Scissors Game is as follows:
1.Rock vs Paper --> Paper wins
2.Rock vs Scissor --> Rock wins
3.Paper vs Scissor --> Scissor wins

Enter the score limit: 5

Now it's your turn!!
Please Enter your choice
[1 for Rock]
[2 for Paper]
[3 for Scissors]

1
You chose: Rock
Computer chose: Paper
Rock vs Paper
User Score: 0
Computer Score: 1

Now it's your turn!!
Please Enter your choice
[1 for Rock]
[2 for Paper]
[3 for Scissors]

2
You chose: Paper
Computer chose: Rock
Paper vs Rock
User Score: 1
Computer Score: 1

Now it's your turn!!
Please Enter your choice
[1 for Rock]
[2 for Paper]
[3 for Scissors]

3
You chose: Scissors
Computer chose: Paper
Scissors vs Paper
User Score: 2
Computer Score: 1

...

User wins: 5 / 2
In this example, the user reached the specified score limit of 5 points and won the game.

License
This program is open-source and available under the MIT License.

