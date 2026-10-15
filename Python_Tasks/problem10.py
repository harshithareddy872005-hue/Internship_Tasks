
# Problem 10: Find a String
# HackerRank: https://www.hackerrank.com/challenges/find-a-string/problem

s = input().strip()
sub = input().strip()

count = 0
for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        count += 1

print(count)
