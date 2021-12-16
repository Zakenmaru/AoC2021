import sys
from sys import maxsize


filename = "inp.txt"

def parse_file(filename):
    with open(filename, 'r') as inp:
        arr= inp.readline().split(',')
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        return arr


def p1():
    pos = parse_file(filename)
    min_fuel = sys.maxsize
    for i in pos:
        fuel = 0
        for j in pos:
            dist = i-j
            fuel += abs(dist)
        if min_fuel > fuel:
            min_fuel = fuel
    print(min_fuel)


def main():
    p1()


if __name__ == '__main__':
    main()