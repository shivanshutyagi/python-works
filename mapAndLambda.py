def call():
    frez = map(lambda x, y: x * y, range(1, 10), range(10, 1, -1))
    return frez


if __name__ == "__main__":
    for i in call():
        print(i)
