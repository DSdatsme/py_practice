# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

h, w = map(int, raw_input().split())

for i in range(h):
    if math.ceil(h / 2) == i:
        print("WELCOME".center(w, '-'))
        continue
    if i < h / 2:
        print((".|." * (2 * i + 1)).center(w, '-'))
        continue
    if i < h:
        print((".|." * (2 * (h - i) - 1)).center(w, '-'))

'''
9 27
'''
