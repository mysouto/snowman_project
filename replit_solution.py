SNOWMAN_MIN_WORD_LENGTH = 5
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_WRONG_GUESSES = 7

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \( : )/ *',
    '* (_ : _)  ',
    '-----------',
]


def snowman(snowman_word):
    """Complete the snowman function
    replace "pass" below with your own code
    It should print 'Congratulations, you win!'
    If the player wins and, 'Sorry, you lose! The word was {snowman_word}' if the player loses
    """
    # secret/snowman word selected in main.py file

    snowman_word_dict = build_word_dict(snowman_word)
    wrong_guesses_list = []

    word_complete = False

    while len(
            wrong_guesses_list) < SNOWMAN_WRONG_GUESSES and not word_complete:
        if get_word_progress(snowman_word, snowman_word_dict) == True:
            print(f"You win!")
            word_complete = True
            # do I need to return anything to end the game?
            # -- maybe yes, while loop continues without this return
            # return None
            return word_complete

        letter = get_letter_from_user(wrong_guesses_list, snowman_word_dict)

        if letter in snowman_word_dict:
            snowman_word_dict[letter] = True
        else:
            wrong_guesses_list.append(letter)

        draw_snowman(len(wrong_guesses_list))

        print_word_progress_string(snowman_word, snowman_word_dict)

        wrong_guesses_str = " ".join(wrong_guesses_list)
        print(f"Wrong guesses: {wrong_guesses_str}")

    if word_complete == False:
        print(f"Sorry, you lose! The word was {snowman_word}")


def draw_snowman(wrong_guess_count):
    """This function prints out the appropriate snowman image 
    depending on the number of wrong guesses the player has made.
    """

    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guess_count, SNOWMAN_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])


def get_letter_from_user(wrong_guesses_list, letter_dict):
    """This function takes the snowman_word_dict and the list of characters 
    that have been guessed incorrectly (wrong_guesses_list) as input.
    It asks for input from the user of a single character until 
    a valid character is provided and then returns this character.
    """
    letter_from_user = None
    valid_input = False

    while not valid_input:
        letter_from_user = input("Guess a letter:  ")
        if not letter_from_user.isalpha():
            print("You must input a letter!")
        elif len(letter_from_user) > 1:
            print("You can only input one letter at a time!")
        elif letter_from_user in letter_dict and letter_dict[letter_from_user]:
            print("You have already guessed that letter and it's in the word!")
        elif letter_from_user in wrong_guesses_list:
            print("You have already guessed that letter and it's not in the word!")
        else:
            valid_input = True

    return letter_from_user


def build_word_dict(word):
    """This function takes snowman_word as input and returns 
    a dictionary with a key-value pair for each letter in 
    snowman_word where the key is the letter and the value is `False`.
    """
    letter_dict = {}
    for letter in word:
        if not letter in letter_dict:
            letter_dict[letter] = False
    return letter_dict


def print_word_progress_string(word, letter_dict):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It prints an output_string that shows the correct letter guess placements 
    as well as the placements for the letters yet to be guessed.
    """
    word_progress_string = ""
    for letter in word:
        if letter_dict[letter] == True:
            word_progress_string += letter + " "
        else:
            word_progress_string += "_" + " "
    word_progress_string = word_progress_string.strip()
    print(word_progress_string)


def get_word_progress(word, word_dict):
    """
    This function takes the snowman_word and snowman_word_dict as input.
    It returns True if all the letters of the word have been guessed, and False otherwise.
    """
    for letter in word:
        if word_dict[letter] == False:
            return False
    return True
