def func():
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
            continue

        if user_input == "input markers":
            print("You might have noticed that when you're typing something in, theres a little box on the left. Here is a list of what they mean:")
            print(" [~] - basic input where you write in a question")
            print(" [H] - help page input for detail on subjects")
            print(" [A] - answering input that will set whatever you write as the answer to your question")
            print(" [S] - service editing input")
            continue
