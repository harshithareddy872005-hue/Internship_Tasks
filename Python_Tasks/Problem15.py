
# Problem 15: Game of Thrones - I
# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

s = input().strip()
counts = Counter(s)

odd_counts = sum(1 for count in counts.values() if count % 2 != 0)

if odd_counts <= 1:
    print("YES")
else:
    print("NO")
