"""
Question 1: Program that finds whether an entered number is prime or not
Question 2: Program that finds prime numbers between 1-1000
Question 3: Program showing perfect numbers up to 10000 --> 1+2+3 = 6
"""


def is_prime(number):
    if number <= 1:
        return False
    else:
        for i in range(2, int(number**1/2)+1):
            if number % i == 0:
                return False
        return True


if __name__ == '__main__':
    num = int(input("Please enter a number: "))
    if is_prime(num):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

    print("\n*******************PRIME NUMBERS (1 TO 1000)*******************")
    for i in range(1, 1001):
        if is_prime(i):
            print(i, end=" ")

    print("\n\n*******************PERFECT NUMBERS (LOWER THAN 10000)*******************")
    for i in range(1, 10000):
        toplam = 0
        for j in range(1, int((i/2)+1)):
            if i % j == 0:
                toplam += j
            else:
                continue
        if toplam == i:
            print(i, end=" ")
