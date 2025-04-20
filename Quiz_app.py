import time

def quiz_app_with_timer():
    questions = [
        ("What is the capital of India?", "Delhi"),
        ("What is 2 + 2?", "4"),
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("What is the chemical symbol for water?","H2O"),
        ("How many planets are in our solar system?","8"),
    ]
    
    score = 0
    timer_limit = 10  # Set timer for each question in seconds

    print("Welcome to the Quiz App with Timer!")
    print(f"You have {timer_limit} seconds to answer each question.")
    print()

    for question, correct_answer in questions:
        print(question)
        start_time = time.time()
        user_answer = input(f"Answer (You have {timer_limit} seconds): ")

        # Calculate time taken for the user to respond
        time_taken = time.time() - start_time


        # Check if the time taken exceeds the allowed time
        if time_taken > timer_limit:
            print(f"Time's up! go to the next Question.")
        else:
            if user_answer.strip().lower() == correct_answer.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")

        print(f"Time taken: {time_taken:.2f} seconds")
        print()

    
    if score == 5:
        print("Great job!")
        print(f"You got {score} out of 5.")
    elif score >= 2:
        print("Good job!")
        print(f"You got {score} out of 5.")
    else:
        print("Good efforts! but needs to improve!")
        print(f"You got {score} out of 5.")

quiz_app_with_timer()
