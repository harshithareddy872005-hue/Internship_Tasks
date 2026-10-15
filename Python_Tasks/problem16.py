
# Problem 16: Nested Lists
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem

records = []

for _ in range(int(input())):
    name = input().strip()
    score = float(input())
    records.append([name, score])

scores = sorted(set(record[1] for record in records))
second_lowest = scores[1]

names = sorted(
    record[0] for record in records
    if record[1] == second_lowest
)

for name in names:
    print(name)
