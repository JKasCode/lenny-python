def func():
    print("\nI work by learning the answers to any question you have, then remembering them for later.\nFor more help, type in any of the subjects below for details.\nWhen you're done, type in \"exit\" to go back.")

    print("\nformat\ncommands\ninput markers\nmath\nservices\n")

    while True:
        user_input = input("[H] ")

        if user_input == "exit":
            break

        if user_input == "format":
            print("I recommend that you don't add any punctuations such as ! or ?. I also don't really care whether you capitalize your sentences or not!")
            continue

        if user_input == "commands":
            print("Since most answers to questions are created by you, the user, I'll only list down my built in commands.")
            continue

        if user_input == "input markers":
            print("You might have noticed that when you're typing something in, theres a little box on the left. Here is a list of what they mean:")
            print(" [~] - basic input where you write in a question")
            print(" [H] - help page input for detail on subjects")
            print(" [A] - answering input that will set whatever you write as the answer to your question")
            print(" [S] - service editing input")
            continue

        if user_input == "math":
            print("So far I can only do basic math, like addition, subtraction, multiplication and division.")
            print("If you want me to calculate something for you, write in a question with 2 numbers with a math symbol (+, -, /, *)")
            continue

        if user_input == "services":
            print("Services are the smaller functions that handle dynamic questions like math or this help page.")
            print("Some of my services are incomplete and are disabled by default to keep this program running smoothly.")
            print("If you want to disable or enable a service, type in the \"services\" command in a [~] input to view them all.")
            continue
        
        print("I couldn't find the subject you're looking to find out more about! Maybe check for any typos?")
