youguess = False
while youguess == False:
    guess = input()
    correct = "99"
    numguess = str(guess)
    if (numguess == correct):
        youguess = True
        print ("you got it")
        #once the # is true you can conduct other things here
    else:
        youguess = False
    
