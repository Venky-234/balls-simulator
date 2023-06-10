import random

def random_verticies():
    a = random.randint(100, 500)
    b = random.randint(100, 500)
    random_verticies = [a,b]
    return random_verticies 

def random_size():
    a = random.randint(0,80)
    return a

def random_color():
    return [
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
    ]

print(random_verticies())

