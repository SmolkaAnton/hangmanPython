#Very basic hangman game

from random import randint

#Main function
def main():
    words = ["hello", "world", "test"]
    num = random()
    word_generated = list(words[num]) #Chooses word from list user has to guess
    playGame(word_generated)

#function used to generate random number
def random():
    num = randint(0, 2)
    return num

#Function used to play game
def playGame(word_generated):
    #Counter for guesses
    counter = 0
    display = []

    #Adds the generated word to the list
    display.extend(word_generated)

    #This will add _ to the display array
    for i in range (len(display)):
        display[i]= "_"

    #Adds spaces between each _
    print(" ".join(display))
    print()

    while(counter<=len(word_generated)):
        guess = input("Guess a letter ")
        guess.lower()
        print(counter)

        #iterate through the generated word
        for i in range (len(word_generated)):
            if(word_generated[i]==guess):
                display[i]=guess
                counter+=1

        print(" ".join(display))
        print()

    print("You guessed the word!")

main()
