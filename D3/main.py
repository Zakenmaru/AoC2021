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


def column(matrix, i):
    return [row[i] for row in matrix]


def rating_filter(arr, criteria):
    index = 0
    if criteria == "o2":
        while index < len(arr[0]) and len(arr) > 1:
            cur_col = column(arr, index)
            count_one = cur_col.count("1")
            count_zero = cur_col.count("0")
            crit = "1" if count_one >= count_zero else "0"
            arr = [bin for bin in arr if bin[index] == crit]
            index += 1
    else:
        while index < len(arr[0]) and len(arr) > 1:
            cur_col = column(arr, index)
            count_one = cur_col.count("1")
            count_zero = cur_col.count("0")
            crit = "0" if count_zero <= count_one else "1"
            arr = [bin for bin in arr if bin[index] == crit]
            index += 1
    return arr[0]

def p2():
    _, arr = create_array()
    oxygen_rating = rating_filter(copy.copy(arr), criteria="o2")
    carbon_rating = rating_filter(copy.copy(arr), criteria="co2")
    res = int(oxygen_rating, 2) * int(carbon_rating, 2)
    print(res)


def main():
    p1()
    p2()


if __name__ == '__main__':
    main()