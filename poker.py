# Python course -  Projeckt 3 - card game

from random import shuffle
cardDeck= []
cards= ["9","10","J","Q","K","A"]
for  i in range(4):
    if i == 0:
        for j in cards:
            j = j + "spades"
            cardDeck.append(j)
    elif i == 1:
        for j in cards:
            j = j + "hearts"
            cardDeck.append(j)
    elif i == 2:
        for j in cards:
            j = j + "diamonds"
            cardDeck.append(j)
    elif i == 3:
        for j in cards:
            j = j + "clubs"
            cardDeck.append(j)
shuffle(cardDeck)
print(cardDeck)

class Player:
    def __init__(self,name = "Player", hand = [], bet = 0, money = 100):
        self.name = name
        self.hand = hand
        self.bet = bet
        self.money = money
        #how many cards do you want to swap
            #pops 5 card from the deck
    def getCards(self):
        self.hand.append(cardDeck.pop())
        self.hand.append(cardDeck.pop())
        self.hand.append(cardDeck.pop())
        self.hand.append(cardDeck.pop())
        self.hand.append(cardDeck.pop())
    def start(self):
        global Player1
        global Player2
        Player1 = input("What is Players 1 name: ")
        if Player1 == "--help":
            self.Help()
        else:
            Player1 = Player(Player1)
            Player1.getCards()
            print(Player1.hand)
            print(cardDeck)
        Player2 = input("What is Players 2 name: ")
        if Player2 == "--help":
            self.Help()
        else:
            Player2 = Player(Player2)
            Player2.getCards()
            print(Player2.hand)
            print(cardDeck)
    def betMoney(self, bet):
        self.money -= self.bet
    def win(self):
        self.money += 2*self.bet
    def lissen(self):
        Input = input("Wellcome to the game of poker! Type --help for help. Enter any key to continue.")
        if Input == "--help":
            self.Help()
        else:
            global players
            players = input("How many players want to play? ")
            if players == "0":
                print("No players")
            elif players == "1":
                print("Not enougth players. ")
            elif players == "2":
                self.start()
            elif players == "--help":
                self.Help()
    def Help(self):
        Help = input("Game of poker is this and that. Type --resume to resume.")
        if Help == "--resume":
            self.resume()
        else:
            self.Help()
    def resume(self):
        if players == "" or players=="--help":
            self.lissen()
        else:
            self.start()
    def __str__(self):
        return ("Player "+ str(self.name)+" hand "+ str(self.hand))
House = Player("House")
House.lissen()
print(Player1)
print(Player2)