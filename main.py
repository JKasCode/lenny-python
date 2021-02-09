print("\nJust a moment while everything is being set up...")

# Opens files and sets up variables
import connect
import formatting

with open("qadoc", "r") as qadocument_r:
    file_lines = qadocument_r.readlines()

questions = []
answers = []

print("Formatting and sorting QAs...")

# commands dict
cmds = connect.get_commands()

# Removes the annoying \n in all the lines
for file_line in file_lines:
    formatted = file_line.rstrip()
    split_line = formatted.split("~")

    questions.append(split_line[0])
    answers.append(split_line[1])

print("\nWelcome to Lenny! Version 0.3.3")
print("To get started, type in any question! Type \"/help\" to get more detailed instructions.\n")

with open("reminder", "r") as reminder_doc:
    reminder = reminder_doc.read()

    if reminder == "":
        reminder = "E"
    else:
        print("Reminder: "+reminder+"\n")

while True:
    user_input = input("[~] ")
    user_input = formatting.format_input(user_input)

    # Built in functions (priority) so that user can't overwrite them
    if user_input == "exit" or user_input == "quit":
        exit()
    
    # Command handling
    if user_input[0] == "/":
        foundResult = False
        
        if user_input[1:] in cmds:
            slashremoved = cmds[user_input[1:]]

            if "connect" not in slashremoved["command"]:
                if slashremoved["arguments"] == None:
                    connect.run_process(slashremoved["command"])
                else:
                    connect.run_process(slashremoved["command"], slashremoved["arguments"])
            else:
                getattr(connect, slashremoved["command"].replace("connect.", ""))()

            foundResult = True
        
        if foundResult == True: 
            continue
        else:
            print("I don't think I have any commands that go by that name. Maybe try removing spaces or punctuation!")
            continue

    # User-generated question/answer handling
    if user_input in questions:
        list_place = questions.index(user_input)
        print(answers[list_place])
    else:
        print("I don't know the answer to that yet. Can you please tell me? If you're not sure, type \"cancel\" to stop writing.")
        new_answer = input("[A] ")

        if new_answer == "cancel":
            print("Cancelled")
            continue
        
        answers.append(new_answer)
        questions.append(user_input)

        with open("qadoc", "a") as qadocument_a:
            new_qa_line = user_input+"~"+new_answer+"\n"
            qadocument_a.write(new_qa_line)
