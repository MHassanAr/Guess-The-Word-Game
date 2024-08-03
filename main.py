import random

# Function to write the list of words and hints to a file
def writeToFile(fileName):
    # Multi-line string containing words and their hints
    wordsAndHints = """
    apple - A common fruit, often red or green.
    banana - A yellow fruit that monkeys love.
    carrot - A crunchy orange vegetable.
    dog - Man's best friend.
    elephant - The largest land animal.
    fish - Lives in water and has gills.
    giraffe - Animal with a very long neck.
    house - A place where people live.
    igloo - A type of house made of ice.
    jacket - Worn to keep warm in winter.
    kite - Flies in the sky, controlled by a string.
    lion - Known as the king of the jungle.
    mountain - A large, natural elevation of the earth's surface.
    nurse - A healthcare professional.
    ostrich - A large bird that cannot fly.
    penguin - A flightless bird often found in Antarctica.
    """
    
    # Open the file in write mode and write the words and hints
    with open(fileName, "w") as wordFile:
        wordFile.write(wordsAndHints)

# Function to read a random word and hint from the file
def readFromFile(fileName):
    # Open the file in read mode
    with open(fileName, "r") as wordFile:
        # Read all lines from the file
        lines = wordFile.readlines()
        # Choose a random line and strip any leading/trailing whitespace
        randomLine = random.choice(lines).strip()
        # Split the line into the word and hint
        randomWord, randomHint = randomLine.split(" - ")
    return randomWord, randomHint
    
def main():
    print("Welcome! Let's play a word guessing game.")
    
    fileName = "wordFile.txt"

    # Write the words and hints to the file
    writeToFile(fileName)
    
    # Read a random word and hint from the file
    randomWord, randomHint = readFromFile(fileName)

    # Convert the random word to a list of characters
    wordList = list(randomWord)

    # Set the number of guesses to the length of the word plus three
    guesses = len(wordList) + 3

    print(f"\nHint!!: {randomHint.strip()}")
    print(f"\nYou have {guesses} chances to guess it right.")
    
    # Loop until the player runs out of guesses
    while guesses != 0:
        alphabet = input("\nEnter alphabet: ").lower()
        
        # Validate input
        while not alphabet.isalpha() or len(alphabet) != 1:
            print("Invalid input. Please enter a single alphabet.")
            alphabet = input("\nEnter alphabet: ").lower()
        
        # Check if the entered alphabet is in the word list
        if alphabet in wordList:
            print(alphabet)
            wordList.remove(alphabet)
            
            # If the word list is empty, the player has guessed the word
            if not wordList:
                print(f"Congrats!! You guessed the word \"{randomWord}\" right.")
                break
        
        else:
            print("Wrong Alphabet!!")
            guesses -= 1
    
    # If the player runs out of guesses and hasn't guessed the word
    if guesses == 0 and wordList:
        print(f"\nSorry, you've run out of guesses. The word was: \"{randomWord}\"")

# Call the main function to start the game
main()
