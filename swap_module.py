def check_fn(question, answer, index):
    print("\n\n❓Current Question")
    print(f"Q:{list(question)[index]}")
    print("---------------------------------")
    print(f"a: {answer[index][0]}")
    print(f"b: {answer[index][1]}")
    print(f"c: {answer[index][2]}")
    print(f"d: {answer[index][3]}")
    current_question = list(question)[index]
    current_answer = question[current_question]
    user_answer = "m"
    valid_inputs = {'a', 'b', 'c', 'd', 'q', 'l'}
    while user_answer not in valid_inputs:
        user_answer = input("Enter your option(a/b/c/d), 'l' for lifeline, 'q' to quit: ")
        if question[list(question)[index]] == user_answer:
            return 1, current_question, current_answer, answer[index]
        elif user_answer == "q":
            return 2, current_question, current_answer, answer[index]
        elif user_answer == "l":
            return 3, current_question, current_answer, answer[index]
        elif user_answer not in valid_inputs:
            print("🚫 Invalid input! Please enter a, b, c, d, l, or q.")
            continue
        else:
            return 0, current_question, current_answer, answer[index]

def Swapout(Experties_on_sub, level):
    swap_stage_1_questions = {
        "What type of word is 'quickly'?": "c",
        "What is 9 x 7?": "d",
        "What is the freezing point of water in Celsius?": "b",
        "Who was the first Prime Minister of India?": "a",
        "Which continent is the Amazon River located in?": "c",
        "What does 'CFC' stand for?": "b"
    }

    swap_stage_1_options = [
        ["Noun", "Adjective", "Adverb", "Verb"],
        ["54", "61", "72", "63"],
        ["10 degrees", "0 degrees", "32 degrees", "100 degrees"],
        ["Jawaharlal Nehru", "Sardar Patel", "B.R. Ambedkar", "Rajendra Prasad"],
        ["Asia", "Africa", "South America", "North America"],
        ["Carbon Fluorine Compound", "Chlorofluorocarbon", "Central Force Control", "Complex Fluid Chemistry"]
    ]

    swap_stage_2_questions = {
        "What literary term means a humorous imitation of a serious work?": "c",
        "If a shirt is ₹800 after a 20% discount, what was its original price?": "d",
        "Which gland in the human body produces insulin?": "b",
        "Who was the first woman to be appointed as the Speaker of the Lok Sabha?": "a",
        "The Great Barrier Reef is located off the coast of which country?": "c",
        "Which gas is responsible for the characteristic smell after a lightning strike?": "d"
    }

    swap_stage_2_options = [
        ["Allegory", "Metaphor", "Parody", "Sonnet"],
        ["₹960", "₹1080", "₹900", "₹1000"],
        ["Thyroid", "Pancreas", "Adrenal", "Pituitary"],
        ["Meira Kumar", "Sumitra Mahajan", "Sushma Swaraj", "Pratibha Patil"],
        ["Brazil", "New Zealand", "Australia", "South Africa"],
        ["Ozone", "Nitrogen Dioxide", "Sulphur Dioxide", "Ozone (O3)"]
    ]

    swap_stage_3_questions = {
        "What is the metrical foot used predominantly in Shakespearean sonnets?": "c",
        "What is the total number of diagonals in a regular dodecagon (12 sides)?": "a",
        "Which type of radioactive decay does not change the atomic number or mass number of the nucleus?": "b",
        "The Young Bengal Movement was founded by whom?": "d",
        "Which European country has the longest coastline?": "a",
        "What is the term for the total dry mass of all living organisms in a given area?": "b"
    }

    swap_stage_3_options = [
        ["Trochaic Trimeter", "Anapestic Tetrameter", "Iambic Pentameter", "Dactylic Hexameter"],
        ["54", "66", "72", "90"],
        ["Alpha decay", "Gamma decay", "Beta decay", "Electron Capture"],
        ["Rabindranath Tagore", "Ishwar Chandra Vidyasagar", "Raja Ram Mohan Roy", "Henry Louis Vivian Derozio"],
        ["Norway", "Greece", "United Kingdom", "Iceland"],
        ["Species diversity", "Biomass", "Ecosystem volume", "Net primary productivity"]
    ]

    if level >= 0 and level <= 4:
        if Experties_on_sub == "e":
            return check_fn(swap_stage_1_questions, swap_stage_1_options, 0)
        elif Experties_on_sub == "m":
            return check_fn(swap_stage_1_questions, swap_stage_1_options, 1)
        elif Experties_on_sub == "s":
            return check_fn(swap_stage_1_questions, swap_stage_1_options, 2)
        elif Experties_on_sub == "h":
            return check_fn(swap_stage_1_questions, swap_stage_1_options, 3)
        elif Experties_on_sub == "g":
            return check_fn(swap_stage_1_questions, swap_stage_1_options, 4)
        elif Experties_on_sub == "ec":
            return check_fn(swap_stage_1_questions, swap_stage_1_options, 5)

    elif level >= 5 and level <= 9:
        if Experties_on_sub == "e":
            return check_fn(swap_stage_2_questions, swap_stage_2_options, 0)
        elif Experties_on_sub == "m":
            return check_fn(swap_stage_2_questions, swap_stage_2_options, 1)
        elif Experties_on_sub == "s":
            return check_fn(swap_stage_2_questions, swap_stage_2_options, 2)
        elif Experties_on_sub == "h":
            return check_fn(swap_stage_2_questions, swap_stage_2_options, 3)
        elif Experties_on_sub == "g":
            return check_fn(swap_stage_2_questions, swap_stage_2_options, 4)
        elif Experties_on_sub == "ec":
            return check_fn(swap_stage_2_questions, swap_stage_2_options, 5)

    elif level >= 10 and level <= 14:
        if Experties_on_sub == "e":
            return check_fn(swap_stage_3_questions, swap_stage_3_options, 0)
        elif Experties_on_sub == "m":
            return check_fn(swap_stage_3_questions, swap_stage_3_options, 1)
        elif Experties_on_sub == "s":
            return check_fn(swap_stage_3_questions, swap_stage_3_options, 2)
        elif Experties_on_sub == "h":
            return check_fn(swap_stage_3_questions, swap_stage_3_options, 3)
        elif Experties_on_sub == "g":
            return check_fn(swap_stage_3_questions, swap_stage_3_options, 4)
        elif Experties_on_sub == "ec":
            return check_fn(swap_stage_3_questions, swap_stage_3_options, 5)

