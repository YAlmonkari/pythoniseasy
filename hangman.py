passphrase = input("Give a passphrase: ")
print(chr(27) + "[2J")

lists = list(passphrase)
j=1
guesslist = []
guesses = []


for i in range(0,len(lists)):
    guesslist.append("_ ")
for i in range(0,len(lists)):
    print(guesslist[i], end="")

while i <= 7:
    letter = input("Chose a letter: ")
    if letter in lists:
        True
    else:
        guesses.append(letter)
    for i in range(0,len(lists)):
        if letter == lists[i]:
            if guesslist[i] == "_ ":
                guesslist[i] = letter+" "
    for i in range(0,len(lists)):     
        if guesslist[i] != "_ ":
            ok = True 
        else:
            ok = False
            break
    if letter in lists:
        j = j
    else:
        j+=1
    if ok:
        print("You won!")
    for i in range(0,len(lists)):
        print(guesslist[i],end="")
    for i in range(0,len(guesses)):
            print(guesses[i]+" ", end="")
    if j == 1:
        print("")
        print("")
        print("     ------|")
        print("     |     |")
        print("           |")
        print("           |")
        print("           |")
        print("           |")
        print("           |")
        print("------------")
    elif j == 2:
        print("")
        print("")
        print("     ------|")
        print("     |     |")
        print("     o     |")
        print("           |")
        print("           |")
        print("           |")
        print("           |")
        print("------------")
    elif j == 3:
        print("")
        print("")
        print("     ------|")
        print("     |     |")
        print("     o     |")
        print("     |     |")
        print("           |")
        print("           |")
        print("           |")
        print("------------")
    elif j == 4:
        print("")
        print("")
        print("     ------|")
        print("     |     |")
        print("     o     |")
        print("     |\    |")
        print("           |")
        print("           |")
        print("           |")
        print("------------")
    elif j ==5:
        print("")
        print("")
        print("     ------|")
        print("     |     |")
        print("     o     |")
        print("    /|\    |")
        print("           |")
        print("           |")
        print("           |")
        print("------------")
    elif j == 6:
        print("")
        print("")
        print("     ------|")
        print("     |     |")
        print("     o     |")
        print("    /|\    |")
        print("     \     |")
        print("           |")
        print("           |")
        print("------------")    
    elif j == 7:
        print("")
        print("")
        print("     ------|")
        print("     |     |")
        print("     o     |")
        print("    /|\    |")
        print("    /\     |")
        print("           |")
        print("           |")
        print("------------")    
    if ok:
        break
    input("Press enter to continue.")
if ok == False:
    print("You lose.")