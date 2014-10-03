Simple script to calculate individual foosball rankings based on the results of 2vs2 games

The algorithm is very naive.   Initially each player has 1000 points and in each game you puts in the pot 10% of your points.    Those points are distributed proportionally to the number of goals scored by your team.  (if the result is 5-3 the winning team gets 5/8 of the pot).   Both players in the same team gets the same amount of points.

Just store the results in db.txt with a row per game with the format:
```
name1/name2-name3/4 goalsA-goalsB
```

And run the script with that input data:
```
python trueskill.py < db.txt
```