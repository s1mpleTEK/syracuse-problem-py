#!/usr/bin/python3

import sys

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit() or int(sys.argv[1]) < 1:
        sys.exit(-1)

    num = int(sys.argv[1])
    log = [{"iteration":0}, []]

    while 1:
        num = int(((num*3)+1) if num % 2 == 1 else num/2)
        log[0]['iteration'] += 1
        # log[1].append(int(num))
        log[1].append("{0:b}".format(num))
        if num == 1:
            break

    print(log)
    sys.exit(0)

main()