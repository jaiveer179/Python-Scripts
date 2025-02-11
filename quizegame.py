def quiz_game():
    questions = [
        {"question": "What is the capital of Rajasthan?", "answer": "jaipur"},
        {"question": "What is the square root of 16?", "answer": "4"},
        {"question": "Who is bapu'?", "answer": "mathama  gandhi"}
    ]
    
    score = 0  # Initialize score
    
    print("Welcome to the Quiz Game!\n")
    
    # Loop through each question
    for q in questions:
        user_answer = input(q["question"] + " ")
        if user_answer.strip().lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")
        print()
    
    # Final feedback
    print(f"Your total score is: {score}/{len(questions)}")
    if score == len(questions):
        print("Great job! You got all answers correct!")
    elif score > 0:
        print("Nice work! Keep practicing.")
    else:
        print("Better luck next time!")

# Run the game
quiz_game()
