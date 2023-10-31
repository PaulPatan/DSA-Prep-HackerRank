# There is a new mobile game that starts with consecutively numbered clouds. 
# Some of the clouds are thunderheads and others are cumulus. 
# The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . 
# The player must avoid the thunderheads. 
# Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. 
# It is always possible to win the game.
# Example:
# n=6
# c = [0,0,0,0,1,0]
# The only thundercloud to avoid is c[4] . The game can be won in 3 jumps:


def jumpingOnClouds(c):
    j = 0
    i = 0
    n = len(c)
    while i < n - 1:
        if i + 2 < n and c[i + 2] == 0:
            i += 1
        i += 1
        j += 1
    return j

n=6
c = [0,0,0,0,1,0]
print(jumpingOnClouds(c))