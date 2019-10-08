youguess = False
while youguess == False:
    correct = "Joe Mama"
    question = "Who?"
    print("Who's Joe")
    guess = input()
    numguess = str(guess)
    if (numguess == correct):
        print("Fine, you win :(")
        youguess = True
    elif (numguess == question):
        print("Joe Mama!")
        youguess = True
    else:
        print("No, Joe Mama!:)")
        youguess = True
