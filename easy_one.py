# challenge : https://www.hackerrank.com/contests/womens-codesprint-3/
# challenges/ascii-flower

# ASCII Flower

r,c = list(map(int, input().strip().split(' ')))p

f = ['..O..','O.o.O','..O..']

for i in range(r):
    for j in f:
        flowers = ''
        for k in range(c):
            flowers += j
        print(flowers)
