
# Problem 5: Alternating Characters
# HackerRank: https://www.hackerrank.com/challenges/alternating-characters/problem

def alternatingCharacters(s):
    deletions = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1

    return deletions


t = int(input())

for _ in range(t):
    s = input().strip()
    print(alternatingCharacters(s))
