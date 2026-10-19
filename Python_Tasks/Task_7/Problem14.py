
# Problem 14: Anagram
# HackerRank: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

def anagram(s):
    if len(s) % 2 != 0:
        return -1

    mid = len(s) // 2
    first = Counter(s[:mid])
    second = Counter(s[mid:])

    changes = 0

    for char, count in first.items():
        if count > second[char]:
            changes += count - second[char]

    return changes


q = int(input())

for _ in range(q):
    s = input().strip()
    print(anagram(s))
