import random
print("$Welcome to Hangman Game!")
def import_dictionary(dictionary_file):
    # counter for key
    counter = 1
    # Opens the file for reading
    with open(dictionary_file) as infile:
        # Creates a empty dictionary
        dictionary = {}
        # Reads the data from file one line at a time
        for line in infile:
            # Remove linebreak which is available as
            # the last character of the record
            line = line[:-1] 
            # Split the data with space
            array = line.split(' ')
            # Sets the key value
            key = counter
            # Makes the key as default for the dictionary
            dictionary.setdefault(key, [])

            # Loops till end of the array
            for word in array:
                # Appends the current word to dictionay key 
                dictionary[key].append(word)
            # Increse the counter by one
            counter = counter + 1
    # returns the dictionary
    return dictionary

# Calls the funtion to get the dicrionary created from file
myDictionary = import_dictionary("dictionary.txt")
play="Y"
while play=="Y":
    wordsize=int(input("$Please choose the size of a word to be guessed[3-12,default any]") or random.choice(["3","4","5","6","7","8","9","10","11","12"]))
    print("Size of word is set to ", + wordsize)
    actlives=int(input("Please choose number of lives [1-10,default 5]") or "5")
    print("You have ",+ actlives,"lives")
    word = random.choice(myDictionary[wordsize])
    guesses = ''
    lives=actlives
    while lives > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print ("$"+char,end=" " )
            else:
                print ("-", end = " ")
                failed += 1
        print ("Letters Choosen:"+guesses)
        print("lives:",+lives,"x"*(actlives-lives)+"O"*lives)
        if failed == 0:
            print ("\n Congratulations!!! You won The word was " + word)
            break
        # Accepts a letter from the user
    guess = input("\n Please choose a new letter: ") 
      
    # Concatenates every user entered guess letter 
    guesses += guess  

    print("\n Letters choosen: ", end = "")
    # Loops till end of the guessed letters and displays it
    for c in guesses:
        print(c, end = ", ")
    print()
    
    # Checks user entered guessed letter with the letters in
    # secret word is not available
    if guess not in word: 
        # Decrease the turn value by one
        lives -= 1
          
        # If the letter entered by the user does not match the
        # secret word then display message
        print("\n You guessed wrong. You lost one life.") 
          
        # Prints number of lives left
        print("\n You have ", + lives, ' lives.') 
          
        # Checks if lives value is equals to 0
        if lives == 0: 
            print("\n You lost! The word is: ", word ) 