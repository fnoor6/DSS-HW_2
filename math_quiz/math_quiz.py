import random


def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generates a random arithmetic operator: +, -, or *.
    """
    return random.choice(['+', '-', '*'])


def generate_problem_and_answer(num1, num2, operator):
    """
    Generates a math problem and its correct answer.
    """
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    problem = f"{num1} {operator} {num2}"
    return problem, answer


def math_quiz():
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 6)
        operator = generate_random_operator()

        problem, answer = generate_problem_and_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        while True:
            user_answer = input("Your answer: ")
            try:
                user_answer = int(user_answer)
                break  # Exit the loop if the input is valid
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
