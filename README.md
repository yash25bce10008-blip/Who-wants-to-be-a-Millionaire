🏆 Who wants to be a Millionaire! (KBC Console Game)

💡 Overview of the Project This project is a console-based implementation of the popular quiz show, "Who Wants to Be a Millionaire!" (or Kaun Banega Crorepati - KBC). It challenges the user with a series of multiple-choice questions of increasing difficulty, offering a prize money structure and three distinct lifelines to assist the player. The game features essential safe levels to ensure the player walks away with a guaranteed minimum prize even after a wrong answer.

✨ Features The KBC Console Game includes the following core functionalities:

Question Progression: The game progresses through 16 questions with escalating prize money, leading up to the top prize of ₹7 Crore.

Three Lifelines: Players are equipped with three distinct lifelines, usable once each:

50/50: Removes two incorrect options, leaving the correct answer and one incorrect option.

Audience Poll: Provides percentage-based support for each option, with a higher percentage favoring the correct answer.

Swap Out: Replaces the current question with an easier question based on the user's pre-selected area of expertise (English, Maths, Science, History, Geography, or Economics).

Safe Levels: The player secures a guaranteed safe prize amount after completing:

Question 5: ₹10,000

Question 10: ₹3,20,000

Quit Option: Players can choose to quit at any point to walk away with their current accumulated prize money.

🛠 Technologies/Tools Used Programming Language: Python 3.x

Structure: Modular design utilizing multiple Python files/modules (main_kbc.py, data_module.py, swap_module.py, lifeline_module.py) for separation of concerns.

🎯 Foundational Implementation Focus

The architecture of the KBC Console Game is designed to showcase proficiency in core programming concepts. The entire logic, including question management, lifeline processing, and prize money tracking, is implemented using native Python functionalities. This approach intentionally avoids external modules or advanced paradigms like Object-Oriented Programming (OOP), relying instead on fundamental tools such as lists, tuples, conditional statements, loops, and custom functions to ensure the code base is highly readable, easily maintainable, and demonstrates a strong command of the language's basic building blocks."

🚀 Steps to Install & Run the Project Prerequisites Ensure Python 3.x is installed on your operating system.

Download Files Save the following project files into a single directory:

main_kbc.py data_module.py swap_module.py lifeline_module.py

Run the Game Open your console or terminal Navigate to the project directory. Execute the main file using the Python interpreter: python main_kbc.py

✅ Instructions for Testing The primary mode of testing is through validation tests by playing the game and verifying the core mechanics:

Gameplay Testing: Play multiple full games to test the core loop, including answering questions, prize money accumulation, and the quit functionality.

Lifeline Testing: Verify that each lifeline (50/50, Audience Poll, Swap Out) works as intended when invoked, and correctly becomes unavailable after a single use.

Safe Level Testing:

Answer correctly up to Question 5 (and then 10).

Answer the next question incorrectly to confirm the take-home prize money is correctly set to the safe level amount (₹10,000 and ₹3,20,000, respectively).

Input Validation Testing: Attempt to enter invalid inputs (e.g., non-letter/non-digit characters, options out of range, or attempting to use an already-used lifeline code) to ensure the game's validation logic handles them gracefully.
