#There is a large pile of socks that must be paired by color. 
#Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
def sockMerchant(n, ar):
    freq = {}
    for color in ar:
        if color in freq:
            freq[color] += 1
        else:
            freq[color] = 1

    pairs = 0

    for color in freq:
        pairs += freq[color] // 2

    return pairs



n = 7
arr = [1, 2, 1, 2, 1, 3, 2]
print(sockMerchant(n, arr))