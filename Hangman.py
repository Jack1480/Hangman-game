# Hangman game
import random
import string

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------
wordlist = loadWords()


def is_word_guessed(secret_word, letters_guessed):

    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    c = 0
    for i in letters_guessed:
        if i in secret_word:
            c += 1
    if c == len(secret_word):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = []
    for i in secret_word:
        if i in letters_guessed:
            s.append(i)
    ans = ''
    for i in secret_word:
        if i in s:
            ans += i
        else:
            ans += '_ '
    return ans


def get_available_letters(letters_guessed):
    lowercase = string.ascii_lowercase
    a = []
    for char in lowercase:
        if char not in letters_guessed:
            a.append(char)
    return ''.join(a)


def hangman(secret_word):

    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    global letters_guessed
    warning = 0
    mistakeMade = 0
    letters_guessed = []

    print("Welcome to the game, Hangman!")
    print("You have 3 warning left")
    print("I am thinking of a word that is", len(secret_word), "letters long.")



    while 6 - mistakeMade > 0:

        if is_word_guessed(secret_word, letters_guessed):
            print("-------------")
            print("Congratulations, you won!")
            break

        else:
            print("-------------")
            print("You have", 6 - mistakeMade, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            guess = str(input("Please guess a letter: ")).lower()

            if guess in letters_guessed:
                print("Oops! You've already guessed that letter:" + "you have {} warnings left: ".format(warning),get_guessed_word(secret_word, letters_guessed))
            if guess not in string.ascii_lowercase:
                warning += 1
                print("Please enter a valid alphabet to guess a word."+ "You have {} warning left:".format(warning) ,
                      get_guessed_word(secret_word, letters_guessed))

            elif guess in secret_word and guess not in letters_guessed:
                letters_guessed.append(guess)
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))

            else:
                letters_guessed.append(guess)
                mistakeMade += 1
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

        if 6 - mistakeMade == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.", secret_word)
            break

        else:
            continue


def match_with_gaps(my_word, other_word):
    num = 0
    my_word = my_word.replace(' ', '')
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] == '_' or my_word[i] == other_word[i]:
                pass
            else:
                num += 1
        if num == 0:
            return True
        else:
            return False
    else:
        return False


# print(match_with_gaps("ta_ b", "tacg"))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    list = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            list.append(word)

    if len(list) != 0:
        print(' '.join(list))
    else:
        print('No matches found')


# show_possible_matches("t_ _ t")

def hangman_with_hints(secret_word):
    print("Welcome to the game, Hangman!")
    print("You have 3 warnings left")
    print("I am thinking of a word that is", len(secret_word), "letters long.")

    global letters_guessed
    warning = 0
    mistakeMade = 0
    letters_guessed = []

    while 6 - mistakeMade > 0:

        if is_word_guessed(secret_word, letters_guessed):
            print("-------------")
            print("Congratulations, you won!")
            break

        else:
            print("-------------")
            print("You have", 6 - mistakeMade, "guesses left.")
            print("Available letters:", get_available_letters(letters_guessed))
            guess = str(input("Please guess a letter: ")).lower()


            if guess in letters_guessed:
                print("Oops! You've already guessed that letter:", get_guessed_word(secret_word, letters_guessed))

            if guess not in string.ascii_lowercase:
                warning += 1
                print("Please enter a valid alphabet to guess a word."+ "You have {} warning left:".format(warning) ,
                      get_guessed_word(secret_word, letters_guessed))

            elif guess in secret_word and guess not in letters_guessed:
                letters_guessed.append(guess)
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))

            else:
                letters_guessed.append(guess)
                mistakeMade += 1
                print("Oops! That letter is not in my word:","you have {} warnings left:".format( warning), get_guessed_word(secret_word, letters_guessed))

        if guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))


        if 6 - mistakeMade == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.", secret_word)
            break

        else:
            continue

if __name__ == "__main__":
    #secret_word = choose_word(wordlist).lower()
   # hangman(secret_word)

    secret_word = choose_word(wordlist).lower()
    hangman_with_hints(secret_word)

