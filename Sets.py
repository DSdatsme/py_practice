# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(raw_input())
a = map(int,raw_input().split())
n = int(raw_input())
b = map(int,raw_input().split())
list1=list((set(a).union(set(b))).difference(set(a).intersection(set(b))))
for i in sorted(list1):
    print(i)


'''
4
2 4 5 9
4
2 4 11 12
'''