class Bowling:
    def __init__(self, player):
        self.player = player
        self.game=[]
        self.scoreTot = 0
        self.mult = 1


    def nwFrm(self, score1, score2):
        self.game.append((score1, score2))
        #TODO: increment score
        if(score1+score2 < 10):
            self.scoreTot += score1+score2
        elif(score1 == 10):
            #STRIKE RULES
            print("STRIKE!")
            self.mult += 1
        else:
            #SPARE RULES
            print("Way to pick up the spare!")
            self.mult+=1
        print("{0}'s score is now {1}".format(self.player, self.scoreTot))
i=0
p1 = Bowling(input('Enter player 1 name: '))

while(i < 9):
    f1, f2 = map(int, input('Enter two scores for frame: \n').split())
    p1.nwFrm(f1, f2)
    i+=1