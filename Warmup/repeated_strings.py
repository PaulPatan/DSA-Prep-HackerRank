# There is a string, , of lowercase English letters that is repeated infinitely many times. 
# Given an integer, , find and print the number of letter a's in the first  letters of the infinite string.

def repeatedString(s,n):
    if s == 'a':
        return n
    else:
        nr = 0
        for i in range(0, len(s)):
            if s[i] == 'a':
                nr +=1
    nr *= int(n/len(s))
    for i in range(0, int(n%len(s))):
        if s[i] =='a':
            nr += 1
    return nr


s="aba"
n=10
print(repeatedString(s,n))