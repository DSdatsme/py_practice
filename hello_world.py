if __name__ == '__main__':
    N = int(raw_input())
    L = []
    for i in range(N + 1):
        mInput = raw_input().split(" ")
        if mInput[0] == "insert" : L.insert(int(mInput[1]),int(mInput[2]))
        if mInput[0] == "remove" : L.remove(int(mInput[1]))
        if mInput[0] == "print" : print(L)
        if mInput[0] == "append" : L.append(int(mInput[1]))
        if mInput[0] == "sort" : L.sort()
        if mInput[0] == "pop" : L.pop()
        if mInput[0] == "reverse" : L.reverse()


''' input
29
append 1
append 6
append 10
append 8
append 9
append 2
append 12
append 7
append 3
append 5
insert 8 66
insert 1 30
insert 6 75
insert 4 44
insert 9 67
insert 2 44
insert 9 21
insert 8 87
insert 1 75
insert 1 48
print
reverse
print
sort
print
append 2
append 5
remove 2
print
'''