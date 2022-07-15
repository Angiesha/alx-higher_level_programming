#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the number of and list of a program's arguments."""
    import sys
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            print("{} arguments:".format(len(sys.argv) - 1))
        else:
            print("{} argument:".format(len(sys.argv) - 1))
        count = 0
        for i in sys.argv:
            if count == 0:
                count += 1
                continue
            else:
                count = count + 1
                print("{}: {}".format(count - 1, sys.argv[count - 1]))
    elif len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
