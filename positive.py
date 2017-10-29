def main():
    i = get_positive_int()
    print("{} is a positve integer".format(i))

def get_positive_int():
    while True:
        n = input("n is ", end="")

        if n >= 1:
            break
    return n

if __name__ == "__main()__":
    main()
