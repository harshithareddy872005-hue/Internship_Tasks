
# Problem 10: CamelCase
# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem

s = input().strip()

words = 1

for char in s:
    if char.isupper():
        words += 1

print(words)
