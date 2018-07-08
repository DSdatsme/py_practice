def swap_case(s):
    ans = ""
    for i in s:
        if i.isupper():
            ans += i.lower()
        else:
            ans += i.upper()
    return ans


'''
Alternate Solution
def swap_case(s):
    return s.swapcase()
'''

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result

'''
HackerRank.com presents "Pythonist 2".
'''
