import pandas as pd

def getOpponent(game):
    deck= game['opponent_deck'] if  game['opponent_deck'] is not None else 'Unknown'
    return str(deck+' '+game['opponent'])
def resultConvertWins(game,play):#Returns 1 if the player who played the card won
    if game['result']=='win' and play['player'] == 'me':return 1
    elif game['result']=='loss' and play['player'] == 'opponent':return 1
    else: return 0  
def resultConvertLosses(game,play):#Returns 1 if player who played the card lost
    if resultConvertWins(game,play)==0:return 1
    else: return 0

wins =[0] * 50 #max possible length of hs = 50 turns
losses = [0] * 50 #Allocating the list ahead of time to preserve the turn order

def checkPlay(game,play):
    #Code will run for every card played
    if(len(play)<1):return
    if play['card']['id']=='CFM_637' :#If certain card was played
        wins[play['turn']-1]+=resultConvertWins(game,play)#Check if that player won or lost, put the result in the array
        losses[play['turn']-1]+=resultConvertLosses(game,play)
       
def analyzeData(data,output):
    print('Analyzing Data')
    #CODE BELOW TO ANALYZE THE DATA
    #Currently will calculate winrate for any card based on the turn it is played
    gamesDF =pd.DataFrame(list(data))#Data frame containing each game
    ranked = gamesDF[gamesDF['mode']=='ranked']
    for index,game in ranked.iterrows():#For each game
        for i,play in enumerate(game['card_history']):#For each card played (card history = array of turns)
            checkPlay(game,play)#check the play. Takes the play itself and the game as a whole for reference
    winrates = [0] *50
    for i in range(len(wins)-1):
        if wins[i]>1 or losses[i] >1:
            winrates[i]=(round(wins[i]/(wins[i]+losses[i])*100))
    i=len(winrates)-1
    while winrates[i]==0:
        i-=1#Remove datapoints where nobody played the card
    winrates = winrates[0:i+1]
    print(winrates)#Winrates in % for each turn 
    #winrates[0] is the winrate of players who played card on turn 1
    with open(output, encoding = 'utf8', mode='w') as myfile:#Export winrates to data
        myfile.writelines(['{"data": '+str(winrates)+'}'])
        myfile.close()