import hangman as execute

player = execute.choose_name()  # enters the player name as variable

chosen_word = execute.return_word_choice()  # players chooses word length, returns a random word matching that

print(f"Excellent, now let's play {player}\n"
      f"I have chosen my word. You will have 10 guesses")

execute.game_round(chosen_word) # main logic --> accepts the word as the input and walks the user through the game
