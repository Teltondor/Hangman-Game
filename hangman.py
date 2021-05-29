import random
import string
import time


def choose_name():
    name = input(f"Please enter your name:")
    return name.title()


def return_word_choice():
    word_list = ['Abundant', 'Accept', 'Accidentally', 'Accurate', 'Achieve', 'Actor', 'Add', 'Addicted', 'Admire',
                 'Admit',
                 'Adopt', 'Adorable', 'Adventurous', 'Advertisement', 'Advise', 'Afraid', 'Afternoon', 'Aggressive',
                 'Agree',
                 'Airport', 'Alcoholic', 'Alert', 'Allow', 'Aloof', 'Always', 'Ambitious', 'Ambulance', 'Ancient',
                 'Angrily',
                 'Angry', 'Animal', 'Animated', 'Announce', 'Annoying', 'Answer', 'Anxious', 'Apple', 'Appreciate',
                 'Approve',
                 'Argue', 'Army', 'Arrive', 'Arrogant', 'Arrogantly', 'Ashamed', 'Ask', 'Assist', 'Attack',
                 'Attractive',
                 'Auspicious', 'Australia', 'Awesome', 'Awful', 'Bad', 'Badly', 'Bake', 'Balloon', 'Banana', 'Bashful',
                 'Bathe',
                 'Battery', 'Be', 'Beach', 'Beard', 'Beat', 'Beautiful', 'Beautifully', 'Become', 'Bed', 'Beg',
                 'Behave',
                 'Belgium', 'Belligerent', 'Beneficial', 'Best', 'Bet', 'Big', 'Bitter', 'Bitterly', 'Bizarre', 'Black',
                 'Blindly', 'Blue', 'Boast', 'Boil', 'Boldly', 'Boring', 'Borrow', 'Boy', 'Brainy', 'Branch', 'Bravely',
                 'Breakfast', 'Breathe', 'Briefly', 'Bright', 'Bring', 'Broad', 'Broken', 'Brother', 'Build', 'Burn',
                 'Bury',
                 'Busily', 'Busy', 'Buy', 'Call', 'Calm', 'Camera', 'Candle', 'Capable', 'Car', 'Caravan', 'Careful',
                 'Carefully', 'Careless', 'Caring', 'Carpet', 'Cartoon', 'Catch', 'Cautious', 'Certainly', 'Challenge',
                 'Change',
                 'Charming', 'Cheap', 'Cheat', 'Cheerful', 'Chew', 'China', 'Choose', 'Chubby', 'Church', 'Clap',
                 'Clean',
                 'Clean', 'Clearly', 'Clever', 'Clumsy', 'Cold', 'Collect', 'Colorful', 'Comfortable', 'Compare',
                 'Complain',
                 'Concerned', 'Confess', 'Confuse', 'Confused', 'Construct', 'Control', 'Copy', 'Count', 'Courageously',
                 'Crayon', 'Create', 'Crowd', 'Crowded', 'Cruel', 'Cruelly', 'Cry', 'Curious', 'Curiously', 'Curly',
                 'Cute',
                 'Daily', 'Damage', 'Damaged', 'Dance', 'Dangerous', 'Dark', 'Daughter', 'Death', 'Deep', 'Defective',
                 'Delicate', 'Delicious', 'Delightfully', 'Deliver', 'Denmark', 'Depressed', 'Destroy', 'Determined',
                 'Diamond',
                 'Different', 'Dinner', 'Dirty', 'Disagree', 'Disease', 'Disgusting', 'Doctor', 'Dog', 'Drag', 'Dream',
                 'Dress',
                 'Drive', 'Drop', 'Dry', 'Dusty', 'Early', 'Earn', 'Easily', 'Easter', 'Eat', 'Educated', 'Efficient',
                 'Egg',
                 'Eggplant', 'Egypt', 'Elderly', 'Elegant', 'Elephant', 'Embarrassed', 'Employ', 'Empty', 'Encourage',
                 'Encouraging', 'Energy', 'Engine', 'England', 'Enjoy', 'Enthusiastic', 'Enthusiastically', 'Establish',
                 'Estimate', 'Evening', 'Eventually', 'Exactly', 'Excellent', 'Excitedly', 'Exciting', 'Exercise',
                 'Expand',
                 'Expensive', 'Explain', 'Extremely', 'Eye', 'Fabulous', 'Fair', 'Fairly', 'Faithful', 'Faithfully',
                 'Family',
                 'Famous', 'Fancy', 'Fantastic', 'Fast', 'Fast', 'Fear', 'Fearful', 'Fearless', 'Feel', 'Fertile',
                 'Fight',
                 'Filthy', 'Find', 'Finland', 'Fish', 'Flag', 'Flower', 'Fly', 'Foolish', 'Foolishly', 'Football',
                 'Forest',
                 'Forget', 'Forgetful', 'Forgive', 'Fortunately', 'Fountain', 'France', 'Frankly', 'Friendly', 'Fry',
                 'Funny',
                 'Furniture', 'Garage', 'Garden', 'Gas', 'Gather', 'Generally', 'Generously', 'Gentle', 'Gently', 'Get',
                 'Ghost',
                 'Girl', 'Give', 'Glamorous', 'Glass', 'Glorious', 'Glow', 'Gold', 'Gorgeous', 'Graceful', 'Gracefully',
                 'Grass',
                 'Grateful', 'Great', 'Greece', 'Greedy', 'Green', 'Greet', 'Grow', 'Guess', 'Guitar', 'Hair',
                 'Hamburger',
                 'Handsome', 'Happily', 'Happy', 'Harass', 'Harsh', 'Hate', 'Healthy', 'Hear', 'Heavy', 'Helicopter',
                 'Helmet',
                 'Help', 'Helpful', 'Highly', 'Hilarious', 'Historical', 'Hit', 'Holiday', 'Honestly', 'Honey', 'Hope',
                 'Hopelessly', 'Horrible', 'Horse', 'Hospital', 'Hot', 'House', 'Huge', 'Humorous', 'Hungry',
                 'Hydrogen', 'Ice',
                 'Identify', 'Ignorant', 'Illegal', 'Imaginary', 'Immediately', 'Impolite', 'Important', 'Impossible',
                 'Innocent', 'Innocently', 'Insect', 'Instantly', 'Insurance', 'Intelligent', 'Interesting',
                 'Interestingly',
                 'Interrupt', 'Introduce', 'Iron', 'Irritate', 'Island', 'Jackal', 'Jealous', 'Jealously', 'Jelly',
                 'Jewellery',
                 'Jolly', 'Jordan', 'Joyfully', 'Juice', 'Juicy', 'Jump', 'Juvenile', 'Kangaroo', 'Keep', 'Kick',
                 'Kind',
                 'Kindly', 'King', 'Kiss', 'Kitchen', 'Kite', 'Knife', 'Lamp', 'Large', 'Laugh', 'Lawyer', 'Lazily',
                 'Learn',
                 'Leather', 'Leave', 'Legal', 'Lend', 'Less', 'Library', 'Lie', 'Light', 'Lighter', 'Like', 'Lion',
                 'Listen',
                 'Literate', 'Little', 'Lively', 'Lizard', 'Lock', 'London', 'Lonely', 'Lose', 'Loud', 'Loudly', 'Love',
                 'Lovely', 'Lovingly', 'Loyally', 'Lucky', 'Lunch', 'Machine', 'Macho', 'Madly', 'Magazine', 'Magical',
                 'Magician', 'Magnificent', 'Make', 'Manchester', 'Market', 'Marry', 'Massive', 'Match', 'Mature',
                 'Mean',
                 'Measure', 'Meet', 'Messy', 'Microphone', 'Modern', 'Monkey', 'More', 'Morning', 'Motorcycle', 'Move',
                 'Murder',
                 'Mysteriously', 'Nail', 'Napkin', 'Narrow', 'Nasty', 'Naturally', 'Naughty', 'Nearly', 'Needle',
                 'Nervous',
                 'Nervously', 'Nest', 'Never', 'New', 'Nigeria', 'Night', 'Noisy', 'Notebook', 'Nutritious', 'Obedient',
                 'Obediently', 'Obese', 'Obey', 'Obnoxious', 'Ocean', 'Offend', 'Offer', 'Officially', 'Often', 'Oil',
                 'Old',
                 'Open', 'Openly', 'Orange', 'Overconfident', 'Oxygen', 'Oyster', 'Painfully', 'Paint', 'Painting',
                 'Parrot',
                 'Patiently', 'Pay', 'Peaceful', 'Pencil', 'Piano', 'Pick', 'Pillow', 'Pink', 'Pizza', 'Planet',
                 'Plastic',
                 'Play', 'Polite', 'Politely', 'Poor', 'Poorly', 'Portugal', 'Positively', 'Potato', 'Powerful', 'Pray',
                 'Precious', 'Pretty', 'Print', 'Properly', 'Proud', 'Pull', 'Punch', 'Punish', 'Purchase', 'Push',
                 'Queen',
                 'Quick', 'Quickly', 'Quiet', 'Quietly', 'Quill', 'Quit', 'Race', 'Rain', 'Rainbow', 'Raincoat',
                 'Rapid', 'Rare',
                 'Rarely', 'Read', 'Really', 'Red', 'Refrigerator', 'Regularly', 'Relax', 'Reluctantly', 'Remarkable',
                 'Remember', 'Repeatedly', 'Reply', 'Responsible', 'Restaurant', 'Retire', 'Rich', 'River', 'Rocket',
                 'Romantic',
                 'Room', 'Rose', 'Royal', 'Rub', 'Rude', 'Rudely', 'Russia', 'Sadly', 'Safely', 'Sandwich', 'School',
                 'Scintillating', 'Scooter', 'Secretive', 'See', 'Seldom', 'Select', 'Selfish', 'Selfishly', 'Sell',
                 'Send',
                 'Serious', 'Seriously', 'Shampoo', 'Sharp', 'Shiny', 'Shocking', 'Shoe', 'Short', 'Shy', 'Silently',
                 'Silly',
                 'Sincere', 'Sing', 'Skinny', 'Slim', 'Slow', 'Slowly', 'Small', 'Snore', 'Soccer', 'Soft', 'Softly',
                 'Sometimes', 'Soon', 'Spicy', 'Spiritual', 'Splendid', 'Spoon', 'Stand', 'Stare', 'Start', 'Stink',
                 'Stone',
                 'Strictly', 'Strong', 'Study', 'Successful', 'Suddenly', 'Sugar', 'Surprisingly', 'Sweden', 'Sweep',
                 'Sweet',
                 'Sweetly', 'Swim', 'Take', 'Talented', 'Talk', 'Tall', 'Tasty', 'Teach', 'Teacher', 'Tear',
                 'Telephone',
                 'Television', 'Tell', 'Tense', 'Tent', 'Terrible', 'Terribly', 'Terrific', 'Thailand', 'Thank',
                 'Thankfully',
                 'Thick', 'Thin', 'Thoughtfully', 'Tiny', 'Tomato', 'Tomorrow', 'Toothbrush', 'Traffic', 'Train',
                 'Travel',
                 'Truck', 'Type', 'Uganda', 'Ugly', 'Umbrella', 'Understand', 'Unexpectedly', 'Unfortunately', 'Unique',
                 'Untidy', 'Upset', 'Urgently', 'Use', 'Usually', 'Valiantly', 'Van', 'Vase', 'Vegetable', 'Very',
                 'Victorious',
                 'Violent', 'Violently', 'Visit', 'Vulgar', 'Vulture', 'Wait', 'Walk', 'Wall', 'Want', 'Warm', 'Warn',
                 'Weak',
                 'Wealthy', 'Wed', 'Weep', 'Well', 'Whale', 'Wide', 'Window', 'Wink', 'Wire', 'Wise', 'Wisely', 'Witty',
                 'Wonderful', 'Worried', 'Worry', 'Write', 'Xylophone', 'Yacht', 'Yak', 'Yearly', 'Yell', 'Yesterday',
                 'Young',
                 'Youthful', 'Zealous', 'Zebra', 'Zoo']
    short_list = []
    word_acceptable = False
    print("First, I want to define how you want to play today \n")
    print("Enter how many characters you wish the word to be (Must be between 2-13)\n")
    while not word_acceptable:
        num_characters = input("ENTER HERE:")
        if num_characters in ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']:
            print("Good choice! Continuing...")
            num_characters = int(num_characters)
            word_acceptable = True
        else:
            print("Invalid entry. Must be a number between 2 and 13.")
    for word in word_list:
        if len(word) == num_characters:
            short_list.append(word)
    chosen_word = random.choice(short_list).upper()
    return chosen_word


def game_round(player_word):
    guesses_remaining = True
    guessed_correctly = False
    guess_list = []
    guess = ""
    num_guesses = 0
    # while statement that runs as long as the user has guesses left AND they have not guessed the word correctly
    while guesses_remaining and not guessed_correctly:
        valid_guess = False
        # while statement that runs to capture the user guess and handle invalid entries. Allows guessing the word
        while not valid_guess:
            time.sleep(0.25)
            guess = input("Type 'guess' if you want to guess the whole word \n Otherwise, enter one letter that you "
                          "guess is in the word:").upper()
            time.sleep(0.5)
            if guess in string.ascii_letters:
                print(f'You guessed {guess}')
                time.sleep(0.5)
                valid_guess = True
            elif guess.upper() == "GUESS":
                time.sleep(0.25)
                word_guess = input("Enter your guess for the word:").upper()
                time.sleep(0.25)
                print(f'{word_guess} is your guess.')
                if word_guess == player_word:
                    time.sleep(0.5)
                    print(f"You are correct!")
                    time.sleep(0.5)
                    guessed_correctly = True
                    guesses_remaining = False
                    valid_guess = True
                else:
                    time.sleep(0.25)
                    print("Unfortunately, that guess is wrong.")
                    valid_guess = True
            else:
                print("INVALID ENTRY")
                continue
        # adds the guess to the list of guesses IF it was not a full word guess
        if len(guess) == 1:
            guess_list.append(guess)
        # checks if guess is in the word,presents the word with letters, otherwise tells the user invalid
        if guess in player_word.upper():
            result = []
            count = player_word.count(guess)
            for i in player_word:
                if i in guess_list:
                    result.append(i)
                else:
                    result.append("_")
            new_word = "".join(result)
            time.sleep(0.5)
            print(f'This letter is found {count} time(s)')
            time.sleep(0.5)
            print(new_word)
        else:
            if len(guess) == 1:
                result = []
                time.sleep(0.5)
                print("Your guess is not in the word")
                for i in player_word:
                    if i in guess_list:
                        result.append(i)
                    else:
                        result.append("_")
                new_word = "".join(result)
                print(new_word)
        # adds to the guess count
        num_guesses += 1
        # lets the user know the number of guesses remaining, and what has been guessed IF the game is not over
        if guesses_remaining or not guessed_correctly:
            time.sleep(0.5)
            print(f"Your guesses so far: {guess_list}")
            time.sleep(0.5)
            print(f'You have {10-num_guesses} guesses remaining')
        # checks to see if there are guesses remaining
        if num_guesses >= 10:
            guesses_remaining = False
        print("\n")
    print(f"The word was {player_word}. Thank you for playing!")







