x = 0
y = 0

directions = {"up":[], "down":[], "forward":[]}

def parse_file_2(file):
    global x 
    global y 
    f = open(file, 'r')
    data = f.readlines()
    
    aim = 0
    
    for line in data:
        line_arr = line.split()
        dire = line_arr[0]
        amt = int(line_arr[1])
        if dire == "up":
            aim -= amt
        if dire == "down":
            aim += amt
        if dire == "forward":
            x += amt
            if aim > 0:
                y += aim * amt
    
    print("X: ", x)
    print("Y: ", y)
    
    print(x * y)
    
    
def parse_file(file):
    res = []
    f = open(file, 'r')
    data = f.readlines()
    for line in data:
        line_arr = line.split()
        directions[line_arr[0]].append(int(line_arr[1]))
    
def p1():
    global x 
    global y 
    x = 0
    y = 0
    parse_file("inp.txt")
    y -= sum(directions["up"])
    y += sum(directions["down"])
    x += sum(directions["forward"])
    
    print("X: ", x)
    print("Y: ", y)
    
    print(x * y)


def p2():
    global x 
    global y 
    x = 0
    y = 0
    parse_file_2("inp.txt")
    


def main():
    p1()
    p2()
    
if __name__ == '__main__':
    main()