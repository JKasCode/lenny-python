import math
import datetime
import formatting

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

def sqrtcmd():
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

def timecmd():
    time = datetime.datetime.now()
    print("The time is " + time.strftime("%H") + ":" + time.strftime("%M"))
    print("Today is " + time.strftime("%A") + ", " + time.strftime("%d") + " " + time.strftime("%B"))

def helpcmd(jump):
    print("\nI work by learning the answers to any question you have, then remembering them for later.\nFor more help, type in any of the subjects below for details.\nWhen you're done, type in \"exit\" to go back.")
    print("\nformat\ncommands\ninput markers\n")

    debounce = False

    while True:
        user_input = None

        if jump and not debounce:
            user_input = jump
            debounce = True
        else:
            user_input = input("[H] ")
            user_input = formatting.format_input(user_input)

        if user_input == "exit":
            break

        if user_input == "format":
            print("I recommend that you don't add any punctuations such as ! or ?. I also don't really care whether you capitalize your sentences or not!")
            continue

        if user_input == "commands":
            print("I have some built in commands that you can use such as time and math!")
            print("You start all commands with a \"/\" and then the command. Below is a list of all my commands'\n")
            print("/math     - [ALPHA] This is still in development, but right now this is capable of doing basic math with only two numbers.")
            print("/help     - This sends you to this page!")
            print("/services - Lists down all the services being used in this program, and gives you the option to disable/enable them")
            print("/time     - Prints the time and date! Pretty nifty, huh?")
            print("/sqrt     - Brings up the kSquareRoot function for finding the square root of the number you're looking for.")
            continue

        if user_input == "input markers":
            print("You might have noticed that when you're typing something in, theres a little box on the left. Here is a list of what they mean:")
            print(" [~] - basic input where you write in a question")
            print(" [H] - help page input for detail on subjects")
            print(" [A] - answering input that will set whatever you write as the answer to your question")
            print(" [S] - service editing input")
            continue

def mathcmd():
    print("\nI work by learning the answers to any question you have, then remembering them for later.\nFor more help, type in any of the subjects below for details.\nWhen you're done, type in \"exit\" to go back.")

    print("\nformat\ncommands\ninput markers\n")

    while True:
        user_input = input("[H] ")
        

        if user_input == "exit":
            break

        if user_input == "format":
            print("I recommend that you don't add any punctuations such as ! or ?. I also don't really care whether you capitalize your sentences or not!")
            continue

        if user_input == "commands":
            print("I have some built in commands that you can use such as time and math!")
            print("You start all commands with a \"/\" and then the command. Below is a list of all my commands")
            print("/math     - [ALPHA] This is still in development, but right now this is capable of doing basic math with only two numbers.")
            print("/help     - This sends you to this page!")
            print("/services - Lists down all the services being used in this program, and gives you the option to disable/enable them")
            print("/time     - Prints the time and date! Pretty nifty, huh?")
            print("/sqrt     - Brings up the kSquareRoot function for finding the square root of the number you're looking for.")
            continue

        if user_input == "input markers":
            print("You might have noticed that when you're typing something in, theres a little box on the left. Here is a list of what they mean:")
            print(" [~] - basic input where you write in a question")
            print(" [H] - help page input for detail on subjects")
            print(" [A] - answering input that will set whatever you write as the answer to your question")
            print(" [S] - service editing input")
            continue
