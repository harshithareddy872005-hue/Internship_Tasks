
# Problem Name: Set .union() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input())
english_students = set(map(int, input().split()))

m = int(input())
french_students = set(map(int, input().split()))

result = english_students.union(french_students)

print(len(result))
