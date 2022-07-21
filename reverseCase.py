def caseSwitch(s):
    return (''.join([i.lower() if i.isupper() else i.upper() for i in s]))

if __name__=="__main__":
    s = input("\nInput a string for a ~reverse case~\n------------------\n")
    result = caseSwitch(s)
    print(f'\n{result}\n')