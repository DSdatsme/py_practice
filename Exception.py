# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(raw_input())):
    try:
        a, b = map(int, raw_input().split())
        print(a // b)
    except ZeroDivisionError or ValueError as e:
        print "Error Code: integer division or modulo by zero"
    except ValueError as e:
        print "Error Code: %s" % (e)

'''
3
1 0
2 $
3 1
'''
