
# Problem: Piling Up!
# HackerRank: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

if __name__ == "__main__":
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        blocks = deque(map(int, input().split()))
        last = float("inf")
        possible = True

        while blocks:
            left = blocks[0]
            right = blocks[-1]

            if left >= right:
                if left <= last:
                    last = blocks.popleft()
                elif right <= last:
                    last = blocks.pop()
                else:
                    possible = False
                    break
            else:
                if right <= last:
                    last = blocks.pop()
                elif left <= last:
                    last = blocks.popleft()
                else:
                    possible = False
                    break

        print("Yes" if possible else "No")
