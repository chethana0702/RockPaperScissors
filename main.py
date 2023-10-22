import random

class RockPaperScissors:
    def __init__(self):
        self.user_point = 0
        self.computer_point = 0

    def print_welcome_message(self):
        print("Welcome to Rock Paper Scissors Game!!!!")
        print("Winning rules of the Rock Paper Scissors Game is as follows:")
        print("1.Rock vs Paper --> Paper wins")
        print("2.Rock vs Scissor --> Rock wins")
        print("3.Paper vs Scissor --> Scissor wins")

    def get_score_limit(self):
        return int(input("Enter the score limit:"))

    def get_user_choice(self):
        while True:
            print("Now it's your turn!!")
            print("Please Enter your choice")
            print("[1 for Rock]")
            print("[2 for Paper]")
            print("[3 for Scissors]")
            choice_number = int(input())
            if choice_number in [1, 2, 3]:
                return choice_number
            else:
                print("Please give a valid input")

    def get_computer_choice(self):
        return random.randint(1, 3)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            self.computer_point += 1
            self.user_point += 1
        elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1):
            self.computer_point += 1
        elif (user_choice == 1 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
            self.user_point += 1
        elif (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 2):
            self.computer_point += 1

    def print_scores(self):
        print("User Score:", self.user_point)
        print("Computer Score:", self.computer_point)

    def play_game(self):
        self.print_welcome_message()
        score_limit = self.get_score_limit()

        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()

            print("You chose: " + self.get_choice_name(user_choice))
            print("Computer chose: " + self.get_choice_name(computer_choice))
            print(self.get_choice_name(user_choice) + " vs " + self.get_choice_name(computer_choice))

            self.determine_winner(user_choice, computer_choice)
            self.print_scores()

            if self.user_point >= score_limit or self.computer_point >= score_limit:
                break

        self.determine_game_winner()

    def get_choice_name(self, choice_number):
        if choice_number == 1:
            return "Rock"
        elif choice_number == 2:
            return "Paper"
        elif choice_number == 3:
            return "Scissors"

    def determine_game_winner(self):
        if self.computer_point > self.user_point:
            print("Computer wins: " + str(self.computer_point) + " / " + str(self.user_point))
        elif self.user_point > self.computer_point:
            print("User wins: " + str(self.user_point) + " / " + str(self.computer_point))
        else:
            print("It's a draw")

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
