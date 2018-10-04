import bisect

n = int(raw_input())

a = map(int, raw_input().split())

a = sorted(a)
q = int(raw_input())

for i in xrange(q):
    m = int(raw_input())
    # ... hint: use bisect
    print(ans)
