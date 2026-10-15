
# Problem 9: Mutations
# HackerRank: https://www.hackerrank.com/challenges/python-mutations/problem

s = input()
i, c = input().split()

s = s[:int(i)] + c + s[int(i) + 1:]
print(s)
