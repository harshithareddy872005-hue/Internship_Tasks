
# Problem 17: Separate the Numbers
# HackerRank: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    if len(s) < 2 or s[0] == '0':
        print("NO")
        return

    for length in range(1, len(s) // 2 + 1):
        first = int(s[:length])
        current = first
        result = ""

        while len(result) < len(s):
            result += str(current)
            current += 1

        if result == s:
            print("YES", first)
            return

    print("NO")


q = int(input())

for _ in range(q):
    s = input().strip()
    separateNumbers(s)
