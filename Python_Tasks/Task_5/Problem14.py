
# Problem: Finding the Percentage
# HackerRank: https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == "__main__":
    n = int(input())
    students = {}

    for _ in range(n):
        data = input().split()
        students[data[0]] = list(map(float, data[1:]))

    query_name = input()
    marks = students[query_name]
    average = sum(marks) / len(marks)

    print(f"{average:.2f}")
