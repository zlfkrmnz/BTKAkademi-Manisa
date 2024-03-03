def factorial(num):
    try:

        if num == 1 or num == 0:
            return 1
        elif num < 0:
            return "Non positive"
        return num * factorial(num - 1)
    except Exception as e:
        return f"Invalid input. Error message: {e}"


def combination(n, r):
    return factorial(n)/(factorial(r)*(factorial(n-r)))


if __name__ == '__main__':
    print(factorial(10))
    print(factorial(2))
    print(factorial(7))
    print(combination(10, 2))
