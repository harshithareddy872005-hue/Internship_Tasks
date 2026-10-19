
# Problem 16: Caesar Cipher
# HackerRank: https://www.hackerrank.com/challenges/caesar-cipher-1/problem

def caesarCipher(s, k):
    result = []

    k = k % 26

    for char in s:
        if 'a' <= char <= 'z':
            shifted = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result.append(shifted)

        elif 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') + k) % 26 + ord('A'))
            result.append(shifted)

        else:
            result.append(char)

    return ''.join(result)


n = int(input())
s = input().strip()
k = int(input())

print(caesarCipher(s, k))

