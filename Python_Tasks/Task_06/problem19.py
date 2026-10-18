
# Problem Name: Company Logo
# HackerRank Link: https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

if __name__ == '__main__':
    s = input()

    count = Counter(s)

    result = sorted(count.items(), key=lambda item: (-item[1], item[0]))

    for char, frequency in result[:3]:
        print(char, frequency)
