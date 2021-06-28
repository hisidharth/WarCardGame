import random

def shuffled_deck():
        basic_deck=list(range(2,8))*4
        random.shuffle(basic_deck)
    
        return basic_deck
def compare(x,y):
        if x>y:
            return("Player1")
        elif x<y:
            return("Player 2")
g_deck= shuffled_deck()
print(g_deck)
player1=g_deck[:4]
print(player1)
player2=g_deck[4:8]
print(player2)
game=True
while game==True:
    if player1==[]:
        print("Player 1 wins")
        game=False
    elif player2==[]:
        print("Player 2 wins")
        game=False
   
    


    
    print("Player 1 drew this,",player1[0])
    print("Player 2 drew this,",player2[0])
    

    result=compare(player1[0],player2[0])
    if result == "Player1":
        player1.append(player1[0])
        player1.append(player2[0])
        player1.pop(0)
        player2.pop(0)
        print("Player 1 had the higher card")
        print(player1)
        print(player2)


    elif result == "Player 2":
        player2.append(player1[0])
        player2.append(player2[0])
        player1.pop(0)
        player2.pop(0)
        print("Player 2 had the higher card")
        print(player1)
        print(player2)
    placeholder=[]
    tie= True
    while tie==True:
        tiecard=0
        if player1==[]:
            print("Player 1 wins")
            game=False
            tie=False
            break
        elif player2==[]:
            print("Player 2 wins")
            game=False
            tie=False
            break
    
        elif player1[tiecard]>player2[tiecard]:
            placeholder.append(player1.pop(0))
            placeholder.append(player2.pop(0))
            player1=player1+placeholder
            placeholder=[]
            tie=False
            ##add all cards into p1 deck
        elif player1[tiecard]<player2[tiecard]:
            placeholder.append(player1.pop(0))
            placeholder.append(player2.pop(0))
            player2=player2+placeholder
            placeholder=[]
            tie=False
            ## add all cards into p2 deck
        
        else:
            placeholder.append(player1.pop(0))
            placeholder.append(player2.pop(0))
        
        
    
       
