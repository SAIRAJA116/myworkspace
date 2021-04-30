import itertools
s = input()
prep = itertools.combinations(s,1)
for i in prep:
    print(i)