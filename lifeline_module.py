def fifty_life(question, answer, options):
    print("\n\n✂ 50/50 Lifeline Activated! ✂")
    print("❌ Two incorrect options have been removed!")
    print(f" Q : {question}")
    print("---------------------------------")

    if answer == "a":
        print(f"a: {options[0]}")
        print(f"b: {options[1]}")
    elif answer == "b":
        print(f"c: {options[2]}")
        print(f"b: {options[1]}")
    elif answer == "c":
        print(f"c: {options[2]}")
        print(f"a: {options[0]}")
    elif answer == "d":
        print(f"d: {options[3]}")
        print(f"a: {options[0]}")

    user_answer = "m"
    valid_inputs = {'a', 'b', 'c', 'd', 'q', 'l'}
    while user_answer not in valid_inputs:
        user_answer = input("Enter your option(a/b/c/d), 'l' for lifeline, 'q' to quit: ")
        if user_answer == answer:
            return 1
        elif user_answer == "q":
            return 2
        elif user_answer == "l":
            return 3
        elif user_answer not in valid_inputs:
            print("🚫Invalid input! Please enter a, b, c, d, l, or q.")
            continue
        else:
            return 0