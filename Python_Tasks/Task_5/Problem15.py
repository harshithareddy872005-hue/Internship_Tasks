
# Problem: Lists
# HackerRank: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == "__main__":
    n = int(input())
    result = []

    for _ in range(n):
        command, *args = input().split()

        if command == "insert":
            result.insert(int(args[0]), int(args[1]))
        elif command == "print":
            print(result)
        elif command == "remove":
            result.remove(int(args[0]))
        elif command == "append":
            result.append(int(args[0]))
        elif command == "sort":
            result.sort()
        elif command == "pop":
            result.pop()
        elif command == "reverse":
            result.reverse()
