class SmallValueException(Exception):
    pass


class LargeValueException(Exception):
    pass


while True:
    try:
        a = int(raw_input("Enter a number"))
        if a > 1000:
            raise LargeValueException
        if a < 0:
            raise SmallValueException
        break
    except SmallValueException:
        print('small val')
    except LargeValueException:
        print("large val")

    print('Number Excepted')
