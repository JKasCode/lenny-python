print("\nJust a moment while everything is being set up...")

# Opens files and sets up variables
import connect

qadocument_r = open("qadoc", "r")
file_lines = qadocument_r.readlines()
qadocument_r.close()

questions = []
answers = []

print("Formatting and sorting QAs...")

# commands array
cmds = [
    ["help", "helpcmd"],
    ["services", connect.list_processes],
    ["time", "timecmd"],
    ["math", "mathcmd"],
    ["exit", exit],
    ["quit", exit]
]

# Removes the annoying \n in all the lines
for file_line in file_lines:
    file_place = file_lines.index(file_line)
    file_lines[file_place] = file_lines[file_place].rstrip()

for file_line in file_lines:
    split_line = file_line.split("~")
    split_answer = split_line[1].split(";")

    questions.append(split_line[0])
    answers.append(split_answer)

print("\nWelcome to Lenny! Version 0.3:30.10.20")
print("To get started, type in any question! Type \"/help\" to get more detailed instructions.\n")

while True:
    user_input = input("[~] ")
    user_input = user_input.lower()

    # Built in functions (priority) so that user can't overwrite them
    if user_input == "exit" or user_input == "quit":
        exit()
    
    # Command handling
    if user_input[0] == "/":
        foundResult = False

        for cmd in cmds:
            if user_input[1:] == cmd[0]:
                if isinstance(cmd[1], str):
                    connect.run_process(cmd[1])
                else:
                    cmd[1]()
                
                foundResult = True
                break
        
        if foundResult == True: 
            continue
        else:
            print("I don't think I have any commands that go by that name. Maybe try removing spaces or punctuation!")
            continue

    # User-generated question/answer handling
    if user_input in questions:
        list_place = questions.index(user_input)
        print(answers[list_place][0])
    else:
        print("I don't know the answer to that yet. Can you please tell me? If you're not sure, type \"cancel\" to stop writing.")
        new_answer = input("[A] ")

        if new_answer == "cancel":
            print("Cancelled")
            continue

        qadocument_a = open("qadoc", "a")
        new_qa_line = user_input+"~"+new_answer+"\n"
        qadocument_a.write(new_qa_line)
        qadocument_a.close()
