swap_stage_1_questions = {
        "What type of word is 'quickly'?": "c",
        "What is 9 x 7?": "d",
        "What is the freezing point of water in Celsius?": "b",
        "Who was the first Prime Minister of India?": "a",
        "Which continent is the Amazon River located in?": "c",
        "What does 'CFC' stand for?": "b"
    }

swap_stage_1_options = [
        ["Noun", "Adjective", "Adverb", "Verb"],# English
        ["54", "61", "72", "63"],  # Maths
        ["10 degrees", "0 degrees", "32 degrees", "100 degrees"], # Science
        ["Jawaharlal Nehru", "Sardar Patel", "B.R. Ambedkar", "Rajendra Prasad"], # History
        ["Asia", "Africa", "South America", "North America"], # Geography
        ["Carbon Fluorine Compound", "Chlorofluorocarbon", "Central Force Control", "Complex Fluid Chemistry"] # Ecology
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
        ["Allegory", "Metaphor", "Parody", "Sonnet"], # English
        ["₹960", "₹1080", "₹900", "₹1000"],# Maths
        ["Thyroid", "Pancreas", "Adrenal", "Pituitary"], # Science
        ["Meira Kumar", "Sumitra Mahajan", "Sushma Swaraj", "Pratibha Patil"], # History
        ["Brazil", "New Zealand", "Australia", "South Africa"], # Geography
        ["Ozone", "Nitrogen Dioxide", "Sulphur Dioxide", "Ozone (O3)"] # Ecology
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
        ["Trochaic Trimeter", "Anapestic Tetrameter", "Iambic Pentameter", "Dactylic Hexameter"], # English
        ["54", "66", "72", "90"], # Maths
        ["Alpha decay", "Gamma decay", "Beta decay", "Electron Capture"], # Science
        ["Rabindranath Tagore", "Ishwar Chandra Vidyasagar", "Raja Ram Mohan Roy", "Henry Louis Vivian Derozio"], # History
        ["Norway", "Greece", "United Kingdom", "Iceland"], # Geography
        ["Species diversity", "Biomass", "Ecosystem volume", "Net primary productivity"] # Ecology
    ]

kbc_questions_answers = {
    #level1
    "How many sides does a triangle have?": "b",
    "What is the capital of India?": "c",
    "Which animal is known as the 'Ship of the Desert'?": "c",
    "What color is a stop sign?": "c",
    "Which planet is known as the Red Planet?": "b",
    
    #level2
    "Which Mughal Emperor commissioned the construction of the Jama Masjid in Delhi?": "c",
    "The historical Iron Pillar in the Qutb Complex, Delhi, is primarily associated with which ancient Indian dynasty?": "b",
    "The famous historical document, the Magna Carta, was signed in which year?": "a",
    "What is the capital city of Bhutan?": "b",
    "Which country is the setting for the majority of Fyodor Dostoevsky's novel, 'Crime and Punishment'?": "d",
    
    #level3
    "Which famous economist authored the book 'The General Theory of Employment, Interest and Money', published in 1936?": "c",
    "The 'Treaty of Tordesillas' (1494) primarily divided the new world lands between which two colonial powers?": "b",
    "Which Indian state has the highest number of Lok Sabha (Lower House of Parliament) constituencies?": "d",
    "The ancient city of Persepolis, the capital of the Achaemenid Empire, is located in the modern-day country of:": "c",
    "Who was the only person to serve as both the President of India and the Vice-President of the United Nations General Assembly?": "c",
    "Which is the only sea in the world that has no coastline, being defined entirely by ocean currents?": "c"
}

kbc_options_list = [
    # Q1: How many sides does a triangle have?
    ["2", "3", "4", "5"],
    # Q2: What is the capital of India?
    ["Mumbai", "Kolkata", "New Delhi", "Chennai"],
    # Q3: Which animal is known as the 'Ship of the Desert'?
    ["Lion", "Tiger", "Camel", "Elephant"],
    # Q4: What color is a stop sign?
    ["Yellow", "Green", "Red", "Blue"],
    # Q5: Which planet is known as the Red Planet?
    ["Earth", "Mars", "Jupiter", "Venus"],
    
    # Q6: Which Mughal Emperor...
    ["Akbar", "Humayun", "Shah Jahan", "Aurangzeb"],
    # Q7: The historical Iron Pillar...
    ["Mauryan", "Gupta", "Chola", "Satavahana"],
    # Q8: The famous historical document...
    ["1215", "1492", "1066", "1776"],
    # Q9: What is the capital city of Bhutan?
    ["Paro", "Thimphu", "Punakha", "Gelephu"],
    # Q10: Which country is the setting for...
    ["France", "Poland", "Germany", "Russia"],
    
    # Q11: Which famous economist...
    ["Adam Smith", "Karl Marx", "John Maynard Keynes", "Milton Friedman"],
    # Q12: The 'Treaty of Tordesillas'...
    ["England and France", "Spain and Portugal", "Netherlands and Spain", "France and Portugal"],
    # Q13: Which Indian state has the highest...
    ["Maharashtra", "West Bengal", "Bihar", "Uttar Pradesh"],
    # Q14: The ancient city of Persepolis...
    ["Turkey", "Iraq", "Iran", "Egypt"],
    # Q15: Who was the only person to serve...
    ["V.V. Giri", "Dr. Zakir Husain", "Sarvepalli Radhakrishnan", "R. Venkataraman"],
    # Q16: Which is the only sea in the world...
    ["Caspian Sea", "Black Sea", "Sargasso Sea", "Coral Sea"]
]
kbc_prize_money = [
    # Level 1 (Q1-Q5: Easy)
    1000, 2000, 3000, 5000, 10000,
    # Level 2 (Q6-Q10: Medium)
    20000, 40000, 80000, 160000, 320000,
    # Level 3 (Q11-Q16: Hard/Mega Prize)
    640000, 1250000, 2500000, 5000000, 10000000, 70000000 # Rs 7 Crore Final
]
