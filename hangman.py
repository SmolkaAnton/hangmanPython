#Very basic hangman game

from random import randint

#Main function
def main():
    animals = ["dog", "cat", "horse", "lion", "kangaroo", "parrot", "panda", "turle", "elephant", "tiger", "llama"]
    adjectives = ["athletic", "happy", "sad", "fit", "dazzling", "magnificent", "mad", "lively", "petite", "brave", "thoughtful"]
    states = ["alabama", "california", "delaware", "arizona", "nevada", "newyork", "northcarolina", "texas", "tennessee", "florida", "colorado"]

    num = choose_word()
    cat = choose_category()
    
    if(cat==1):
        category = "Animals"
        word_generated = list(animals[num]) #Chooses word from list user has to guess
        playGame(word_generated, category)
    elif(cat==2):
        category = "Adjectives"
        word_generated = list(adjectives[num]) #Chooses word from list user has to guess
        playGame(word_generated, category)
    else:
        category = "States"
        word_generated = list(states[num]) #Chooses word from list user has to guess
        playGame(word_generated, category)

#function used to generate random number to choose word
def choose_word():
    num = randint(0, 10)
    return num

#Function used to generate number to choose category
def choose_category():
    num = randint(1,3)
    return num

#Function used to play game
def playGame(word_generated, category):
    display = []
    used = []

    #Adds the generated word to the list
    display.extend(word_generated)
    used.extend(display)

    #This will add _ to the display array
    for i in range (len(display)):
        display[i]= "_"

    #Adds spaces between each _
    print(" ".join(display))
    print("Category is: ", category)
    print()

    #Counter for guesses
    count = 0
    #Counter for incorrect guesses
    incorrect = 5
    while(count < len(word_generated) and incorrect >=0):
        guess = input("Guess a letter ")
        guess.lower()

        #iterate through the generated word
        for i in range (len(word_generated)):
            if(word_generated[i]==guess and guess in used):
                display[i]=guess
                count += 1
                used.remove(guess)

        if guess not in display:
            print("Sorry, wrong guess. You have ", incorrect, " guesses left!")
            incorrect -= 1

        print("You have guessed: ", count, " correct letters.")
        print("Category is: ", category)
        print(" ".join(display))
        print()

    if(count == len(word_generated)):
        print("You guessed the word!")
    else:
        print("Sorry, you didn't guess the word!")

main()
