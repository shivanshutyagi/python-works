def printPrimeFactors(num):
    '''
    prints primeFactors of num
    :argument: number whose prime factors need to be printed
    :return:
    '''
    for i in range(2, num+1):
        if isPrime(i) and num%i==0:
            print(i)


def isPrime(num):
    '''
    Checks if num is prime or not
    :param num:
    :return: true if num is prime, else false
    '''
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False

    return True

if __name__ == "__main__":
    n = int(input('Enter the number: '))
    printPrimeFactors(n)
