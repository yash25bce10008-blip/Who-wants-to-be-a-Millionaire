Statement of Purpose: Who Wants to be a Millionaire! (KBC Console Game)

🎯 Problem Statement

The core challenge is to create an interactive and engaging console application that accurately replicates the structure and official rules of the popular quiz show, Who Wants to be a Millionaire! (specifically, the Indian version, Kaun Banega Crorepati). The solution must prioritize modular design and robust functional implementation using core Python concepts to manage complex game state, user interactions, and specific lifeline logic.

🔭 Scope of the Project

This project is a standalone console application scoped to cover the full gameplay loop of the quiz:

Question Progression: Presentation of 16 questions of increasing difficulty.

Input Handling: Management of multiple-choice input (a, b, c, d), lifeline activation (l), and the quit option (q).

State Management: Accurate tracking and updating of prize money, including the application of Safe Levels after Question 5 (₹10,000) and Question 10 (₹3,20,000).

Lifeline Integration: Complete functional implementation of all three specified lifelines: 50/50, Audience Poll, and Swap Out. The Swap Out functionality requires specific logic to retrieve a new question based on the user's declared subject expertise.

🧑‍🤝‍🧑 Target Users

The primary target audience includes students and general audiences who:

Enjoy quiz games and want to test their general knowledge.

Seek a challenging, structured, and fun interactive format.

Are looking for a simple, readily executable console application.

⚙ High-Level Features

The architecture is built around the following high-level components to ensure separation of concerns (as outlined in the detailed project documentation):

Core Game Engine: Manages the main game loop, question flow, user interaction, and the overall answer validation mechanism.

Prize Management: Dedicated logic to track and update the player's winnings, correctly implementing the two safe money levels.

Lifeline Integration: Provides specific, callable functions (in separate modules) for 50/50, Audience Poll, and Swap Out utilities, ensuring each is used only once.

Subject Specialization: Enables the user to select a domain of expertise (English, Maths, Science, History, Geography, or Economics) which is utilized to provide a relevant replacement question when the Swap Out lifeline is chosen.
