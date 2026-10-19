
# Problem 13: Sherlock and the Valid String
# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-the-valid-string/problem

from collections import Counter

def isValid(s):
    frequencies = Counter(Counter(s).values())
    unique_counts = list(frequencies.keys())

    if len(unique_counts) == 1:
        return "YES"

    if len(unique_counts) > 2:
        return "NO"

    a, b = sorted(unique_counts)

    # One character occurs once and can be removed.
    if a == 1 and frequencies[a] == 1:
        return "YES"

    # One character occurs exactly one time more than others.
    if b == a + 1 and frequencies[b] == 1:
        return "YES"

    return "NO"


s = input().strip()
print(isValid(s))
