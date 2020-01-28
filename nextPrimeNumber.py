def next_prime(num):
    """
    returns next prime number
    :param num: number from which next prime number should succeed
    :return: next prime number greater than num
    """
    num += 1
    while not is_prime(num):
        num += 1
    return num


def is_prime(num):
    """
    Checks if num is prime or not
    :param num:
    :return: true if num is prime, else false
    """
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False

    return True


if __name__ == "__main__":
    print_next = input("Print next?? (y/n): ")
    num = 1
    while print_next == 'y':
        num = next_prime(num)
        print(num)
        print_next = input("Print next?? (y/n): ")


