import re
import fileinput


def parse(line):
    return re.findall(r"[\w']+", line)


players = {}

for line in fileinput.input():

    n1, n2, n3, n4, ga, gb = parse(line)

    print n1
    print n2
    print n3
    print n3
    print ga
    print gb

    p1 = float(players.get(n1, 1000))
    p2 = float(players.get(n2, 1000))
    p3 = float(players.get(n3, 1000))
    p4 = float(players.get(n4, 1000))

    pot = p1 * 0.1 + p2 * 0.1 + p3 * 0.1 + p4 * 0.1

    p1AwardPercentage = p1/(p1+p2)
    p2AwardPercentage = p2/(p1+p2)
    p3AwardPercentage = p3/(p3+p4)
    p4AwardPercentage = p4/(p3+p4)

    p1 = p1 * 0.9
    p2 = p2 * 0.9
    p3 = p3 * 0.9
    p4 = p4 * 0.9

    pot_per_goal = pot / (float(ga) + float(gb))

    players[n1] = p1 + pot_per_goal * int(ga) * p1AwardPercentage
    players[n2] = p2 + pot_per_goal * int(ga) * p2AwardPercentage
    players[n3] = p3 + pot_per_goal * int(gb) * p3AwardPercentage
    players[n4] = p4 + pot_per_goal * int(gb) * p4AwardPercentage

print players
