# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
st,k = raw_input().split()
for a in combinations_with_replacement(sorted(st), int(k)):
    print("".join(a))

'''
HACK 2
'''