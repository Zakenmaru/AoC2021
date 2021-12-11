def p1():
    arr = inp_to_arr('inp.txt')
    prev = arr[0]
    i = 1
    count = 0
    while i < len(arr):
        curr = arr[i]
        if (prev < curr):
            count += 1 
        prev = curr
        i += 1
    print(count)

def p2():
    arr = inp_to_arr('inp.txt')
    prev = arr[0] + arr[1] + arr[2]
    i = 1
    count = 0
    while i < len(arr) - 2:
        curr = arr[i] + arr[i + 1] + arr[i + 2]
        if (prev < curr):
            count += 1 
        prev = curr
        i += 1
    print(count)

def inp_to_arr(file):
    res = []
    f = open(file, 'r')
    data = f.readlines()
    for line in data:
        res.append(int(line))
    return res
    
def main():
    p1()
    p2()

if __name__ == '__main__':
    main()