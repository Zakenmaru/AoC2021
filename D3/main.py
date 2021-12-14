import copy

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
    return dig, arr


def p1():
    dig, _ = create_array()
    gamma = ""
    for i in dig:
        gamma += "1" if i.count("1") > i.count("0") else "0"
    epsilon = ""
    for j in range(len(gamma)):
        epsilon += "1" if gamma[j] == "0" else "0"
        
    res = int(gamma, 2) * int(epsilon, 2)
    print(res)


def p2():
    dig, arr = create_array()
    temp_arr_o = copy.copy(arr)
    temp_arr_co = copy.copy(arr)
    index = 0
    for i in dig:
        if len(temp_arr_o) == 1 and len(temp_arr_o) == 1 and index >= len(dig):
            break
        mcv = "1" if i.count("1") >= i.count("0") else "0"
        lcv = "0" if i.count("0") <= i.count("1") else "1"
        for bin in arr:
            if bin[index] != mcv:
                temp_arr_o.remove(bin)
                arr.remove(bin)
            if bin[index] != lcv:
                temp_arr_co.remove(bin)
                arr.remove(bin)
        index += 1
    
    res = int(temp_arr_o[0], 2) * int(temp_arr_co[0], 2)
    print(res)

def main():
    p1()
    p2()


if __name__ == '__main__':
    main()