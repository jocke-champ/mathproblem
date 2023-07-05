import random
import operator

# Def operators
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


def generate_problem(difficulty):
    # Start with single number
    problem = [random.randint(1, difficulty)]
    # Add operators and numbers based on difficulty
    for _ in range(difficulty):
        op = random.choice(list(ops.keys()))
        num = random.randint(1, difficulty)
        problem.extend([op, num])
    return problem


def calculate_answer(problem):
    # Start with the first number
    answer = problem[0]
    # Apply each operator in turn
    for i in range(1, len(problem), 2):
        op = ops[problem[i]]
        num = problem[i+1]
        if op == operator.truediv:
            answer = round(op(answer, num), 2) # Round to 2 decimals
        else:
            answer = op(answer, num)
    return answer


def math_game():
    score = 0
    difficulty = 1 # Start with single operator problems

    while True:
        problem = generate_problem(difficulty)
        # Convert the problem to a string to display
        problem_str = ' '.join(str(x) for x in problem)
        print(f"Vad är {problem_str}")
        answer = input()

        correct_answer = calculate_answer(problem)

        if float(answer) == correct_answer:
            print("Korrekt!")
            score += 1
            print(f"Hur har {score} poäng")
            difficulty += random.choice([0, 1]) # Randomly adds 1 to slightly increase difficulty
        else:
            print(f"Inte korrekt. Rätt svar är {correct_answer}")
            print(f"Din slutgiltiga popäng är {score}")
            break


if __name__ == "__main__":
    math_game()
