# challenge : https://www.hackerrank.com/contests/womens-codesprint-3/
# challenges/the-birthday-bar

# Birthday Chocolate

n = int(input().strip())
squares = list(map(int, input().strip().split(' ')))
d,m = list(map(int, input().strip().split(' ')))

check = 0
for i in range(n-m+1):
    s = 0
    for x in range(i, m+i):
        s += squares[x]

    if s == d:
        check += 1

print(check)
