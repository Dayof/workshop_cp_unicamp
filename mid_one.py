# https://www.hackerrank.com/contests/womens-codesprint-3/
# challenges/hackathon-shirts/

# Hackathon Shirts

q = int(input().strip())

for a0 in range(q):
    n = int(input().strip())
    sizes = list(map(int, input().strip().split(' ')))
    sizes = sorted(sizes)

    v = int(input().strip())

    ranges = []
    for a1 in range(v):
        smallest,largest = input().strip().split(' ')
        smallest,largest = [int(smallest),int(largest)]

        ranges.append((smallest, 1))
        ranges.append((largest, 2))

    ranges = sorted(ranges)

    ans = j = start = start_point = end_point = 0

    for tup in ranges:
        if tup[1] == 1:
            if start == 0:
                start_point = tup[0]
            start += 1
        else:
            start -= 1
        if start == 0:
            end_point = tup[0]
            while j<n and sizes[j] <= end_point:
                if sizes[j] >= start_point:
                    ans += 1
                j += 1

    print(ans)
