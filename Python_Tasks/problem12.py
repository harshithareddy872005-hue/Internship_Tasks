
# Problem 12: Introduction to Sets
# HackerRank: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    distinct_heights = set(array)
    return sum(distinct_heights) / len(distinct_heights)

n = int(input())
array = list(map(int, input().split()))

print(f"{average(array):.3f}")
