import random


def is_even(number):
    return number % 2 == 0


def main():
    print('Welcome to the Brain Games!')
    
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers_needed = 3
    correct_answers = 0
    
    while correct_answers < correct_answers_needed:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        
        user_answer = input('Your answer: ').strip().lower()
        correct_answer = 'yes' if is_even(number) else 'no'
        
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            error_msg = f"'{user_answer}' is wrong answer ;(. "
            error_msg += f"Correct answer was '{correct_answer}'."
            print(error_msg)
            print(f"Let's try again, {name}!")
            return
    
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
