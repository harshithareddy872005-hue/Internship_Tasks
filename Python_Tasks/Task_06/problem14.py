
# Problem Name: Set .intersection() Operation
# HackerRank Link: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

n = int(input())
english_students = set(map(int, input().split()))

m = int(input())
french_students = set(map(int, input().split()))

result = english_students.intersection(french_students)

print(len(result))
