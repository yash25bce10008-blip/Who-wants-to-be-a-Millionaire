from database import *
def check_fn(question, answer, index):
    print("\n\n❓Current Question")
    print(f"Q:{list(question)[index]}")
    print("---------------------------------")
    print(f"a: {answer[index][0]}")
    print(f"b: {answer[index][1]}")
    print(f"c: {answer[index][2]}")
    print(f"d: {answer[index][3]}")
    current_question=list(question)[index]
    current_answer=question[list(question)[index]]
    user_answer = "m" 
    valid_inputs = {'a', 'b', 'c', 'd', 'q', 'l'}
    while user_answer not in valid_inputs:
        user_answer = input("Enter your option(a/b/c/d), 'l' for lifeline, 'q' to quit: ")
        if question[list(question)[index]] == user_answer:
            return 1 , current_question , current_answer , answer[index]
        elif user_answer == "q":
            return 2 , current_question , current_answer , answer[index]
        elif user_answer == "l":
            return 3 , current_question , current_answer , answer[index]
        elif user_answer not in valid_inputs:
            print("🚫 Invalid input! Please enter a, b, c, d, l, or q.")
            continue
        else:
            return 0 , current_question , current_answer , answer[index]

def Swapout(Experties_on_sub, level):
    if level >= 0 and level <= 4:
        if Experties_on_sub == "e":
            check = check_fn(swap_stage_1_questions, swap_stage_1_options, 0)
            return check
        elif Experties_on_sub == "m":
            check = check_fn(swap_stage_1_questions, swap_stage_1_options, 1)
            return check
        elif Experties_on_sub == "s":
            check = check_fn(swap_stage_1_questions, swap_stage_1_options, 2)
            return check
        elif Experties_on_sub == "h":
            check = check_fn(swap_stage_1_questions, swap_stage_1_options, 3)
            return check
        elif Experties_on_sub == "g":
            check = check_fn(swap_stage_1_questions, swap_stage_1_options, 4)
            return check
        elif Experties_on_sub == "ec":
            check = check_fn(swap_stage_1_questions, swap_stage_1_options, 5)
            return check

    elif level >= 5 and level <= 9:
        if Experties_on_sub == "e":
            check = check_fn(swap_stage_2_questions, swap_stage_2_options, 0)
            return check
        elif Experties_on_sub == "m":
            check = check_fn(swap_stage_2_questions, swap_stage_2_options, 1)
            return check
        elif Experties_on_sub == "s":
            check = check_fn(swap_stage_2_questions, swap_stage_2_options, 2)
            return check
        elif Experties_on_sub == "h":
            check = check_fn(swap_stage_2_questions, swap_stage_2_options, 3)
            return check
        elif Experties_on_sub == "g":
            check = check_fn(swap_stage_2_questions, swap_stage_2_options, 4)
            return check
        elif Experties_on_sub == "ec":
            check = check_fn(swap_stage_2_questions, swap_stage_2_options, 5)
            return check

    elif level >= 10 and level <= 14:
        if Experties_on_sub == "e":
            check = check_fn(swap_stage_3_questions, swap_stage_3_options, 0)
            return check
        elif Experties_on_sub == "m":
            check = check_fn(swap_stage_3_questions, swap_stage_3_options, 1)
            return check
        elif Experties_on_sub == "s":
            check = check_fn(swap_stage_3_questions, swap_stage_3_options, 2)
            return check
        elif Experties_on_sub == "h":
            check = check_fn(swap_stage_3_questions, swap_stage_3_options, 3)
            return check
        elif Experties_on_sub == "g":
            check = check_fn(swap_stage_3_questions, swap_stage_3_options, 4)
            return check
        elif Experties_on_sub == "ec":
            check = check_fn(swap_stage_3_questions, swap_stage_3_options, 5)
            return check

def fifty_life(question,answer,options):
    print("\n\n✂ 50/50 Lifeline Activated! ✂")
    print("❌ Two incorrect options have been removed!")
    print(f" Q : {question}")
    print("---------------------------------")
    option_remain=[]
    if(answer=="a"):
        print(f"a: {options[0]}")
        print(f"b: {options[1]}")
        option_remain =[options[0],options[1]]
    elif(answer=="b"):
        print(f"c: {options[2]}")
        print(f"b: {options[1]}")
        option_remain = [options[2], options[1]]
    elif(answer=="c"):
        print(f"c: {options[2]}")
        print(f"a: {options[0]}")
        option_remain = [options[3], options[0]]
    elif(answer=="d"):
        print(f"d: {options[3]}")
        print(f"a: {options[0]}")
        option_remain = [options[3], options[0]]

    user_answer = "m" # initialize
    valid_inputs = {'a', 'b', 'c', 'd', 'q', 'l'}
    while user_answer not in valid_inputs:
        user_answer = input("Enter your option(a/b/c/d), 'l' for lifeline, 'q' to quit: ")
        if user_answer==answer:
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

def audiencepoll(answer,level,poll):
    print("\n\n🧑‍🤝‍🧑 Audience Poll Results 📊 ")
    print("The audience has voted! Here are the percentages:")

    if(level>=0 and level<=4):
        if(answer=="a"):
            if(poll==0):
                print("a: 76%")
                print("b: 9%")
                print("c: 4%")
                print("d: 11%")
            else:
                print("a: 89%")
                print("b: 11%")
        elif(answer=="b"):
            if(poll==0):
                print("a: 3%")
                print("b: 80%")
                print("c: 4%")
                print("d: 13%")
            else:
                print("b: 87%")
                print("c: 13%")
        elif(answer=="c"):
            if(poll==0):
                print("a: 10%")
                print("b: 15%")
                print("c: 73%")
                print("d: 2%")
            else:
                print("a: 23%")
                print("c: 73%")
        elif(answer=="d"):
            if(poll==0):
                print("a: 3%")
                print("b: 7%")
                print("c: 4%")
                print("d: 86%")
            else:
                print("a: 14%")
                print("d: 86%")
    elif(level>=5 and level<=9):
        if(answer=="a"):
            if(poll==0):
                print("a: 66%")
                print("b: 9%")
                print("c: 14%")
                print("d: 11%")
            else:
                print("a: 70%")
                print("c: 30%")
        elif(answer=="b"):
            if(poll==0):
                print("a: 2%")
                print("b: 69%")
                print("c: 1%")
                print("d: 28%")
            else:
                print("b: 73%")
                print("c: 27%")
        elif(answer=="c"):
            if(poll==0):
                print("a: 10%")
                print("b: 15%")
                print("c: 73%")
                print("d: 2%")
            else:
                print("a: 31%")
                print("c: 69%")
        elif(answer=="d"):
            if(poll==0):
                print("a: 20%")
                print("b: 3%")
                print("c: 1%")
                print("d: 76%")
            else:
                print("b: 28%")
                print("d: 72%")
    elif(level>=10 and level<=14):
        if(answer=="a"):
            if(poll==0):
                print("a: 51%")
                print("b: 4%")
                print("c: 1%")
                print("d: 44%")
            else:
                print("a: 57%")
                print("b: 43%")
        elif(answer=="b"):
            if(poll==0):
                print("a: 20%")
                print("b: 55%")
                print("c: 14%")
                print("d: 11%")
            else:
                print("a: 44%")
                print("b: 56%")
        elif(answer=="c"):
            if(poll==0):
                print("a: 17%")
                print("b: 13%")
                print("c: 60%")
                print("d: 10%")
            else:
                print("b: 40%")
                print("c: 60%")
        elif(answer=="d"):
            if(poll==0):
                print("a: 40%")
                print("b: 2%")
                print("c: 1%")
                print("d: 57%")
            else:
                print("b: 45%")
                print("d: 55%")
    user_answer = "m" # initialize
    valid_inputs = {'a', 'b', 'c', 'd', 'q', 'l'}
    while user_answer not in valid_inputs:
        user_answer = input("Enter your option(a/b/c/d), 'l' for lifeline, 'q' to quit: ")
        if user_answer==answer:
            return 1
        elif user_answer == "q":
            return 2
        elif user_answer == "l":
            return 3
        elif user_answer not in valid_inputs:
            # Print statement changed below
            print("🚫Invalid input! Please enter a, b, c, d, l, or q.")
            # End of change
            continue
        else:
            return 0
    
print("Welcome to Kaun Banega Crorepati! \n")
Name=input("Enter your name : ")
print("-"*30)
try:
    Age=int(input("Enter your age : "))
except ValueError:
    print("enter valid age")
    Age=1000
if(Age<0 or Age>100):
    print("Error Invalid Age! Please enter valid Age between 0 to 100.")
    Age = int(input("Enter your age : "))
print("-" * 30)
print(f"Hello, {Name}! Let's play for the crores!")
print("Rules : Answer questions correctly. You have 2 safe levels after question 5 and question 10.")
print("You can use one 50/50 lifeline , one Audience Poll and one Swap Out!")
print("-" * 30)
print("\n📝 Subject Expertise Selection 🧠")
print("Enter any subject that you are expert in or you are comfortable with:")

experties_on_sub = "k" # given any initiating value
valid_inputs = {"e", "m", "s", "h", "g", "ec"}
while experties_on_sub not in valid_inputs:
    experties_on_sub = input(
        "Press e for english, m for maths, s for science, h for history, g for geography, ec for economics: "
    ).lower()
    if experties_on_sub not in valid_inputs:
        print("❌ Invalid input! Please re-enter a valid subject code.")
       
lifeline=["a:swap","b:fifty","c:audience"]
def lifeline_user():
 while True:
    global question,answer,option,poll
    if len(lifeline)==0:

        print("😔 No more lifelines remaining! You must choose a direct option.")
        print("choose correct option")
        user_ans=input("enter")
        check(user_ans)
        break

    print("\n💡 Remaining Lifelines:")
    for j in lifeline:
        print(f"   -> {j}")
    
    inpu=input("choose lifeline ('a' for Question-swap, 'b' for Fifty-Fifty, 'c' for Audience Poll): ")
    if inpu=="a" and ("a:swap" in lifeline):
        swapout_answer,question,answer,option=Swapout(experties_on_sub,count)
        lifeline.remove("a:swap")
        check(swapout_answer)
        break
    if inpu=="b" and ("b:fifty" in lifeline):
        fifty_answer=fifty_life(question,answer,option)
        if(fifty_answer==3):
            poll=1
        lifeline.remove("b:fifty")
        check(fifty_answer)
        break
    if inpu=="c" and ("c:audience" in lifeline):
        audiencepoll_answer=audiencepoll(answer,count,poll)
        lifeline.remove("c:audience")
        check(audiencepoll_answer)
        break
    else:
        print("❌ Invalid lifeline choice or that lifeline has already been used. Please choose a valid option.")
        
break_flag=0
prize=0
count=0
def check(b):
    global break_flag,count,prize,i,question,answer,option
    a=b
    if a==1 or a==answer:
        print(f"\n🎉 CORRECT ANSWER! You've won ₹{kbc_prize_money[count]:,}! 💰")
        prize=kbc_prize_money[count]
        count=count+1
    elif a==2 or a=="q":
        print(f"\n QUITTING GAME. You walk away with a safe amount of ₹{prize:,}.")
       
        prize=prize
        break_flag=1
    elif a==3:
        lifeline_user()
    else:
        print("\n❌ WRONG ANSWER! Game Over.")
        if 9>=count>4:
            prize=10000
            print(f"You reached the safe level. Your take-home prize is ₹{prize:,}.")
            break_flag=1
        elif count>9:
            prize=320000
            print(f"You reached the safe level. Your take-home prize is ₹{prize:,}.")
            break_flag=1
        else:
            prize=0
            print("You did not reach a safe level. Better luck next time!")
            break_flag=1
question="m"  
option="m"
answer="m"
fifty_count=0
for i in kbc_questions_answers:
    print("\n\n🧠 NEW QUESTION! Level", count + 1)
    print("---------------------------------")
    print(f"Question for ₹{kbc_prize_money[count]:,}: {i}")
    question=i
    answer=kbc_questions_answers[i]
    option= kbc_options_list[count]
    option_letters = ['a', 'b', 'c', 'd']
    index = 0
    while index < len(option):
        print(f"{option_letters[index]}: {option[index]}")
        index += 1
    valid_inputs1={"a","b","c","d","q","l"}
    a=input("Enter your option (a/b/c/d), 'l' for lifeline, 'q' to quit: ")
    while a not in valid_inputs1:
        print("please enter valid input")
        a=input("Enter your option (a/b/c/d), 'l' for lifeline, 'q' to quit: ")
    if a==kbc_questions_answers[i]:
        print(f"\n🎉CORRECT ANSWER! You've won ₹{kbc_prize_money[count]:,}! 💰")
        prize=kbc_prize_money[count]
        count=count+1
    elif a=="l":
        lifeline_user()
        if break_flag==1:
            break

    elif a=="q":
        print(f"\n👋Thank you for playing! You walk away with a safe amount of ₹{prize:,}.")
        prize=prize
        break
    else:
        print("\n❌WRONG ANSWER! Game Over.")
        if 9>=count>4:
            prize=10000
            print(f"You reached the safe level.Your take-home prize is ₹{prize:,}.")
        elif count>9:
            prize=320000
            print(f"You reached the *third safe level . Your take-home prize is ₹{prize:,}.")
        else:
            prize=0
            print("You did not reach a safe level. Better luck next time!")
        break

print(f"\n🌟FINAL PRIZE WON : ₹{prize:,} 🥳")