def isIdentical(l1, l2):
    hm1, hm2 = hash(l1), hash(l2)
    if(hm1==hm2):
        return True
    else:
        return False


if __name__ == "__main__":
    a1 = input("Enter first line: ")
    a2 = input("Enter second line: ")
    

    print("Input is identical: ", isIdentical(a1,a2))