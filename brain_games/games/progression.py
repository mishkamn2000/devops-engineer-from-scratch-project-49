import random

GAME_RULE = 'What number is missing in the progression?'


def generate_progression(start, step, length):
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))
    return progression


def generate_round():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(progression)
    
    return question, correct_answer
