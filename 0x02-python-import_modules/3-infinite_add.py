#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    tot = 0
    for i in range(1, len(sys.argv)):
        tot = tot + int(sys.argv[i])
    print("{}".format(tot))
