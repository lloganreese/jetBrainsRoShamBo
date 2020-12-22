import random


class RoShamBo:
    options = ["rock", "gun", "lightning", "devil", "dragon",
               "water", "air", "paper", "sponge", "wolf", "tree",
               "human", "snake", "scissors", "fire"]

    # prompts user for their name & greets user
    # searches through 'ratings.txt' to see if users input matches username in file
    # file is closed and 'play_game' method is called
    def __init__(self):
        self.chosen_options = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.user_name = input("Enter your name:")
        print("Hello, " + self.user_name)

        opened_rating = open('rating.txt', 'r')

        for users in opened_rating.readlines():
            if users.split()[0] == self.user_name:
                self.user_score = int(users.split()[1])

        opened_rating.close()

        self.create_game_list()

    def create_game_list(self):
        while True:
            selected_game_list = input().split(",")

            # if no input is detected game starts & options stay 'regular'
            # checks to make sure the input above is contained within the overall options
            # final option is to start game with selected options list
            if selected_game_list == [""]:
                print("Okay, let's start")
                self.play_game()
            elif not set(selected_game_list).issubset(RoShamBo.options):
                print("Invalid Input")
            else:
                self.chosen_options = selected_game_list
                print("Okay, let's start")
                self.play_game()

    def play_game(self):
        while True:
            user_won = []
            remake = []
            user_input = input()

            # queries user if they want to check rating/exit before gameplay
            if user_input == '!exit':
                print("Bye!")
                exit()
            elif user_input == '!rating':
                print(self.user_score)
                continue
            elif user_input not in self.chosen_options:
                print("Invalid input")
                continue

            # computer selects an opposing play from the users selected list
            computer_choice = random.choice(self.chosen_options)

            # takes the original options list and creates a new list of the
            # options that defeat the users choice
            user_options_index = RoShamBo.options.index(user_input)
            middle_index = int((len(RoShamBo.options) - 1) / 2)
            user_lost = RoShamBo.options[user_options_index + 1:user_options_index + middle_index + 1]

            # if users choice is indexed past the middle of the overall options list
            # then the 'winning' list is created and the users_lost list is created
            # from everything that is not in the winning list
            if user_options_index > middle_index:
                user_lost = RoShamBo.options[user_options_index - middle_index:user_options_index + 1:1]
                user_lost = [i for i in self.chosen_options if i not in user_lost]

            # dictionary for printing multiple game outcomes
            results = {'Lose': f'Sorry, but the computer chose {computer_choice}',
                       'Draw': f'There is a draw ({computer_choice})',
                       'Win': f'Well done. The computer chose {computer_choice} and failed'}

            # goes through gaming options & adds to score when necessary
            if user_input == computer_choice:
                print(results['Draw'])
                self.user_score += 50
            elif computer_choice not in user_lost:
                print(results['Win'])
                self.user_score += 100
            else:
                print(results['Lose'])


play = RoShamBo()
