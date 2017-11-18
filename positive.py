def main():
    i = get_positive_int()
    print (" is a positive")
    print (i,'')

def get_positive_int():
    while True:
        n = input("n is ")
        if (n >= 1):
            break
    return n
if __name__ == "__main__":
    main()
