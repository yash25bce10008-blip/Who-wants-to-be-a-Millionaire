from data_module import lifeline as lifeline_list, kbc_questions_answers, kbc_options_list, kbc_prize_money
from swap_module import Swapout
from lifeline_module import fifty_life

break_flag = 0
prize = 0
count = 0

print("Welcome to Who wants to be a Millionare ! \n")
Name = input("Enter your name : ")
print("-"*30)
while True:
    Age = input("Enter your age : ")
    if Age.isdigit():
        break
    else:
        print("❌ Invalid input!")
print("-" * 30)
print(f"Hello, {Name}! Let's play for the millions!")
print("Rules : Answer questions correctly. You have 2 safe levels after question 5 and question 10.")
print("You can use one 50/50 lifeline , one Audience Poll and one Swap Out!")
print("-" * 30)
print("\nFor Swapout Lifeline : 📝 Subject Expertise Selection 🧠")
print("Enter any subject that you are expert in or you are comfortable with:")

experties_on_sub = "k"
valid_inputs = {"e", "m", "s", "h", "g", "ec"}
while experties_on_sub not in valid_inputs:
    experties_on_sub = input(
        "Press e for english, m for maths, s for science, h for history, g for geography, ec for economics: "
    ).lower()
    if experties_on_sub not in valid_inputs:
        print("❌ Invalid input! Please re-enter a valid subject code.")

lifeline = lifeline_list.copy()
fifty_count = 0

def audiencepoll(answer,level):
    print("\n\n🧑‍🤝‍🧑 Audience Poll Results 📊 ")
    print("The audience has voted! Here are the percentages:")
    if level >= 0 and level <= 4 and fifty_count == 0:
        if answer == "a":
            print("a: 76%")
            print("b: 9%")
            print("c: 4%")
            print("d: 11%")
        elif answer == "b":
            print("a: 3%")
            print("b: 80%")
            print("c: 4%")
            print("d: 13%")
        elif answer == "c":
            print("a: 10%")
            print("b: 15%")
            print("c: 73%")
            print("d: 2%")
        elif answer == "d":
            print("a: 3%")
            print("b: 7%")
            print("c: 4%")
            print("d: 86%")
    elif level >= 5 and level <= 9 and fifty_count == 0:
        if answer == "a":
            print("a: 66%")
            print("b: 9%")
            print("c: 14%")
            print("d: 11%")
        elif answer == "b":
            print("a: 2%")
            print("b: 69%")
            print("c: 1%")
            print("d: 28%")
        elif answer == "c":
            print("a: 10%")
            print("b: 15%")
            print("c: 73%")
            print("d: 2%")
        elif answer == "d":
            print("a: 20%")
            print("b: 3%")
            print("c: 1%")
            print("d: 76%")
    elif level >= 10 and level <= 15 and fifty_count == 0:
        if answer == "a":
            print("a: 51%")
            print("b: 4%")
            print("c: 1%")
            print("d: 44%")
        elif answer == "b":
            print("a: 20%")
            print("b: 55%")
            print("c: 14%")
            print("d: 11%")
        elif answer == "c":
            print("a: 17%")
            print("b: 13%")
            print("c: 60%")
            print("d: 10%")
        elif answer == "d":
            print("a: 40%")
            print("b: 2%")
            print("c: 1%")
            print("d: 57%")
    if level >= 0 and level <= 4 and fifty_count == 1:
         if answer == "a":
            print("a: 76%")
            print("b: 9%")
         elif answer == "b":
            print("b: 80%")
            print("c: 4%")
         elif answer == "c":
            print("a: 10%")
            print("c: 73%")
         elif answer == "d":
            print("a: 3%")
            print("d: 86%")
    elif level >= 5 and level <= 9 and fifty_count == 1:
        if answer == "a":
            print("a: 66%")
            print("b: 9%")
        elif answer == "b":
            print("b: 69%")
            print("c: 1%")
        elif answer == "c":
            print("a: 10%")
            print("c: 73%")
        elif answer == "d":
            print("a: 20%")
            print("d: 76%")
    elif level >= 10 and level <= 15 and fifty_count == 1:
        if answer == "a":
            print("a: 51%")
            print("b: 4%")
        elif answer == "b":
            print("b: 55%")
            print("c: 14%")
        elif answer == "c":
            print("a: 17%")
            print("c: 60%")
        elif answer == "d":
            print("a: 40%")
            print("d: 57%")
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

def lifeline_user():
    global question, answer, option, fifty_count, break_flag
    while True:
        if len(lifeline) == 0:
            print("😔 No more lifelines remaining! You must choose a direct option.")
            print("Choose correct option or quit !")
            user_ans = input("enter: ")
            if user_ans == answer:
                check(1)
            elif user_ans == "q":
                check(2)
            else:
                check(0)
            break

        print("\n💡 Remaining Lifelines:")
        for j in lifeline:
            print(f"   -> {j}")

        inpu = input("choose lifeline (e.g., 'a' for swap): ")
        if inpu == "a" and ("a:swap" in lifeline):
            swapout_answer, question, answer, option = Swapout(experties_on_sub, count)
            lifeline.remove("a:swap")
            check(swapout_answer)
            break
        if inpu == "b" and ("b:fifty" in lifeline):
            fifty_answer = fifty_life(question, answer, option)
            lifeline.remove("b:fifty")
            fifty_count = 1
            check(fifty_answer)
            break
        if inpu == "c" and ("c:audience" in lifeline):
            audiencepoll_answer = audiencepoll(answer, option, count)
            lifeline.remove("c:audience")
            check(audiencepoll_answer)
            break
        else:
            print("❌ Invalid lifeline choice or that lifeline has already been used. Please choose a valid option.")

def check(b):
    global break_flag, count, prize
    if b == 1 or b == answer:
        print(f"\n🎉 CORRECT ANSWER! You've won ₹{kbc_prize_money[count]:,}! 💰")
        prize = kbc_prize_money[count]
        count = count + 1
    elif b == 2 or b == "q":
        print(f"\n QUITTING GAME. You walk away with a safe amount of ₹{prize:,}.")
        print("Correct option was : ", answer)
        break_flag = 1
    elif b == 3:
        lifeline_user()
        
    else:
        print("\n❌ WRONG ANSWER! Game Over.")
        print("Correct option was : ", answer)
        if 9 >= count > 4:
            prize = 10000
            print(f"You reached the safe level. Your take-home prize is ₹{prize:,}.")
            break_flag = 1
        elif count > 9:
            prize = 320000
            print(f"You reached the safe level. Your take-home prize is ₹{prize:,}.")
            break_flag = 1
        else:
            prize = 0
            print("You did not reach a safe level. Better luck next time!")
            break_flag = 1

question = None
option = None
answer = None

for i in kbc_questions_answers:
 
    if break_flag == 1:
        break
    fifty_count = 0
    print("\n\n🧠 NEW QUESTION! Level", count + 1)
    print("---------------------------------")
    print(f"Question for ₹{kbc_prize_money[count]:,}: {i}")
    question = i
    answer = kbc_questions_answers[i]
    option = kbc_options_list[count]
    option_letters = ['a', 'b', 'c', 'd']
    idx = 0
    while idx < len(option):
        print(f"{option_letters[idx]}: {option[idx]}")
        idx += 1
    while True:
            a = input("Enter your option (a/b/c/d), 'l' for lifeline, 'q' to quit: ")
            if a in {'a', 'b', 'c', 'd', 'q', 'l'}:
                break
            else:
                print("❌ Invalid input!")
    if a == kbc_questions_answers[i]:
        print(f"\n🎉CORRECT ANSWER! You've won ₹{kbc_prize_money[count]:,}! 💰")
        prize = kbc_prize_money[count]
        count = count + 1
    elif a == "l":
        lifeline_user()
        if break_flag == 1:
            break
    elif a == "q":
        print(f"\n👋Thank you for playing! You walk away with a safe amount of ₹{prize:,}.")
        print("Correct option was : ", answer)
        break
    elif a in 'abcd':
        print("\n❌WRONG ANSWER! Game Over.")
        print("Correct option was : ", answer)
        if 9 >= count > 4:
            prize = 10000
            print(f"You reached the safe level.Your take-home prize is ₹{prize:,}.")
        elif count > 9:
            prize = 320000
            print(f"You reached the *third safe level . Your take-home prize is ₹{prize:,}.")
        else:
            prize = 0
            print("You did not reach a safe level. Better luck next time!")
        break

print(f"\n🌟FINAL PRIZE WON : ₹{prize:,} ")