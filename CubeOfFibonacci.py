cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, b + a


if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))

'''
5
'''
