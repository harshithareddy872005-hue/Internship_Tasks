
# Problem 4: Funny String
# HackerRank: https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    n = len(s)

    for i in range(1, n):
        left = abs(ord(s[i]) - ord(s[i - 1]))
        right = abs(ord(s[n - i]) - ord(s[n - i - 1]))

        if left != right:
            return "Not Funny"

    return "Funny"


t = int(input())

for _ in range(t):
    s = input().strip()
    print(funnyString(s))
