"""
This program solves the following problem
----
We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:

{'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42},
'match3':{'player2':41, 'player4':63, 'player3':91}

Each match is identified by a string, as is each player.  The scores are all integers.  The names associated with the
matches are not fixed (here they are 'match1','match2','match3'), nor are the names of the players. A player need not
have a score recorded in all matches

Define a Python function "orangecap(d)" that reads a dictionary d of this form and identifies the player with the
highest total score.  Your function should return a pair (playername,topscore) where playername is a string, the name of
the player with the highest score, and topscore is an integer, the total score of playername.

The input will be such that there are never any ties for highest total score.

"""

def orangecap(d):
    matchscores = []
    dictvalues = d.values()
    matchscores = list(dictvalues)
    allplayers = []
    scores = dict()

    for i in range(0,len(matchscores)):
        temp = list(matchscores[i].keys())
        for j in range(0,len(temp)):
            allplayers.append(temp[j])

    players = sorted(set(allplayers))

    for player in players:
        for i in range(0,len(matchscores)):
            if player in matchscores[i]:
                if player in scores:
                    scores[player] += matchscores[i][player]
                else:
                    scores[player] = matchscores[i][player]

    (playername, totalscore) = ('player1', 0)
    for player in scores:
        if scores[player] > totalscore:
            playername,totalscore = player, scores[player]

    return (playername, totalscore)
