'''
You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest 
overall score. The score of the team is the sum of scores of all the players in the team.
However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly 
higher score than an older player. A conflict does not occur between players of the same age.
Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, 
respectively, return the highest overall score of all possible basketball teams.

Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.

Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that 
you are allowed to choose multiple people of the same age.

Input: scores = [1,2,3,5], ages = [8,9,10,1]
Output: 6
Explanation: It is best to choose the first 3 players. 
'''

scores = [4,5,6,5]
ages = [2,1,2,1]

def bestTeamScore():
    total_score = 0
    zipped = zip(ages, scores)
    zipped = list(zipped)
    print(zipped)
    res = sorted(zipped, key=lambda x: x[0])    # list with ages in ascending order
    print(res)
    a, sc = list(zip(*res))
    print(a, sc)
    smallest_score = min(sc)
    for n in sc():
        if n[0:] == smallest_score:
            sc.remove(n)
    for s in sc:
        total_score += s
    return total_score

bestTeamScore()