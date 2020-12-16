import math

def kSquareRoot(tested_num, repetitions): # KasCode's Square Root finder algorithm!
    current_min = 0
    current_max = tested_num
    percent_done = 0

    for loop_place in range(repetitions):
        middle = current_min + ( current_max - current_min ) / 2
        #print("min: "+str(current_min)+", max: "+str(current_max)+", middle: "+str(middle))
        
        tenth_percent = math.floor(loop_place/repetitions*10)
        if tenth_percent > percent_done:
            percent_done = tenth_percent
            print(str(tenth_percent*10)+"%")
        
        if middle * middle == tested_num:
            print("Exact result found after "+str(loop_place)+" repetitions!")
            break

        if middle * middle > tested_num:
            current_max = middle
        else:
            current_min = middle

    return current_min + ( current_max - current_min ) / 2

def func():
    tested_num = 0
    reps = 0

    while True:
        try:
            tninput = input("Enter the number you want to find the square root of: ")
            tninput = int(tninput)
        except ValueError:
            print("Make sure you're typing in a number!")
            continue
        else:
            tested_num = tninput
            break
    
    while True:
        try:
            tninput = input("Now enter the number of algorithm repetitions. Type \"help\" for more: ")
            if tninput == "help":
                print("This number is how many times this algorithm will repeat. The higher the number, the more accurate my result will be! I recommend around 5000-50000000 (A lot)")
                continue
            else:
                tninput = int(tninput)
        except ValueError:
            print("Make sure you're typing in a number!")
            continue
        else:
            reps = tninput
            break

    result = kSquareRoot(tested_num, reps)
    print("Result: "+str(result))
    
