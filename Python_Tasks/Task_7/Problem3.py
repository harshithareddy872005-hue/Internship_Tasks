
# Problem 3: Mars Exploration
# HackerRank: https://www.hackerrank.com/challenges/mars-exploration/problem

s = input().strip()
expected = "SOS" * (len(s) // 3)

count = 0

for actual, correct in zip(s, expected):
    if actual != correct:
        count += 1

print(count)
