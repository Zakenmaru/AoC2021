filename = "inp.txt"

def create_array():
    arr = []
    with open(filename, 'r') as inp:
        arr = inp.read().splitlines() 
    row_len = len(arr[0])
    dig = []
    for i in range(row_len):
        l = [a[i] for a in arr]
        dig.append(l)
    return dig


def p1():
    dig = create_array()
    gamma = ""
    for i in dig:
        gamma += "1" if i.count("1") > i.count("0") else "0"
    epsilon = ""
    for j in range(len(gamma)):
        epsilon += "1" if gamma[j] == "0" else "0"
        
    res = int(gamma, 2) * int(epsilon, 2)
    print(res)


def main():
    p1()


if __name__ == '__main__':
    main()