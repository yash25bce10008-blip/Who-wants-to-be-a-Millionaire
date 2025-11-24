lifeline = ["a:swap", "b:fifty", "c:audience"]

kbc_questions_answers = {
    # level1
    "How many sides does a triangle have?": "b",
    "What is the capital of India?": "c",
    "Which animal is known as the 'Ship of the Desert'?": "c",
    "What color is a stop sign?": "c",
    "Which planet is known as the Red Planet?": "b",
    
    # level2
    "Which Mughal Emperor commissioned the construction of the Jama Masjid in Delhi?": "c",
    "The historical Iron Pillar in the Qutb Complex, Delhi, is primarily associated with which ancient Indian dynasty?": "b",
    "The famous historical document, the Magna Carta, was signed in which year?": "a",
    "What is the capital city of Bhutan?": "b",
    "Which country is the setting for the majority of Fyodor Dostoevsky's novel, 'Crime and Punishment'?": "d",
    
    # level3
    "Which famous economist authored the book 'The General Theory of Employment, Interest and Money', published in 1936?": "c",
    "The 'Treaty of Tordesillas' (1494) primarily divided the new world lands between which two colonial powers?": "b",
    "Which Indian state has the highest number of Lok Sabha (Lower House of Parliament) constituencies?": "d",
    "The ancient city of Persepolis, the capital of the Achaemenid Empire, is located in the modern-day country of:": "c",
    "Who was the only person to serve as both the President of India and the Vice-President of the United Nations General Assembly?": "c",
    "Which is the only sea in the world that has no coastline, being defined entirely by ocean currents?": "c"
}

kbc_options_list = [
    # Level1 Options
    ["2", "3", "4", "5"],                    # Q1
    ["Mumbai", "Kolkata", "New Delhi", "Chennai"],   # Q2
    ["Lion", "Tiger", "Camel", "Elephant"],          # Q3
    ["Yellow", "Green", "Red", "Blue"],             # Q4
    ["Earth", "Mars", "Jupiter", "Venus"],          # Q5
    
    # Level2 Options
    ["Akbar", "Humayun", "Shah Jahan", "Aurangzeb"],   # Q6
    ["Mauryan", "Gupta", "Chola", "Satavahana"],       # Q7
    ["1215", "1492", "1066", "1776"],                  # Q8
    ["Paro", "Thimphu", "Punakha", "Gelephu"],         # Q9
    ["France", "Poland", "Germany", "Russia"],         # Q10
    
    # Level3 Options
    ["Adam Smith", "Karl Marx", "John Maynard Keynes", "Milton Friedman"],  # Q11
    ["England and France", "Spain and Portugal", "Netherlands and Spain", "France and Portugal"],  # Q12
    ["Maharashtra", "West Bengal", "Bihar", "Uttar Pradesh"],  # Q13
    ["Turkey", "Iraq", "Iran", "Egypt"],                      # Q14
    ["V.V. Giri", "Dr. Zakir Husain", "Sarvepalli Radhakrishnan", "R. Venkataraman"],  # Q15
    ["Caspian Sea", "Black Sea", "Sargasso Sea", "Coral Sea"]               # Q16
]

kbc_prize_money = [
    # Level1 (Q1-Q5)
    1000, 2000, 3000, 5000, 10000,
    # Level2 (Q6-Q10)
    20000, 40000, 80000, 160000, 320000,
    # Level3 (Q11-Q16)
    640000, 1250000, 2500000, 5000000, 10000000, 70000000
]