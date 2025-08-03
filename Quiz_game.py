# KBC Game - Beginner Version using Lists

# Questions, options, and answers stored in lists
questions = [
    "What is the capital of India?",
    "Who is known as the father of computers?",
    "Which planet is known as the Red Planet?",
    "What is the national bird of India?"
]

options = [
    ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Charles Babbage", "B. Newton", "C. Alan Turing", "D. Einstein"],
    ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    ["A. Crow", "B. Pigeon", "C. Peacock", "D. Eagle"]
]

answers = ['B', 'A', 'B', 'C']  # Correct options
prizes = [1000, 5000, 10000, 20000]  # Prize for each correct answer

amount_won = 0

# Welcome message
print("🎉 Welcome to KBC - Kaun Banega Crorepati 🎉\n")
print("Answer the following questions to win money!\n")

# Game loop
for i in range(len(questions)):
    print(f"Q{i+1}. {questions[i]}")
    for opt in options[i]:
        print(opt)
    user_ans = input("Enter your answer (A/B/C/D): ").strip().upper()

    if user_ans == answers[i]:
        amount_won += prizes[i]
        print(f"✅ Correct! You have won ₹{amount_won}\n")
    else:
        print("❌ Wrong answer! Game Over.")
        break

# Final message
print(f"🎁 You are taking home ₹{amount_won}! Thanks for playing KBC.")
